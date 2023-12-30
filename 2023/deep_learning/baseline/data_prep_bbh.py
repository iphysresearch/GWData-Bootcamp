
from __future__ import division

import lal
import lalsimulation
from lal.antenna import AntennaResponse
from lal import MSUN_SI, C_SI, G_SI

import os
import sys
import argparse
import time
import numpy as np
from six.moves import cPickle
from scipy.signal import filtfilt, butter
from scipy.optimize import brentq
from scipy import integrate, interpolate


if sys.version_info >= (3, 0):
    xrange = range

safe = 2    # define the safe multiplication scale for the desired time length

class bbhparams:
    def __init__(self,mc,M,eta,m1,m2,ra,dec,iota,phi,psi,idx,fmin,snr,SNR):
        self.mc = mc
        self.M = M
        self.eta = eta
        self.m1 = m1
        self.m2 = m2
        self.ra = ra
        self.dec = dec
        self.iota = iota
        self.phi = phi
        self.psi = psi
        self.idx = idx
        self.fmin = fmin
        self.snr = snr
        self.SNR = SNR

def tukey(M,alpha=0.5):
    """
    Tukey window code copied from scipy
    """
    n = np.arange(0, M)
    width = int(np.floor(alpha*(M-1)/2.0))
    n1 = n[0:width+1]
    n2 = n[width+1:M-width-1]
    n3 = n[M-width-1:]

    w1 = 0.5 * (1 + np.cos(np.pi * (-1 + 2.0*n1/alpha/(M-1))))
    w2 = np.ones(n2.shape)
    w3 = 0.5 * (1 + np.cos(np.pi * (-2.0/alpha + 1 + 2.0*n3/alpha/(M-1))))
    w = np.concatenate((w1, w2, w3))

    return np.array(w[:M])

def parser():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser(prog='data_prep.py',description='generates GW data for application of deep learning networks.')

    # arguments for reading in a data file
    parser.add_argument('-N', '--Nsamp', type=int, default=7000, help='the number of samples')
    #parser.add_argument('-Nv', '--Nvalid', type=int, default=1500, help='the number of validation samples')
    #parser.add_argument('-Nt', '--Ntest', type=int, default=1500, help='the number of testing samples')
    parser.add_argument('-Nn', '--Nnoise', type=int, default=25, help='the number of noise realisations per signal')
    parser.add_argument('-Nb', '--Nblock', type=int, default=10000, help='the number of training samples per output file')
    parser.add_argument('-f', '--fsample', type=int, default=8192, help='the sampling frequency (Hz)')
    parser.add_argument('-T', '--Tobs', type=int, default=1, help='the observation duration (sec)')
    parser.add_argument('-s', '--snr', type=float, default=None, help='the signal integrated SNR')
    parser.add_argument('-I', '--detectors', type=str, nargs='+',default=['H1','L1'], help='the detectors to use')
    parser.add_argument('-b', '--basename', type=str,default='test', help='output file path and basename')
    parser.add_argument('-m', '--mdist', type=str, default='astro', help='mass distribution for training (astro,gh,metric)')
    parser.add_argument('-z', '--seed', type=int, default=1, help='the random seed')

    return parser.parse_args()

def convert_beta(beta,fs,T_obs):
    """
    Converts beta values (fractions defining a desired period of time in
    central output window) into indices for the full safe time window
    """
    # pick new random max amplitude sample location - within beta fractions
    # and slide waveform to that location
    newbeta = np.array([(beta[0] + 0.5*safe - 0.5),(beta[1] + 0.5*safe - 0.5)])/safe
    low_idx = int(T_obs*fs*newbeta[0])
    high_idx = int(T_obs*fs*newbeta[1])

    return low_idx,high_idx

def gen_noise(fs,T_obs,psd):
    """
    Generates noise from a psd
    """

    N = T_obs * fs          # the total number of time samples
    Nf = N // 2 + 1
    dt = 1 / fs             # the sampling time (sec)
    df = 1 / T_obs

    amp = np.sqrt(0.25*T_obs*psd)
    idx = np.argwhere(psd==0.0)
    amp[idx] = 0.0
    re = amp*np.random.normal(0,1,Nf)
    im = amp*np.random.normal(0,1,Nf)
    re[0] = 0.0
    im[0] = 0.0
    x = N*np.fft.irfft(re + 1j*im)*df

    return x

