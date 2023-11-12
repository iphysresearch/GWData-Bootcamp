

# 第 1 部分 编程开发环境与工作流


- 日期：2023-11-12
- Video：[https://meeting.tencent.com/v2/cloud-record/share?id=af256140-e032-4b0c-9116-5741fad5010b&from=3](https://meeting.tencent.com/v2/cloud-record/share?id=af256140-e032-4b0c-9116-5741fad5010b&from=3)
- Slide: [https://slides.com/iphysresearch/gwda_coding_1](https://slides.com/iphysresearch/gwda_coding_1)

## Homework

- 基础作业：
  - 在自己的本地笔记本电脑/远程服务器上，用 Docker 容器创建 Python / Jupyter 开发环境。
  - 自行安装好 VS Code 后，用 SSH remote 扩展远程连接自己创建好的 Docker 容器。
- 扩展作业：
  - 在自己本地/远程服务器上，用 Docker 容器创建支持 GPUs 的 Python / Jupyter 开发环境（需要有GPU卡）
  - 创建 LALsuite / LISAcode 的源码编译好的容器镜像
 
- Hints:
  - https://hub.docker.com/r/nvidia/cuda
  - https://github.com/NVIDIA/nvidia-container-toolkit
  - https://git.ligo.org/lscsoft/lalsuite
  - https://hub.docker.com/r/igwn/lalsuite-dev
  - https://hub.docker.com/repository/docker/iphysresearch/lal_bilby
  - https://lisa-ldc.lal.in2p3.fr/
