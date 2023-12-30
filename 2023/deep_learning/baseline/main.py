##############################################################################################################
# 这部分代码主要是引入所需要的库
#
#
##############################################################################################################
import os
import numpy as np
from pathlib import Path
from data_prep_bbh import *
from utils import *

import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch import nn

##############################################################################################################
# 这部分代码主要是定义数据生成器
#
#
##############################################################################################################


class DatasetGenerator(Dataset):
    def __init__(self, fs=8192, T=1, snr=20,
                 detectors=['H1', 'L1'],
                 nsample_perepoch=100,
                 Nnoise=25, mdist='metric',beta=[0.75,0.95],
                 verbose=True):
        # 初始化函数，设置各种参数
        if verbose:
            print('GPU available?', torch.cuda.is_available())
        self.fs = fs     # the sampling frequency (Hz)
        self.T = T       # the observation duration (sec)

        safe = 2         # define the safe multiplication scale for the desired time length
        self.T *= safe

        self.detectors = detectors
        self.snr = snr
        
        self.generate(nsample_perepoch, Nnoise, mdist, beta)  # pre-generate sampels

    def generate(self, Nblock, Nnoise=25, mdist='metric',beta=[0.75,0.95]):
        # 生成数据的函数
        # Nnoise: # the number of noise realisations per signal
        # Nblock: # the number of training samples per output file
        # mdist:  # mass distribution (astro,gh,metric)

        ts, par = sim_data(self.fs, self.T, self.snr, self.detectors, Nnoise, size=Nblock, mdist=mdist,
                           beta=beta, verbose=False)
        self.strains = np.expand_dims(ts[0], 1)   # (nsample, 1, len(det), fs*T)
        self.labels = ts[1]

    def __len__(self):
        # 返回数据的长度
        return len(self.strains)

    def __getitem__(self, idx):
        # 获取数据的函数
        return self.strains[idx], self.labels[idx]


##############################################################################################################
# 这部分代码主要是定义网络结构，以及加载和保存模型的函数
#
#
##############################################################################################################

# 在模型定义中，我们定义了一个卷积神经网络，包含了多个卷积层、激活函数、批量归一化层和最大池化层。
# 最后，我们添加了一个Flatten层和两个全连接层。

class MyNet(nn.Module):
    def __init__(self):
        # 初始化函数，设置网络的各种参数
        super(MyNet, self).__init__()

        Nfilters = [8, 16, 16, 32, 64, 64, 128, 128]
        filter_size = [(1, 32)] + [(1, 16)] * 3 + [(1, 8)] * 2 + [(1, 4)] * 2
        filter_stride = [(1, 1)] * 8
        dilation = [(1, 1)] * 8
        pooling = [1, 0, 0, 0, 1, 0, 0, 1]
        pool_size = [[1, 8]] + [(1, 1)] * 3 + [[1, 6]] + [(1, 1)] * 2 + [[1, 4]]
        pool_stride = [[1, 8]] + [(1, 1)] * 3 + [[1, 6]] + [(1, 1)] * 2 + [[1, 4]]

        self.layers = nn.ModuleList()

        for i in range(8):
            # 添加卷积层
            self.layers.append(nn.Conv2d(
                in_channels=1 if i == 0 else Nfilters[i-1],  # Number of channels in the input image
                out_channels=Nfilters[i],  # Number of channels produced by the convolution
                kernel_size=filter_size[i],  # Size of the convolving kernel
                stride=filter_stride[i],  # Stride of the convolution
                padding=0,  # Zero-padding added to both sides of the input
                dilation=dilation[i],  # Spacing between kernel elements
                groups=1,  # Number of blocked connections from input channels to output channels
                bias=True,  # If True, adds a learnable bias to the output
                padding_mode='zeros',  # Specifies the type of padding, 'zeros' pads with zero
            ))
            # 添加ELU激活函数，alpha参数为0.01
            self.layers.append(nn.ELU(0.01))
            # 添加批量归一化层，特征数量为Nfilters[i]
            self.layers.append(nn.BatchNorm2d(num_features=Nfilters[i]))
            # 如果pooling[i]为真，添加最大池化层
            if pooling[i]:
                # 最大池化层的参数：核大小为pool_size[i]，步长为pool_stride[i]，填充为0
                self.layers.append(nn.MaxPool2d(
                    kernel_size=pool_size[i],
                    stride=pool_stride[i],
                    padding=0,
                ))

        # 添加Flatten层，将输入展平
        self.layers.append(nn.Flatten())
        # 添加全连接层，输入维度为20224，输出维度为64
        self.layers.append(nn.Linear(20224, 64))
        # 添加ELU激活函数，alpha参数为0.01
        self.layers.append(nn.ELU(0.01))
        # 添加Dropout层，丢弃率为0.5
        self.layers.append(nn.Dropout(0.5))
        # 添加全连接层，输入维度为64，输出维度为2
        self.layers.append(nn.Linear(64, 2))

    def forward(self, x):
        # 前向传播函数
        for layer in self.layers:
            x = layer(x)
        return x

    
