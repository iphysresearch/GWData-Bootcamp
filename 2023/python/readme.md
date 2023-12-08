

# 第 2 部分 基于 Python 的数据分析基础


## 2023-11-29
- Video: [https://meeting.tencent.com/v2/cloud-record/share?id=38d62612-d754-413f-b6a9-2d0d960f4549&from=3](https://meeting.tencent.com/v2/cloud-record/share?id=38d62612-d754-413f-b6a9-2d0d960f4549&from=3)
- Slide: [PDF](./slide_python.pdf) or [https://slides.com/iphysresearch/gwda_coding_2_python](https://slides.com/iphysresearch/gwda_coding_2_python)
- Notebooks:
  - Jupyter Tutorial: [ipynb](./0-jupyter.ipynb) or [html](./0-jupyter.html)
  - Python Tutorial: [ipynb](./1-python.ipynb) or [html](./1-python.html)
- Extra Bonus: See [Python 补充学习资料包](./Python补充学习资料包)
  - 【入门】简明Python教程.pdf
  - 【进阶】利用Python进行数据分析.pdf
  - 【进阶】Python for Data Analysis, 2nd Edition.pdf
  - 【高阶】深入理解Python中文版(Dive into Python).pdf
  - 【官方文档】Python_tutorial.pdf

## 2023-12-01
- Video: [https://meeting.tencent.com/v2/cloud-record/share?id=0e5f06cb-8c5b-4e28-a1ba-a766025510e4&from=3](https://meeting.tencent.com/v2/cloud-record/share?id=0e5f06cb-8c5b-4e28-a1ba-a766025510e4&from=3)
- Slide: [PDF](./slide_numpy.pdf) or [https://slides.com/iphysresearch/gwda_coding_2_numpy](https://slides.com/iphysresearch/gwda_coding_2_numpy)
- Notebooks:
  - Numpy Tutorial: [ipynb](./2-numpy.ipynb) or [html](./2-numpy.html)

## 2023-12-03
- Video: [https://meeting.tencent.com/v2/cloud-record/share?id=eef300fb-a794-4aff-93e2-0ec36501b1b6&from=3](https://meeting.tencent.com/v2/cloud-record/share?id=eef300fb-a794-4aff-93e2-0ec36501b1b6&from=3)
- Slide: [PDF](./slide_pandas.pdf) or [https://slides.com/iphysresearch/gwda_coding_2_pandas](https://slides.com/iphysresearch/gwda_coding_2_pandas)
- Notebooks:
  - Pandas Tutorial: [ipynb](./3-pandas.ipynb) or [html](./3-pandas.html)
  - GW Catalog 数据分析案例: [ipynb](./3-pandas-GW_Catalog.ipynb)
  - 股票数据分析案例: [ipynb](./3-pandas-Finance.ipynb)



## Homework

### 基础作业

1. Python、Numpy 和 Pandas 的**基础作业**题目（单选题）位于：
  ```text
   2023/python/homework-python.*
   2023/python/homework-numpy.*
   2023/python/homework-pandas.*
  ```
（分别有 ipynb, html, md 三种文档格式，以方便阅读）

2. 将你完成的作业添加到你在上一步中创建的个人作业目录中。根据作业的类型，应将完成的作业分别命名为 `python_submit.txt`、`numpy_submit.txt` 和 `pandas_submit.txt`。其中每个 txt 文档的每行对应于 A,B,C,D,... 等选项当中的一个（注意：行号对应于题号）
3. 在 `homework` 分支上把你完成的作业 push 到你自己的关于本课程的远程仓库中，即：`$ git push origin homework` ；最后，在GitHub上你的远程仓库中，在 `homework` 分支下发起 Pull Request (PR) 至本课程远程仓库的 `homework` 分支。 
4. GitHub Actions 工作流将自动检查你的提交和计算成绩，即将 modified 的 `python_submit.txt`、`numpy_submit.txt` 和 `pandas_submit.txt` 与 solution 进行比较。
5. 基础作业的最终成绩，根据PR的最新 commit 来定，记得到时候 @ 我记录成绩。
6. 不要修改其他学员的作业目录和作业内容！

### 扩展作业

1. 完成以下 [Leetcode](https://leetcode.com/) 中的算法题目：
- [434. Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) (初级)
- [1869. Longer Contiguous Segments of Ones than Zeros](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/) (初级)
- [1784. Check if Binary String Has at Most One Segment of Ones](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/) (初级)
- [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/) (中级)
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/description/) (中级)
2. 把上面5道算法题目的结果 comment 在你完成的基础作业的PR里，要求：**算法的每一行都写好中文说明注释**。
3. Want more? see: [Advent of Code](https://adventofcode.com/)
