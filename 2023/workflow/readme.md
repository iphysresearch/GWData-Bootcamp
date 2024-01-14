

# 第 1 部分 编程开发环境与工作流


## 2023-11-12
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=538620703&bvid=BV1xi4y1B7GS](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=538620703&bvid=BV1xi4y1B7GS)
- Slide: [PDF](./slide.pdf) or [https://slides.com/iphysresearch/gwda_coding_1](https://slides.com/iphysresearch/gwda_coding_1)

### Homework

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

## 2023-11-19
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=966071321&bvid=BV1JW4y1A7AY](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=966071321&bvid=BV1JW4y1A7AY)
- Slide: [PDF](./slide_git.pdf) or [https://slides.com/iphysresearch/gwda_coding_1_git](https://slides.com/iphysresearch/gwda_coding_1_git)

### Homework

1. 自己创建一个 GitHub 账户，fork 本课程的远程仓库（注意不要勾选 copy `main` branch only）后再 clone 到本地：
  ```shell
  git clone git@github.com:<你的github账户名>/GWData-Bootcamp.git
  ```
2. 未来的编程作业将仅在 `homework` 分支上完成。你需要在你的本地仓库中新建目录 `/GWData-Bootcamp/2023/homework/<你的名字>/`；并最终把 `homework` 分支的作业 push 到你自己的关于本课程的远程仓库中，即：
  ```shell
  $ git push origin homework
  ```
  最后，在GitHub上你的远程仓库中，在 `homework` 分支下发起 **Pull Request** (PR) 至本课程远程仓库。
3. 不要修改其他学员的作业目录和作业内容！