# 在模型保存和加载函数中，我们保存了模型的参数、优化器的状态、学习率调度器的状态和训练的epoch。
# 在加载模型时，我们加载了模型的参数，并返回了模型、训练的epoch和训练损失历史。


def load_model(checkpoint_dir=None):
    # 加载模型的函数
    net = MyNet()

    if (checkpoint_dir is not None) and (Path(checkpoint_dir).is_dir()):
        p = Path(checkpoint_dir)
        files = [f for f in os.listdir(p) if '.pt' in f]

        # if there is a *.pt model file, load it!
        if (files != []) and (len(files) == 1):
            checkpoint = torch.load(p / files[0])
            net.load_state_dict(checkpoint['model_state_dict'])
        print('Load network from', p / files[0])
        
        epoch = checkpoint['epoch']
        train_loss_history = np.load(p / 'train_loss_history_cnn.npy').tolist()
        return net, epoch, train_loss_history
    else:
        print('Init network!')
        return net, 0, []


def save_model(epoch, model, optimizer, scheduler, checkpoint_dir, train_loss_history, filename):
    """Save a model and optimizer to file.
    """
    # 保存模型的函数
    p = Path(checkpoint_dir)
    p.mkdir(parents=True, exist_ok=True)

    # clear all the *.pt
    assert '.pt' in filename
    for f in [f for f in os.listdir(p) if '.pt' in f]:
        os.remove(p / f)

    # Save loss history
    np.save(p / 'train_loss_history_cnn', train_loss_history)

    output = {
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'epoch': epoch,
    }

    if scheduler is not None:
        output['scheduler_state_dict'] = scheduler.state_dict()
    # save the model
    torch.save(output, p / filename)


##############################################################################################################
# 这部分代码主要是定义训练和评估函数
#
#
##############################################################################################################

numpy = lambda x, *args, **kwargs: x.detach().numpy(*args, **kwargs)
size = lambda x, *args, **kwargs: x.numel(*args, **kwargs)
reshape = lambda x, *args, **kwargs: x.reshape(*args, **kwargs)
to = lambda x, *args, **kwargs: x.to(*args, **kwargs)
reduce_sum = lambda x, *args, **kwargs: x.sum(*args, **kwargs)
argmax = lambda x, *args, **kwargs: x.argmax(*args, **kwargs)
astype = lambda x, *args, **kwargs: x.type(*args, **kwargs)
transpose = lambda x, *args, **kwargs: x.t(*args, **kwargs)


def accuracy(y_hat, y):
    """Compute the number of correct predictions."""
    # 计算预测正确的数量
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = argmax(y_hat, dim=1)        
    cmp = astype(y_hat, y.dtype) == y
    return float(reduce_sum(astype(cmp, y.dtype)))


def evaluate_accuracy_gpu(net, data_iter, loss_func, device=None): #@save
    """使用GPU计算模型在数据集上的精度"""
    if isinstance(net, nn.Module):
        net.eval()  # 设置为评估模式
        if not device:
            device = next(iter(net.parameters())).device
    # 正确预测的数量，总预测的数量, test_loss
    metric = Accumulator(3)
    with torch.no_grad():
        for X, y in data_iter:
            X = X.to(device).to(torch.float)
            y = y.to(device).to(torch.long)
            y_hat = net(X)
            loss = loss_func(y_hat, y)
            metric.add(accuracy(y_hat, y), y.numel(), loss.sum())
    return metric[0] / metric[1], metric[2] / metric[1]


# 在训练函数中，我们首先定义了损失函数、优化器和学习率调度器。
# 然后，我们开始训练循环，每个epoch我们都会生成新的训练样本，
# 然后通过网络进行前向传播，计算损失，然后进行反向传播和参数更新。
# 在每个epoch结束后，我们会在测试集上评估模型，并保存测试损失最小的模型。


