FROM ubuntu:20.04
LABEL MAINTAINER="He Wang<hewang@ucas.ac.cn>"
ARG RELEASE_NAME=focal
ARG ROOT_PASSWD=root
ENV SSH_PORT 22
ENV PATH /root/miniconda3/bin:$PATH
# Open port
EXPOSE 8888
EXPOSE 22
#
# UTF-8 encoding to support chs characters
#
RUN echo "export LANG=C.UTF-8" >>/etc/profile \
#
# apt sources backup
#
&& cp /etc/apt/sources.list /etc/apt/sources.list.bak \
#
# switch apt source to TUNA
#
&& echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ release-name main restricted universe multiverse\n\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ release-name-updates main restricted universe multiverse\n\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ release-name-backports main restricted universe multiverse\n\
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ release-name-security main restricted universe multiverse" >/etc/apt/sources.list \
&& sed -i 's/release-name/'$RELEASE_NAME'/g' /etc/apt/sources.list \
#
# remove nvidia sources
#
# && rm /etc/apt/sources.list.d/cuda.list /etc/apt/sources.list.d/nvidia-ml.list \
#
# install necessary packages
#
&& apt-get update \
&& apt-get install -y --no-install-recommends \
  build-essential \
  apt-utils \
  vim \
  openssh-server \
  net-tools \
  iputils-ping \
  wget \
  curl \
  git \
  iptables \
  bzip2 \
  command-not-found \
  ca-certificates \
#
# download & install miniconda
#
&& wget -q https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh \
&& bash Miniconda3-latest-Linux-x86_64.sh -b \
&& rm Miniconda3-latest-Linux-x86_64.sh \
&& ln -s /root/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
#
# switch conda source to TUNA
#
&& echo "channels:\n\
  - defaults\n\
show_channel_urls: true\n\
default_channels:\n\
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main\n\
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r\n\
custom_channels:\n\
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n\
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n\
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n\
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n\
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud" >/root/.condarc \
#
# create conda py39 environment
#
&& /root/miniconda3/bin/conda create -n py39 python=3.9 -y \
#
# switch pip source to TUNA & update pip
#
&& /root/miniconda3/envs/py39/bin/pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
&& /root/miniconda3/envs/py39/bin/pip install pip -U \
#
# enable root access with ssh: replace line starts with '#PermitRootLogin' or 'PermitRootLogin'
#
&& sed -i '/^#*PermitRootLogin/cPermitRootLogin yes' /etc/ssh/sshd_config \
#
# set root password
#
&& echo "root:$ROOT_PASSWD" \
&& echo "root:$ROOT_PASSWD" | chpasswd \
#
# change ssh port & start ssh service when docker container starts
#
&& echo "#!/bin/bash\n\
sed -i \"s/Port 22/Port \$SSH_PORT/g\" /etc/ssh/sshd_config\n\
service ssh start\n\
/bin/bash" >./startup.sh \
&& chmod 777 ./startup.sh \
#
# add welcome tips
#
&& CONDA_VERSION=`/root/miniconda3/condabin/conda -V` \
&& CONDA_VERSION=${CONDA_VERSION#* } \
&& echo "\
printf '\\\n'\n\
printf '\\\033[0;34m'\n\
printf 'Welcome to ICTP-AP server\\\n'\n\
printf 'Please change the default root password in time\\\n'\n\
printf '\\\n'\n\
printf ' Conda:\\\t\\\tMiniconda v$CONDA_VERSION  use \`conda activate py39\` to activate conda env\\\n'\n\
printf ' SSH port:\\\t$SSH_PORT for this container\\\n'\n\
printf '\\\033[0m'\n\
printf '\\\n'\n\
" >>/etc/update-motd.d/10-help-text \
#
# cleanup
#
&& rm -rf /var/lib/apt/lists/* /tmp/*
#
# set startup script
#
ENTRYPOINT ./startup.sh
