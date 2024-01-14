

# 第 2 部分 基于 Python 的数据分析基础


## 2023-11-29
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=878535052&bvid=BV1VN4y1v7JR](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=878535052&bvid=BV1VN4y1v7JR)
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

---

## 2023-12-01
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=538693977&bvid=BV1Bi4y1B7VP](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=538693977&bvid=BV1Bi4y1B7VP)
- Slide: [PDF](./slide_numpy.pdf) or [https://slides.com/iphysresearch/gwda_coding_2_numpy](https://slides.com/iphysresearch/gwda_coding_2_numpy)
- Notebooks:
  - Numpy Tutorial: [ipynb](./2-numpy.ipynb) or [html](./2-numpy.html)

---

## 2023-12-03
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=836210064&bvid=BV1Cg4y1S79t](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=836210064&bvid=BV1Cg4y1S79t)
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

---

## 2023-12-08
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=411155780&bvid=BV1NV411R7Gt](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=411155780&bvid=BV1NV411R7Gt)
- Slide: [PDF](./slide_visualization.pdf) or [https://slides.com/iphysresearch/gwda_coding_2_visualization](https://slides.com/iphysresearch/gwda_coding_2_visualization)
- Notebooks:
  - Matplotlib Tutorial: [ipynb](./4-matplotlib.ipynb) or [html](./4-matplotlib.html)
- Extra Bonus: Click [Visualization analysis and design by Tamara Munzner (z-lib.org).pdf](https://paul.zhdk.ch/pluginfile.php/93332/mod_resource/content/2/Visualization%20analysis%20and%20design%20by%20Tamara%20Munzner%20%28z-lib.org%29.pdf) link to view the file.

## 2023-12-10
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=238683269&bvid=BV1Ze41127Yz](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=238683269&bvid=BV1Ze41127Yz)
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=241157282&bvid=BV17e411v7vc](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=241157282&bvid=BV17e411v7vc)
- Notebooks:
  - Matplotlib Tutorial: [ipynb](./4-matplotlib.ipynb) or [html](./4-matplotlib.html)
  - Seaborn Tutorial: [ipynb](./4-seaborn.ipynb) or [html](./4-seaborn.html)
  - Reproduce Figure 7 from the GWTC-3 paper Tutorial: [ipynb](./4-GWTC3.ipynb) or [html](./4-GWTC.html)
- Extra Bonus: [Matplotlib styles for scientific plotting](https://github.com/garrettj403/SciencePlots)
- Extra Bonus: [Cheatsheets for Matplotlib users](https://github.com/matplotlib/cheatsheets)
- Note: 2023-12-10 忘了录屏了。。。。感谢杨铭森同学的贡献！


## Homework

- 航班乘客变化分析 (2个题)​​​​​
- 鸢尾花花型尺寸分析 (3个题)
- 餐厅小费情况分析 (7个题)
- 泰坦尼克号海难幸存状况分析 (8个题)

### 基础作业

- 数据可视化作业题目位于 [homework-matplotlib_seaborn.ipynb](./homework-matplotlib_seaborn.ipynb)，用 matplotlib 或 seaborn 完成题目后，把该 notebook 提交到学员自己的作业目录中，最后 PR 即可。

### 拓展作业

- 分别用 matplotlib 和 seaborn 完成基础作业。

---

## 2023-12-15
- Content:

      - LIGO Open Data
      - FFT by scratch
      - Spectral Analysis
      - Data analysis on GW150914
      - Matched filtering to find the signal
- Video: [https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=496155740&bvid=BV1DK411v79y](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=496155740&bvid=BV1DK411v79y)
- Notebooks:
  - Tutorial: [ipynb](./5-GW150914.ipynb) or [html](./5-GW150914.html)