def train(net, lr, nsample_perepoch, epoch, total_epochs,
          dataset_train, data_loader, test_iter,
          train_loss_history, checkpoint_dir, device, notebook=True):
    """训练函数"""
    # 设置优化器参数
    loss_func = nn.CrossEntropyLoss()  # 定义损失函数
    optimizer = torch.optim.Adam(net.parameters(), lr=lr)  # 定义优化器
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                        optimizer,
                        T_max=total_epochs,  # 定义学习率调度器
                    )

    torch.cuda.empty_cache()  # 清空CUDA缓存
    if notebook:
        animator = Animator(xlabel='epoch', xlim=[1, total_epochs],
                                legend=['train loss', 'test loss', 'train acc', 'test acc'])  # 定义动画显示器
    timer, num_batches = Timer(), len(dataset_train)  # 定义计时器和批次数量

    # 开始训练循环
    for epoch in range(epoch, epoch + total_epochs):
        # 预生成训练样本
        dataset_train.generate(nsample_perepoch)

        # 如果不是notebook模式，打印当前学习率
        if not notebook:
            print('Learning rate: {}'.format(
                        optimizer.state_dict()['param_groups'][0]['lr']))

        # 初始化度量累加器，用于计算训练损失总和，训练准确率总和，样本数
        metric = Accumulator(3)

        # 设置网络为训练模式
        net.train()
        # 遍历数据加载器中的所有批次
        for batch_idx, (x, y) in enumerate(data_loader):
            # 开始计时
            timer.start()
            # 清零优化器的梯度 (1/4)
            optimizer.zero_grad()

            # 将数据和标签转移到设备上，并转换为适当的数据类型
            data = x.to(device, non_blocking=True).to(torch.float)
            label = y.to(device, non_blocking=True).to(torch.long)

            # 通过网络进行前向传播，得到预测结果
            pred = net(data)
            # 计算损失
            loss = loss_func(pred, label)

            # 在不需要计算梯度的情况下执行以下操作
            with torch.no_grad():
                # 更新度量累加器
                metric.add(loss.sum(), accuracy(pred, label), x.shape[0])
            # 停止计时
            timer.stop()

            # 反向传播计算梯度 (2/4)
            loss.backward()
            # 使用优化器更新网络参数 (3/4)
            optimizer.step()

            # 计算训练损失和训练准确率
            train_l = metric[0] / metric[2]
            train_acc = metric[1] / metric[2]
            # 如果是notebook模式，并且当前批次是整个训练集的1/5或最后一个批次，更新动画显示器
            if notebook and (batch_idx + 1) % (num_batches // 5) == 0 or batch_idx == num_batches - 1:
                animator.add(epoch + (batch_idx + 1) / num_batches,
                             (train_l, None, train_acc, None))

        # 使用学习率调度器更新学习率 (4/4)
        scheduler.step()

        # 在测试集上评估模型
        test_acc, test_l = evaluate_accuracy_gpu(net, test_iter, loss_func, device)

        # 保存训练损失历史
        train_loss_history.append([epoch+1, train_l, test_l, train_acc, test_acc])

        # 如果是notebook模式，更新动画显示器；否则，打印训练损失、测试损失、训练准确率和测试准确率
        if notebook:
            animator.add(epoch + 1, (train_l, test_l, train_acc, test_acc))
        else:
            print(f'Epoch: {epoch+1} \t'
                  f'Train Loss: {train_l:.4f} Test Loss: {test_l:.4f} \t'
                  f'Train Acc: {train_acc} Test Acc: {test_acc}')

        # 如果当前测试损失小于或等于历史最低测试损失，保存模型
        if (test_l <= min(np.asarray(train_loss_history)[:,1])):
            save_model(epoch, net, optimizer, scheduler, 
                       checkpoint_dir=checkpoint_dir,
                       train_loss_history=train_loss_history,
                       filename=f'model_e{epoch}.pt',)

    # 打印最终的训练损失、训练准确率和测试准确率
    print(f'loss {train_l:.4f}, train acc {train_acc:.3f}, '
          f'test acc {test_acc:.3f}')
    # 打印每秒处理的样本数和使用的设备
    print(f'{metric[2] * total_epochs / timer.sum():.1f} examples/sec '
          f'on {str(device)}')


if __name__ == "__main__":
    # 主函数，程序的入口
    nsample_perepoch = 100  # 每个epoch的样本数
    dataset_train = DatasetGenerator(snr=20, nsample_perepoch=nsample_perepoch)  # 训练数据集
    dataset_test = DatasetGenerator(snr=20, nsample_perepoch=nsample_perepoch)  # 测试数据集

    # 创建一个DataLoader
    data_loader = DataLoader(dataset_train, batch_size=32, shuffle=True,)  # 训练数据加载器
    test_iter = DataLoader(dataset_test, batch_size=32, shuffle=True,)  # 测试数据加载器

    device = torch.device('cuda')  # 使用CUDA设备

    # 模型和损失历史的输出路径
    checkpoint_dir = './checkpoints_cnn1/'

    # 创建模型    
    net, epoch, train_loss_history = load_model(checkpoint_dir)  # 加载模型
    net.to(device);  # 将模型转移到设备上

    # 优化器参数
    lr = 0.003  # 学习率
    total_epochs = 100  # 总的训练轮数
    total_epochs += epoch  # 加上已经训练过的轮数
    output_freq = 1  # 输出频率

    train(net, lr, nsample_perepoch, epoch, total_epochs, data_loader, test_iter, notebook=False)  # 训练模型```