def gen_psd(fs,T_obs,op='AdvDesign',det='H1'):
    """
    generates noise for a variety of different detectors
    """
    N = T_obs * fs          # the total number of time samples
    dt = 1 / fs             # the sampling time (sec)
    df = 1 / T_obs          # the frequency resolution
    psd = lal.CreateREAL8FrequencySeries(None, lal.LIGOTimeGPS(0), 0.0, df,lal.HertzUnit, N // 2 + 1)

    if det=='H1' or det=='L1':
        if op == 'AdvDesign':
            lalsimulation.SimNoisePSDAdVDesignSensitivityP1200087(psd, 10.0)
        elif op == 'AdvEarlyLow':
            lalsimulation.SimNoisePSDAdVEarlyLowSensitivityP1200087(psd, 10.0)
        elif op == 'AdvEarlyHigh':
            lalsimulation.SimNoisePSDAdVEarlyHighSensitivityP1200087(psd, 10.0)
        elif op == 'AdvMidLow':
            lalsimulation.SimNoisePSDAdVMidLowSensitivityP1200087(psd, 10.0)
        elif op == 'AdvMidHigh':
            lalsimulation.SimNoisePSDAdVMidHighSensitivityP1200087(psd, 10.0)
        elif op == 'AdvLateLow':
            lalsimulation.SimNoisePSDAdVLateLowSensitivityP1200087(psd, 10.0)
        elif op == 'AdvLateHigh':
            lalsimulation.SimNoisePSDAdVLateHighSensitivityP1200087(psd, 10.0)
        else:
            print('unknown noise option')
            exit(1)
    else:
        print('unknown detector - will add Virgo soon')
        exit(1)

    return psd

def get_snr(data,T_obs,fs,psd,fmin):
    """
    computes the snr of a signal given a PSD starting from a particular frequency index
    """

    N = T_obs*fs
    df = 1.0/T_obs
    dt = 1.0/fs
    fidx = int(fmin/df)

    win = tukey(N,alpha=1.0/8.0)
    idx = np.argwhere(psd>0.0)
    invpsd = np.zeros(psd.size)
    invpsd[idx] = 1.0/psd[idx]

    xf = np.fft.rfft(data*win)*dt
    SNRsq = 4.0*np.sum((np.abs(xf[fidx:])**2)*invpsd[fidx:])*df
    return np.sqrt(SNRsq)

def whiten_data(data,duration,sample_rate,psd,flag='td'):
    """
    Takes an input timeseries and whitens it according to a psd
    """

    if flag=='td':
        # FT the input timeseries - window first
        win = tukey(duration*sample_rate,alpha=1.0/8.0)
        xf = np.fft.rfft(win*data)
    else:
        xf = data

    # deal with undefined PDS bins and normalise
    idx = np.argwhere(psd>0.0)
    invpsd = np.zeros(psd.size)
    invpsd[idx] = 1.0/psd[idx]
    xf *= np.sqrt(2.0*invpsd/sample_rate)

    # Detrend the data: no DC component.
    xf[0] = 0.0

    if flag=='td':
        # Return to time domain.
        x = np.fft.irfft(xf)
        return x
    else:
        return xf

def gen_masses(m_min=5.0,M_max=100.0,mdist='astro',verbose=True):
    """
    function returns a pair of masses drawn from the appropriate distribution
    """

    flag = False
    if mdist=='astro':
        if verbose:
            print('{}: using astrophysical logarithmic mass distribution'.format(time.asctime()))
        new_m_min = m_min
        new_M_max = M_max
        log_m_max = np.log(new_M_max - new_m_min)
        while not flag:
            m12 = np.exp(np.log(new_m_min) + np.random.uniform(0,1,2)*(log_m_max-np.log(new_m_min)))
            flag = True if (np.sum(m12)<new_M_max) and (np.all(m12>new_m_min)) and (m12[0]>=m12[1]) else False
        eta = m12[0]*m12[1]/(m12[0]+m12[1])**2
        mc = np.sum(m12)*eta**(3.0/5.0)
        return m12, mc, eta
    elif mdist=='gh':
        if verbose:
            print('{}: using George & Huerta mass distribution'.format(time.asctime()))
        m12 = np.zeros(2)
        while not flag:
            q = np.random.uniform(1.0,10.0,1)
            m12[1] = np.random.uniform(5.0,75.0,1)
            m12[0] = m12[1]*q
            flag = True if (np.all(m12<75.0)) and (np.all(m12>5.0)) and (m12[0]>=m12[1]) else False
        eta = m12[0]*m12[1]/(m12[0]+m12[1])**2
        mc = np.sum(m12)*eta**(3.0/5.0)
        return m12, mc, eta
    elif mdist=='metric':
        if verbose:
            print('{}: using metric based mass distribution'.format(time.asctime()))
        new_m_min = m_min
        new_M_max = M_max
        new_M_min = 2.0*new_m_min
        eta_min = m_min*(new_M_max-new_m_min)/new_M_max**2
        while not flag:
            M = (new_M_min**(-7.0/3.0) - np.random.uniform(0,1,1)*(new_M_min**(-7.0/3.0) - new_M_max**(-7.0/3.0)))**(-3.0/7.0)
            eta = (eta_min**(-2.0) - np.random.uniform(0,1,1)*(eta_min**(-2.0) - 16.0))**(-1.0/2.0)
            m12 = np.zeros(2)
            m12[0] = 0.5*M + M*np.sqrt(0.25-eta)
            m12[1] = M - m12[0]
            flag = True if (np.sum(m12)<new_M_max) and (np.all(m12>new_m_min)) and (m12[0]>=m12[1]) else False
        mc = np.sum(m12)*eta**(3.0/5.0)
        return m12, mc, eta
    else:
        print('{}: ERROR, unknown mass distribution. Exiting.'.format(time.asctime()))
        exit(1)

def get_fmin(M,eta,dt,verbose):
    """
    Compute the instantaneous frequency given a time till merger
    """
    M_SI = M*MSUN_SI

    def dtchirp(f):
        """
        The chirp time to 2nd PN order
        """
        v = ((G_SI/C_SI**3)*M_SI*np.pi*f)**(1.0/3.0)
        temp = (v**(-8.0) + ((743.0/252.0) + 11.0*eta/3.0)*v**(-6.0) -
                (32*np.pi/5.0)*v**(-5.0) + ((3058673.0/508032.0) + 5429*eta/504.0 +
                (617.0/72.0)*eta**2)*v**(-4.0))
        return (5.0/(256.0*eta))*(G_SI/C_SI**3)*M_SI*temp - dt

    # solve for the frequency between limits
    fmin = brentq(dtchirp, 1.0, 2000.0, xtol=1e-6)
    if verbose:
        print('{}: signal enters segment at {} Hz'.format(time.asctime(),fmin))

    return fmin

def gen_par(fs,T_obs,mdist='astro',beta=[0.75,0.95],verbose=True):
    """
    Generates a random set of parameters
    """
    # define distribution params
    m_min = 5.0         # rest frame component masses
    M_max = 100.0       # rest frame total mass
    log_m_max = np.log(M_max - m_min)

    m12, mc, eta = gen_masses(m_min,M_max,mdist=mdist,verbose=verbose)
    M = np.sum(m12)
    if verbose:
        print('{}: selected bbh masses = {},{} (chirp mass = {})'.format(time.asctime(),m12[0],m12[1],mc))

    # generate iota
    iota = np.arccos(-1.0 + 2.0*np.random.rand())
    if verbose:
        print('{}: selected bbh cos(inclination) = {}'.format(time.asctime(),np.cos(iota)))

    # generate polarisation angle
    psi = 2.0*np.pi*np.random.rand()
    if verbose:
        print('{}: selected bbh polarisation = {}'.format(time.asctime(),psi))

    # generate reference phase
    phi = 2.0*np.pi*np.random.rand()
    if verbose:
        print('{}: selected bbh reference phase = {}'.format(time.asctime(),phi))

    # pick sky position - uniform on the 2-sphere
    ra = 2.0*np.pi*np.random.rand()
    dec = np.arcsin(-1.0 + 2.0*np.random.rand())
    if verbose:
        print('{}: selected bbh sky position = {},{}'.format(time.asctime(),ra,dec))

    # pick new random max amplitude sample location - within beta fractions
    # and slide waveform to that location
    low_idx,high_idx = convert_beta(beta,fs,T_obs)
    if low_idx==high_idx:
        idx = low_idx
    else:
        idx = int(np.random.randint(low_idx,high_idx,1)[0])
    if verbose:
        print('{}: selected bbh peak amplitude time = {}'.format(time.asctime(),idx/fs))

    # the start index of the central region
    sidx = int(0.5*fs*T_obs*(safe-1.0)/safe)

    # compute SNR of pre-whitened data
    fmin = get_fmin(M,eta,int(idx-sidx)/fs,verbose)
    if verbose:
        print('{}: computed starting frequency = {} Hz'.format(time.asctime(),fmin))

    # store params
    par = bbhparams(mc,M,eta,m12[0],m12[1],ra,dec,np.cos(iota),phi,psi,idx,fmin,None,None)

    return par

def gen_bbh(fs,T_obs,psds,snr=1.0,dets=['H1'],beta=[0.75,0.95],par=None,verbose=True):
    """
    generates a BBH timedomain signal
    """
    N = T_obs * fs      # the total number of time samples
    dt = 1 / fs             # the sampling time (sec)
    f_low = 12.0            # lowest frequency of waveform (Hz)
    amplitude_order = 0
    phase_order = 7
    approximant = lalsimulation.IMRPhenomD
    dist = 1e6*lal.PC_SI  # put it as 1 MPc

    # make waveform
    # loop until we have a long enough waveform - slowly reduce flow as needed
    flag = False
    while not flag:
        hp, hc = lalsimulation.SimInspiralChooseTDWaveform(
                    par.m1 * lal.MSUN_SI, par.m2 * lal.MSUN_SI,
                    0, 0, 0, 0, 0, 0,
                    dist,
                    par.iota, par.phi, 0,
                    0, 0,
                    1 / fs,
                    f_low,f_low,
                    lal.CreateDict(),
                    approximant)
        flag = True if hp.data.length>2*N else False
        f_low -= 1       # decrease by 1 Hz each time
    orig_hp = hp.data.data
    orig_hc = hc.data.data

    # compute reference idx
    ref_idx = np.argmax(orig_hp**2 + orig_hc**2)

    # the start index of the central region
    sidx = int(0.5*fs*T_obs*(safe-1.0)/safe)

    # make aggressive window to cut out signal in central region
    # window is non-flat for 1/8 of desired Tobs
    # the window has dropped to 50% at the Tobs boundaries
    win = np.zeros(N)
    tempwin = tukey(int((16.0/15.0)*N/safe),alpha=1.0/8.0)
    win[int((N-tempwin.size)/2):int((N-tempwin.size)/2)+tempwin.size] = tempwin

    # loop over detectors
    ndet = len(psds)
    ts = np.zeros((ndet,N))
    hp = np.zeros((ndet,N))
    hc = np.zeros((ndet,N))
    intsnr = []
    j = 0
    for det,psd in zip(dets,psds):

        # make signal - apply antenna and shifts
        ht_shift, hp_shift, hc_shift = make_bbh(orig_hp,orig_hc,fs,par.ra,par.dec,par.psi,det,verbose)

        # place signal into timeseries - including shift
        ht_temp = ht_shift[int(ref_idx-par.idx):]
        hp_temp = hp_shift[int(ref_idx-par.idx):]
        hc_temp = hc_shift[int(ref_idx-par.idx):]
        if len(ht_temp)<N:
            ts[j,:len(ht_temp)] = ht_temp
            hp[j,:len(ht_temp)] = hp_temp
            hc[j,:len(ht_temp)] = hc_temp
        else:
            ts[j,:] = ht_temp[:N]
            hp[j,:] = hp_temp[:N]
            hc[j,:] = hc_temp[:N]

        # apply aggressive window to cut out signal in central region
        # window is non-flat for 1/8 of desired Tobs
        # the window has dropped to 50% at the Tobs boundaries
        ts[j,:] *= win
        hp[j,:] *= win
        hc[j,:] *= win

        # compute SNR of pre-whitened data
        intsnr.append(get_snr(ts[j,:],T_obs,fs,psd.data.data,par.fmin))

    # normalise the waveform using either integrated or peak SNR
    intsnr = np.array(intsnr)
    scale = snr/np.sqrt(np.sum(intsnr**2))
    ts *= scale
    hp *= scale
    hc *= scale
    intsnr *= scale
    if verbose:
        print('{}: computed the network SNR = {}'.format(time.asctime(),snr))

    return ts, hp, hc

def make_bbh(hp,hc,fs,ra,dec,psi,det,verbose):
    """
    turns hplus and hcross into a detector output
    applies antenna response and
    and applies correct time delays to each detector
    """

    # make basic time vector
    tvec = np.arange(len(hp))/float(fs)

    # compute antenna response and apply
    resp = AntennaResponse(det, ra, dec, psi,scalar=True, vector=True, times=0.0)
    Fp = resp.plus
    Fc = resp.cross
    ht = hp*Fp + hc*Fc     # overwrite the timeseries vector to reuse it

    # compute time delays relative to Earth centre
    frDetector =  lalsimulation.DetectorPrefixToLALDetector(det)
    tdelay = lal.TimeDelayFromEarthCenter(frDetector.location,ra,dec,0.0)
    if verbose:
        print('{}: computed {} Earth centre time delay = {}'.format(time.asctime(),det,tdelay))

    # interpolate to get time shifted signal
    ht_tck = interpolate.splrep(tvec, ht, s=0)
    hp_tck = interpolate.splrep(tvec, hp, s=0)
    hc_tck = interpolate.splrep(tvec, hc, s=0)
    tnew = tvec + tdelay
    new_ht = interpolate.splev(tnew, ht_tck, der=0,ext=1)
    new_hp = interpolate.splev(tnew, hp_tck, der=0,ext=1)
    new_hc = interpolate.splev(tnew, hc_tck, der=0,ext=1)

    return new_ht, new_hp, new_hc

def sim_data(fs,T_obs,snr=1.0,dets=['H1'],Nnoise=25,size=1000,mdist='astro',beta=[0.75,0.95], verbose=True):
    """
    Simulates all of the test, validation and training data timeseries
    """

    yval = []       # initialise the param output
    ts = []         # initialise the timeseries output
    par = []        # initialise the parameter output
    nclass = 2      # the hardcoded number of classes
    npclass = int(size/float(nclass))
    ndet = len(dets)               # the number of detectors
    psds = [gen_psd(fs,T_obs,op='AdvDesign',det=d) for d in dets]

    # for the noise class
    for x in xrange(npclass):
        if verbose:
            print('{}: making a noise only instance'.format(time.asctime()))
        ts_new = np.array([gen_noise(fs,T_obs,psd.data.data) for psd in psds]).reshape(ndet,-1)
        ts.append(np.array([whiten_data(t,T_obs,fs,psd.data.data) for t,psd in zip(ts_new,psds)]).reshape(ndet,-1))
        par.append(None)
        yval.append(0)
        if verbose:
            print('{}: completed {}/{} noise samples'.format(time.asctime(),x+1,npclass))

    # for the signal class - loop over random masses
    cnt = npclass
    while cnt < size:

        # generate a single new timeseries and chirpmass
        par_new = gen_par(fs,T_obs,mdist=mdist,beta=beta,verbose=verbose)
        ts_new,_,_ = gen_bbh(fs,T_obs,psds,snr=snr,dets=dets,beta=beta,par=par_new,verbose=verbose)

        # loop over noise realisations
        for j in xrange(Nnoise):
            ts_noise = np.array([gen_noise(fs,T_obs,psd.data.data) for psd in psds]).reshape(ndet,-1)
            ts.append(np.array([whiten_data(t,T_obs,fs,psd.data.data) for t,psd in zip(ts_noise+ts_new,psds)]).reshape(ndet,-1))
            par.append(par_new)
            yval.append(1)
            cnt += 1
        if verbose:
            print('{}: completed {}/{} signal samples'.format(time.asctime(),cnt-npclass,int(size/2)))

    # trim the data down to desired length
    ts = np.array(ts)[:size]
    yval = np.array(yval)[:size]
    par = par[:size]

    # return randomised the data
    idx = np.random.permutation(size)
    temp = [par[i] for i in idx]
    return [ts[idx], yval[idx]], temp

# the main part of the code
def main():
    """
    The main code - generates the training, validation and test samples
    """
    snr_mn = 0.0
    snr_cnt = 0

    # get the command line args
    args = parser()
    if args.seed>0:
        np.random.seed(args.seed)
    safeTobs = safe*args.Tobs

    # break up the generation into blocks of args.Nblock training samples
    nblock = int(np.ceil(float(args.Nsamp)/float(args.Nblock)))
    for i in xrange(nblock):

    	# simulate the dataset and randomise it
        # only use Nnoise for the training data NOT the validation and test
    	print('{}: starting to generate data'.format(time.asctime()))
    	ts, par = sim_data(args.fsample,safeTobs,args.snr,args.detectors,args.Nnoise,size=args.Nblock,mdist=args.mdist,beta=[0.75,0.95])
    	print('{}: completed generating data {}/{}'.format(time.asctime(),i+1,nblock))

    	# pickle the results
    	# save the timeseries data to file
    	f = open(args.basename + '_ts_' + str(i) + '.sav', 'wb')
    	cPickle.dump(ts, f, protocol=cPickle.HIGHEST_PROTOCOL)
    	f.close()
    	print('{}: saved timeseries data to file'.format(time.asctime()))

    	# save the sample parameters to file
    	f = open(args.basename + '_params_' + str(i) + '.sav', 'wb')
    	cPickle.dump(par, f, protocol=cPickle.HIGHEST_PROTOCOL)
    	f.close()
    	print('{}: saved parameter data to file'.format(time.asctime()))

    print('{}: success'.format(time.asctime()))

if __name__ == "__main__":
    exit(main())