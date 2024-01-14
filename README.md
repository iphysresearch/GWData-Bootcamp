# 引力波数据探索：编程与分析实战训练营
# Gravitational Wave Data Exploration: A Practical Training in Programming and Analysis

> The course recordings are now available on [Bilibili](​https://space.bilibili.com/76060243/channel/seriesdetail?sid=3896245). <a href="https://space.bilibili.com/76060243/channel/seriesdetail?sid=3896245"><img src="https://f.fameile.net/upload/2022/05/Rogchu.png"  width="30" /></a>

Welcome to the GitHub repository for the Gravitational Wave Data Exploration Bootcamp Series! 
This course is meticulously designed to provide a solid foundation in programming, operational knowledge, and data-driven modeling skills centered around gravitational wave data analysis and research.

<img src="logo-taiji.jpg" style="width:20%;height:auto;">

## Training Objectives
- Equip participants with robust programming and operational skills, and foundational training in data-driven modeling, focusing on gravitational wave data analysis and related research areas.
- **Note: The course is conducted entirely in Mandarin Chinese to cater to a wide range of Chinese-speaking students and researchers.**
- Discuss the common research methodologies combining gravitational wave data processing with AI technologies, with hands-on examples and projects for practical understanding and mastery.
- Analyze cutting-edge deep learning models and apply them to real-world gravitational wave data analysis problems through specific case studies.

## Target Audience
- Undergraduate and graduate students interested in data analysis and algorithm development, especially those focusing on gravitational wave data processing and related research.
- The course also welcomes undergraduates with a basic programming background, looking to enhance their data analysis skills or with an interest in gravitational wave data processing.
- Future professionals aspiring to work in space-based gravitational wave detection projects and related research fields.

## Course Design Philosophy
- Drawing from past teaching experiences and identified knowledge gaps in student research projects, the course introduces relevant concepts and common methods to ensure comprehensive understanding and application in research.
- The course is scheduled weekly or bi-weekly, each session lasting about 3 hours, combining online and offline methods (腾讯会议) to ensure interactivity and practicality.
- The curriculum is expected to be offered once per semester or annually, with continual updates and enrichment based on student feedback and research demands.

## Course Outline / Schedule
- **Part Zero**: _Motivational Introduction_

    <details>
    <summary>Description</summary>

      - 办课初衷与学员构成
      - 讲师介绍
      - 与本课程相关的知识架构
          - 引力波数据分析
          - 课程大纲
          - 本课程是什么，不是什么
      - 本课程的学习方法与教学团队
      - 本课程的考核规则和项目作业
      - 通向自我实现之路
          - 如何自学
          - 如何提问
      - 提问环节

    </details>

  - Date：[2023/11/08](2023/intro/readme.md) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=793550130&bvid=BV1sC4y1Y7CN) | Slide: [PDF](2023/intro/slide.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_0)
- **Part One**: _Programming Development Environment and Workflow_
    <details>
    <summary>Description</summary>
  
      - Linux Commands and Shell Scripting
      - Git Version Control (GitHub / GitLab)
      - SSH Remote Server Access (Shell / VSCode)
      - Containerization with Docker
      - Hands-On: Setting up Python / Jupyter Development Environment
      - Hands-On: Compiling LALsuite / LISAcode Source Code

    </details>

  - Date：[2023/11/12](2023/workflow/readme.md#2023-11-12) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=538620703&bvid=BV1xi4y1B7GS) | Slide: [PDF](2023/workflow/slide.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_1)
  - [Homework](2023/workflow/readme.md#homework)
      - Docker Container Setup
      - Remote Development for Python/Jupyter with GPU Support and LALsuite/LISAcode Compilation
  - Date：[2023/11/19](2023/workflow/readme.md#2023-11-19) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=966071321&bvid=BV1JW4y1A7AY) | Slide: [PDF](2023/workflow/slide_git.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_1_git)
  - [Homework](2023/workflow/readme.md#homework-1)
      - Introduction to Git and GitHub Workflow
      - Setting Up and Submitting Homework via GitHub
- **Tech Talk**: _It's all about data_ (Guest Lecture by [Xinyao Tian](https://www.zhihu.com/people/winchester-26/activities))
    <details>
    <summary>Description</summary>
  
      - 数据的起源 (The origin of data)
      - 何谓数据？ (What is data?)
      - 现代数据技术的发展脉络 (The development momentum behind data)
      - 当前主流数据技术 (Modern data technologies)
        - 关系型数据库 (RDBMS)
        - 非关系型数据库 (Not-only SQL (NoSQL) Database)
        - 大数据 (Big Data)
        - 数据仓库 (Data Warehouse)
        - 流式计算 (Stream Processing)
        - 数据湖 (Data Lake)
        - 数据湖仓 (Data Lakehouse)
      - 思考：从数据的角度认识世界 (Thinking: Realizing the world from a data perspective)
      - 推荐阅读 (Recommend readings)
      - Q & A
  
    </details>

  - Date：[2023/11/19](2023/TechTalk1/readme.md) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=453718702&bvid=BV1R5411i73y) | Slide: [markdown](2023/TechTalk1/readme.md)
    
- **Part Two**: _Python-Based Data Analysis Fundamentals_
    <details>
    <summary>Description</summary>
  
      - Introduction to Python Programming
      - Algorithms with Numpy / Pandas / Scipy
      - Hands-On: Exploratory Data Analysis of GW Event Catalog / Glitch Data
      - Hands-On: Matched Filtering for GW150914 Data
      - Data Visualization in Python: Theory and Practice
      - Hands-On: Reproducing Figures from GWTC Papers

    </details>

  - Date：[2023/11/29](2023/python/readme.md#2023-11-29) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=878535052&bvid=BV1VN4y1v7JR) | Slide: [PDF](2023/python/slide_python.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_python)
  - Date：[2023/12/01](2023/python/readme.md#2023-12-01) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=538693977&bvid=BV1Bi4y1B7VP) | Slide: [PDF](2023/python/slide_numpy.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_numpy)
  - Date：[2023/12/03](2023/python/readme.md#2023-12-03) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=836210064&bvid=BV1Cg4y1S79t) | Slide: [PDF](2023/python/slide_pandas.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_pandas)
  - [Homework](2023/python/readme.md#homework)
      - Python, Numpy, Pandas Basic Homework
      - Leetcode Extension Tasks
  - Date：[2023/12/08](2023/python/readme.md#2023-12-08) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=411155780&bvid=BV1NV411R7Gt) | Slide: [PDF](2023/python/slide_visualization.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_visualization)
  - Date：[2023/12/10](2023/python/readme.md#2023-12-10) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=238683269&bvid=BV1Ze41127Yz)
  - [Homework](2023/python/readme.md#homework-1)
      - Data visualization and analysis using Python libraries, matplotlib and seaborn.
  - [Homework](2023/python/4-GWTC3.ipynb) | Vidwo [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=241157282&bvid=BV17e411v7vc)
      - Recreate Figure 7 from the GWTC-3 paper using numpy, pandas, matplotlib, and seaborn.
  - Date：[2023/12/15](2023/python/readme.md#2023-12-15) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=496155740&bvid=BV1DK411v79y) | [ipynb](2023/python/5-GW150914.ipynb) | [html](2023/python/5-GW150914.html)
      - LIGO Open Data + FFT by scratch + Spectral Analysis ([Project](2023/python/5-GW150914.ipynb))
      - Data analysis on GW150914 + Matched filtering to find the signal ([Project](2023/python/5-GW150914.ipynb))

- **Sci Talk**: _Bayesian inference for gravitational-wave science_ (Guest Lecture by [Junjie Zhao](https://orcid.org/0000-0002-9233-3683))
    <details>
    <summary>Description</summary>
  
        - Brief introduction to gravitational wave (引力波简要介绍)
        - Part I: Bayesian inference (贝叶斯推断)
            - Definition of “probability” ("概率"的定义)
            - Rethink the interpretations (重思概率诠释)
                - Frequentist statistics (频率学派)
                - Bayesian statistics (贝叶斯学派)
            - Bayes' theorem (贝叶斯定理)
                - Application to the detection of gravitational wave (在引力波探测上应用)
            - Bayesian inference framework (贝叶斯推断框架)
                - Parameter estimation for gravitational-wave data (引力波数据分析中参数估计)
                - Model selection for gravitational-wave data (引力波数据分析中模型选择)
        - Q & A
        - Part II: Bayesian computation (贝叶斯计算方法)
            - Markov Chain Monte Carlo (MCMC; 马尔可夫链-蒙特卡罗方法)
                - hands-on tiny mcmc example
            - Nested sampling (嵌套采样)
                - hands-on tiny nested-sampling example
        - Part III: All in gravitational-wave data (一切尽在引力波数据中)
            - Use Bilby & Parallel Bilby in the GW data analysis
            - nShow the complete pipeline for the data analysis
        - The AMAZING Thomas Bayes (为美好的世界献上"贝叶斯定理")
        - Q & A
  
    </details>

  - Date：[2023/12/16](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/README.md) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=751201677&bvid=BV1Yk4y1Q74Q) | Slide: [PDF](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/Junjie%20-%202023%20-%20bayesian%20for%20GWData-Bootcamp.pdf)
  - Date：[2023/12/17](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/README.md) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=496196569&bvid=BV19K411v7Sv) | Slide: [PDF](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/Junjie%20-%202023%20-%20bayesian%20for%20GWData-Bootcamp.pdf)


- **Part Three**: _Basics of Machine Learning_
    <details>
    <summary>Description</summary>
  
      - Overview of Artificial Intelligence
      - Definitions, Objectives, and Types of Machine Learning
      - Machine Learning Project Development and Preparation
      - Hands-On: Clustering Analysis of LIGO's Glitch Data

    </details>

  - Date：[2023/12/22](2023/machine_learning/readme.md#2023-12-22) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=538650039&bvid=BV1ei4y1B7Lg) | Slide: [PDF](2023/machine_learning/slide_ml_1.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_3_intro)
  - [Homework](2023/machine_learning/readme.md#homework)
      - Implement a classification model for credit scoring using the sklearn library in Python.
  - Date：[2023/12/24](2023/machine_learning/readme.md#2023-12-24) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=881213209&bvid=BV14K4y1z72Z) | Slide: [PDF](2023/machine_learning/slide_ml_2.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_3_adv)
      - Use GravitySpy Glitch metadata to build and train a classification model. ([Project](2023/machine_learning/sklearn_gravityspy_glitch_classification.ipynb))
      - Train a clustering model using the time-frequency image information from GravitySpy Glitch. ([Project](2023/machine_learning/sklearn_gravityspy_glitch_cluster_analysis.ipynb))
  - [Homework](2023/machine_learning/readme.md#homework-2)
      - Model Evaluation and Hyperparameter Tuning for a Credit Scoring Dataset.

- **Part Four**: _Introduction to Deep Learning_
    <details>
    <summary>Description</summary>
    
      - Overview of Deep Learning Technologies
      - Fundamentals of Artificial Neural Networks (ANN)
      - Convolutional Neural Networks (CNN)
      - Hands-On: Identifying Gravitational Waves from Binary Black Hole Systems using CNN
      - Frontiers of Gravitational Wave Data Analysis and AI

    </details>

  - Date：[2023/12/27](2023/deep_learning/readme.md#2023-12-27) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=878713271&bvid=BV1DN4y1H7ep) | Slide: [PDF](https://pan.baidu.com/s/1kX8KbQMiMMOubyTwiqTdXQ?pwd=audc) or [online](https://slides.com/iphysresearch/gwda_coding_4_ann)
  - Date：[2023/12/29](2023/deep_learning/readme.md#2023-12-29) | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=238749156&bvid=BV1Ee411m7Kt) | Slide: [PDF](https://pan.baidu.com/s/1nwaAbHIl1Ed7JATm3tGxlw?pwd=6h69) or [online](https://slides.com/iphysresearch/gwda_coding_4_cnn)

- **Tech Talk**: _AI Revolution: From Concept to GPT Breakthroughs_ (Guest Lecture by [Minquan Gao](https://www.mqgao.com/))
    <details>
    <summary>Description</summary>
  
        1. Why AI Was Proposed:
            - Exploring the historical context and reasoning behind the emergence of AI.
            - Initial challenges and needs that AI aimed to address.
        2. Earliest Form of AI and Solutions:
            - Description of the first AI systems, such as simple computational machines.
            - Early AI applications and the problems they solved.
        3. Similarities between AI and Physics Methodologies:
            - Comparing the theoretical frameworks and approaches used in both fields.
            - Identifying shared principles and methods.
        4. From Symbolic Systems to Machine Learning:
            - Evolution of AI from early symbolic and numeric systems.
            - The transition to probabilistic and statistical methods.
            - The development of machine learning technologies.
        5. Principles of Deep Learning:
            - Understanding the core concepts behind deep learning.
            - The architecture of neural networks and their functionality.
        6. Breakthroughs Brought by Deep Learning:
            - Identifying key advancements and innovations due to deep learning.
            - Impact of deep learning on various AI applications.
        7. Typical Deep Learning Scenarios:
            - Examples of deep learning applications in real-world scenarios.
            - Discussion of its effectiveness and adaptability.
        8. Pre-trained Models and Large Models:
            - The role and significance of pre-trained models in AI.
            - Characteristics and implications of large-scale AI models.
        9. Principles of GPT:
            - Explaining the foundational concepts of Generative Pre-trained Transformers.
            - Discussing its applications and impact.
        10. Breakthroughs in AIGC (AI Generated Content):
            - Overview of advancements in AI-generated content.
            - Examples and implications of these breakthroughs.
        11. Current Challenges in AI:
            - Discussing ethical, technical, and practical problems in AI.
            - Examination of ongoing debates and concerns in the field.
        12. Frontiers of AI Research:
            - Exploring cutting-edge research and future directions in AI.
            - Innovations and potential developments on the horizon.

    </details>

  - Date：[2023/12/31]() | Video [recording](https://www.bilibili.com/list/76060243?sid=3896245&spm_id_from=333.999.0.0&desc=1&oid=836130181&bvid=BV1gg4y1S7Bn)

- **Final Part**: _End-of-Camp Ceremony and Wrap-Up_
    <details>
    <summary>Description</summary>

        - Acknowledgements
        - Training Camp Course Review and Summary
        - Homework Completion & Competition Rankings
        - Awards Ceremony
        - Video Recording Sharing + Bilibili Channel Launch + Remember to Star the Course
        - Welcoming More Feedback and Suggestions

    </details>

  - Date：[2024/01/14](2023/gwda_coding.pdf) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=b393c27f-63ff-434a-9d65-a78a48af0431&from=3) | Slide: [PDF](2023/gwda_coding.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_5)


## Kaggle Data Science Competition (Hackathon)

<div class="sl-block is-focused" data-block-type="image" data-name="image-76f7c0" style="width: 702.595px; height: 116.909px; left: 103.5px; top: 243.091px; min-width: 1px; min-height: 1px;" data-origin-id="41987a0e08687243a9014a91eff94fb7"><div class="sl-block-content" style="z-index: 17;"><img class="" data-natural-width="1232" data-natural-height="205" data-lazy-loaded="" src="https://s3.amazonaws.com/media-p.slid.es/uploads/1094055/images/11024519/pasted-from-clipboard.png"></div></div>

> Homepage: [https://www.kaggle.com/competitions/2023-gwdata-bootcamp/](https://www.kaggle.com/competitions/2023-gwdata-bootcamp/)

### Overview

- Welcome to the final challenge of the [Gravitational Wave Data Exploration: A Practical Training in Programming and Analysis (2023)](https://github.com/iphysresearch/GWData-Bootcamp/) - "**Can you find the GW signals?**" Kaggle Data Science Competition (Hackathon)! 
- This competition is designed to apply the knowledge and skills you've learned throughout the course, focusing on gravitational wave data analysis and research.

### Objective

- The objective of this competition is to develop a model that can accurately identify gravitational wave signals from the provided dataset. 
- You will be given a dataset containing a mix of noise and gravitational wave signals. Your task is to develop a model that can accurately distinguish between the two.

### Timeline

- This competition will start at 10:00 PM (Beijing Time) on December 29, 2023, and end at 11:59 PM (Beijing Time) on January 6, 2024.
- Please make sure to submit your solutions before the deadline.

- Good luck and may the best team win!

### Files

- [data_prep_bbh.py](2023/deep_learning/baseline/data_prep_bbh.py) - script for data generation (credit: [Dr. Hunter Gabbard](https://github.com/hagabbar/cnn_matchfiltering/))
- [utils.py](2023/deep_learning/baseline/utils.py) - supplemental script containing some useful functions
- [main.py](2023/deep_learning/baseline/main.py) - main script for training / evaluation / submission
- [test.npy](https://www.kaggle.com/competitions/2023-gwdata-bootcamp/data?select=test.npy) - test data for submission (You can load the test data in the [Kaggle notebook](https://www.kaggle.com/code/herbwang/baseline-kaggle))

> Anyway, just check the [baseline notebook](2023/deep_learning/baseline/baseline_sugon.ipynb) for everything!

## Hall of Fame (龍虎榜)

### Homework

- You can view the complete assignment results from the assignments committed by students with a total score of 6 and 7."

| Total Score | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Frequency | 4 | 5 | 6 | 10 | 7 | 23 | 8 |
| Top Percentage Ranking | $100.00 $% | $93.65 $% | $85.71 $% | $76.19 $% | $60.32 $% | $49.21 $% | $12.70 $% |

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/user321102">
          <img src="https://avatars.githubusercontent.com/u/151484176?s=100" width="100px;" alt="高远坤"/>
          <br />
          <sub><b>高远坤</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=user321102" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Dustingyd">
          <img src="https://avatars.githubusercontent.com/u/93420760?s=100" width="100px;" alt="郭印达"/>
          <br />
          <sub><b>郭印达</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=Dustingyd" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Shoupan">
          <img src="https://avatars.githubusercontent.com/u/112869625?s=100" width="100px;" alt="刘守潘"/>
          <br />
          <sub><b>刘守潘</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=Shoupan" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/suiranruofeng">
          <img src="https://avatars.githubusercontent.com/u/41351023?s=100" width="100px;" alt="张徐蔚"/>
          <br />
          <sub><b>张徐蔚</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=suiranruofeng" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Tangfengjie">
          <img src="https://avatars.githubusercontent.com/u/69887831?s=100" width="100px;" alt="汤丰杰"/>
          <br />
          <sub><b>汤丰杰</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=Tangfengjie" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/suhongqwq">
          <img src="https://avatars.githubusercontent.com/u/100949104?s=100" width="100px;" alt="苏鸿"/>
          <br />
          <sub><b>苏鸿</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=suhongqwq" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/2385877035">
          <img src="https://avatars.githubusercontent.com/u/151613563?s=100" width="100px;" alt="李炳辰"/>
          <br />
          <sub><b>李炳辰</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=2385877035" title="Commit">✅️</a> 
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/haozhao2002">
          <img src="https://avatars.githubusercontent.com/u/152390558?s=100" width="100px;" alt="郝赵"/>
          <br />
          <sub><b>郝赵</b></sub>
        </a>
        <br />
        <a href="#" title="Score">7️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=haozhao2002" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/hzy24">
          <img src="https://avatars.githubusercontent.com/u/38902141?s=100" width="100px;" alt="黄震洋"/>
          <br />
          <sub><b>黄震洋</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=hzy24" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/JunFan0">
          <img src="https://avatars.githubusercontent.com/u/151725601?s=100" width="100px;" alt="范钧"/>
          <br />
          <sub><b>范钧</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=JunFan0" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/ZenghuiZou">
          <img src="https://avatars.githubusercontent.com/u/143919061?s=100" width="100px;" alt="邹增慧"/>
          <br />
          <sub><b>邹增慧</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=ZenghuiZou" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/SuperAmazingMeng">
          <img src="https://avatars.githubusercontent.com/u/150605858?s=100" width="100px;" alt="蒙晓锋"/>
          <br />
          <sub><b>蒙晓锋</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=SuperAmazingMeng" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Qinglsr">
          <img src="https://avatars.githubusercontent.com/u/102406423?s=100" width="100px;" alt="刘世睿"/>
          <br />
          <sub><b>刘世睿</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=Qinglsr" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/itpmds">
          <img src="https://avatars.githubusercontent.com/u/70871491?s=100" width="100px;" alt="孟德双"/>
          <br />
          <sub><b>孟德双</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=itpmds" title="Commit">✅️</a> 
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/LogicMoriaty">
          <img src="https://avatars.githubusercontent.com/u/107927455?s=100" width="100px;" alt="董玉豪"/>
          <br />
          <sub><b>董玉豪</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=LogicMoriaty" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Doubleking-1">
          <img src="https://avatars.githubusercontent.com/u/71910936?s=100" width="100px;" alt="王尊"/>
          <br />
          <sub><b>王尊</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=Doubleking-1" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/zhuyan39">
          <img src="https://avatars.githubusercontent.com/u/151644281?s=100" width="100px;" alt="薛亚东"/>
          <br />
          <sub><b>薛亚东</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=zhuyan39" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/GitLuckyRan">
          <img src="https://avatars.githubusercontent.com/u/124147251?s=100" width="100px;" alt="刘冉"/>
          <br />
          <sub><b>刘冉</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=GitLuckyRan" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/anjo233">
          <img src="https://avatars.githubusercontent.com/u/81004959?s=100" width="100px;" alt="单磊磊"/>
          <br />
          <sub><b>单磊磊</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=anjo233" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/zoujing23">
          <img src="https://avatars.githubusercontent.com/u/151840794?s=100" width="100px;" alt="邹靓"/>
          <br />
          <sub><b>邹靓</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=zoujing23" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/sophia-in-shao">
          <img src="https://avatars.githubusercontent.com/u/117913801?s=100" width="100px;" alt="沈萍"/>
          <br />
          <sub><b>沈萍</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=sophia-in-shao" title="Commit">✅️</a> 
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Minderheiten">
          <img src="https://avatars.githubusercontent.com/u/105500750?s=100" width="100px;" alt="韩佩佳"/>
          <br />
          <sub><b>韩佩佳</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=Minderheiten" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/fargoing">
          <img src="https://avatars.githubusercontent.com/u/9104667?s=100" width="100px;" alt="吉祥"/>
          <br />
          <sub><b>吉祥</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=fargoing" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/ymphys">
          <img src="https://avatars.githubusercontent.com/u/83771689?s=100" width="100px;" alt="张嘉宝"/>
          <br />
          <sub><b>张嘉宝</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=ymphys" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/luopeis">
          <img src="https://avatars.githubusercontent.com/u/128964528?s=100" width="100px;" alt="潘洋"/>
          <br />
          <sub><b>潘洋</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=luopeis" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/HibiscuitDeCJ">
          <img src="https://avatars.githubusercontent.com/u/151739208?s=100" width="100px;" alt="周子力"/>
          <br />
          <sub><b>周子力</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=HibiscuitDeCJ" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Dawn-19">
          <img src="https://avatars.githubusercontent.com/u/103760888?s=100" width="100px;" alt="邱智翀"/>
          <br />
          <sub><b>邱智翀</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=Dawn-19" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/orangetome">
          <img src="https://avatars.githubusercontent.com/u/118738066?s=100" width="100px;" alt="李倾城"/>
          <br />
          <sub><b>李倾城</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=orangetome" title="Commit">✅️</a> 
      </td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/JyusingHo">
          <img src="https://avatars.githubusercontent.com/u/151446121?s=100" width="100px;" alt="何禹成"/>
          <br />
          <sub><b>何禹成</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=JyusingHo" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/WTLleo">
          <img src="https://avatars.githubusercontent.com/u/90229213?s=100" width="100px;" alt="王天龙"/>
          <br />
          <sub><b>王天龙</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=WTLleo" title="Commit">✅️</a> 
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/ShadowLeaper">
          <img src="https://avatars.githubusercontent.com/u/152157382?s=100" width="100px;" alt="汪一凡"/>
          <br />
          <sub><b>汪一凡</b></sub>
        </a>
        <br />
        <a href="#" title="Score">6️⃣</a> 
        <a href="https://github.com/iphysresearch/GWData-Bootcamp/commits/homework?author=ShadowLeaper" title="Commit">✅️</a> 
      </td>
    </tr>
  </tbody>
</table>


### Leaderboard of Kaggle Competition

- https://www.kaggle.com/competitions/2023-gwdata-bootcamp/leaderboard


<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>Team</th>
      <th>Members</th>
      <th>Score</th>
      <th>Rank</th>
      <th>Team</th>
      <th>Members</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <!-- Row 1-2 -->
    <tr>
      <td>1</td>
      <td>XAO</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/hzy24">
          <sub><b>黄震洋</b></sub>
        </a> 
        <br />
        <a href="https://github.com/suiranruofeng">
          <sub><b>张徐蔚</b></sub>
        </a>
      </td>
      <td>0.86173</td>
      <td>16</td>
      <td>Yuanhao Zhang</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>张渊皞</b></sub>
      </td>
      <td>0.83317</td>
    </tr>
    <!-- Row 3-4 -->
    <tr>
      <td>2</td>
      <td>UCAS Li Jiahao</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://www.kaggle.com/ucaslijiahao">
          <sub><b>李嘉豪</b></sub>
        </a> 
      </td>
      <td>0.86160</td>
      <td>17</td>
      <td>B4rRY_G</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>郭意扬</b></sub>
        <br />
        <sub><b>赖景祺</b></sub>
      </td>
      <td>0.82729</td>
    </tr>
    <!-- Row 5-6 -->
    <tr>
      <td>3</td>
      <td>UCAS_212x2</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://www.kaggle.com/ucas212x2">
          <sub><b>刘洋毓</b></sub>
        </a> 
      </td>
      <td>0.86157</td>
      <td>18</td>
      <td>Shao dong zhao</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>赵少东</b></sub>
      </td>
      <td>0.82723</td>
    </tr>
    <!-- Row 7-8 -->
    <tr>
      <td>4</td>
      <td>sophiainshao</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/sophia-in-shao">
          <sub><b>沈萍</b></sub>
        </a> 
      </td>
      <td>0.86145</td>
      <td>19</td>
      <td>Sparkle79</td>
      <td align="center" valign="top" width="14.28%">
        <!-- Assuming no members or link available -->
      </td>
      <td>0.82595</td>
    </tr>
    <!-- Row 9-10 -->
    <tr>
      <td>5</td>
      <td>Haihao SHI</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://www.kaggle.com/shihaihao">
          <sub><b>史海浩</b></sub>
        </a> 
      </td>
      <td>0.85954</td>
      <td>20</td>
      <td>Shoupan Liu</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>刘守潘</b></sub>
      </td>
      <td>0.82526</td>
    </tr>
    <!-- Row 11-12 -->
    <tr>
      <td>6</td>
      <td>Yinda Guo</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/Dustingyd">
          <sub><b>郭印达</b></sub>
        </a>
      </td>
      <td>0.85832</td>
      <td>21</td>
      <td>Capoo Cat</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>孙文博</b></sub>
      </td>
      <td>0.82387</td>
    </tr>
    <!-- Row 13-14 -->
    <tr>
      <td>7</td>
      <td>deslenlir</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://www.kaggle.com/deslenlir">
          <sub><b>温怡蓉</b></sub>
        </a>
      </td>
      <td>0.85753</td>
      <td>22</td>
      <td>Tian_Jun</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>田军</b></sub>
      </td>
      <td>0.82204</td>
    </tr>
    <!-- Row 15-16 -->
    <tr>
      <td>8</td>
      <td>MengXiaofeng-UCAS</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/SuperAmazingMeng">
          <sub><b>蒙晓锋</b></sub>
        </a>
      </td>
      <td>0.85188</td>
      <td>23</td>
      <td>Zhao_Hao</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>郝赵</b></sub>
      </td>
      <td>0.82047</td>
    </tr>
    <!-- Row 17-18 -->
    <tr>
      <td>9</td>
      <td>1500！！！</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/GitLuckyRan">
          <sub><b>刘冉</b></sub>
        </a>
        <br />
        <a href="https://github.com/Qinglsr">
          <sub><b>刘世睿</b></sub>
        </a>
        <br />
        <a href="https://github.com/WTLleo">
          <sub><b>王天龙</b></sub>
        </a>
      </td>
      <td>0.84868</td>
      <td>24</td>
      <td>douking</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>王尊</b></sub>
      </td>
      <td>0.81871</td>
    </tr>
    <!-- Row 19-20 -->
    <tr>
      <td>10</td>
      <td>Qinglin Yan</td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://www.kaggle.com/wtl777">
          <sub><b>王霆澜</b></sub>
        </a>
        <br />
        <a href="https://www.kaggle.com/qinglinyan">
          <sub><b>闫庆琳</b></sub>
        </a>
      </td>
      <td>0.84530</td>
      <td>25</td>
      <td>JunFan</td>
      <td align="center" valign="top" width="14.28%">
        <sub><b>范钧</b></sub>
</td>
<td>0.8141</td>
</tr>
<!-- Remaining rows -->
<tr>
<td>11</td>
<td>Zhiqing Zhu</td>
<td align="center" valign="top" width="14.28%">
<sub><b>朱智清</b></sub>
</td>
<td>0.84527</td>
<td>26</td>
<td>Phi267</td>
<td align="center" valign="top" width="14.28%">
<sub><b>秦戈宇</b></sub>
</td>
<td>0.81304</td>
</tr>
<tr>
<td>12</td>
<td>knnbenn</td>
<td align="center" valign="top" width="14.28%">
<!-- Assuming no members or link available -->
</td>
<td>0.84023</td>
<td>27</td>
<td>tastonlyjust</td>
<td align="center" valign="top" width="14.28%">
<!-- Assuming no members or link available -->
</td>
<td>0.81038</td>
</tr>
<tr>
<td>13</td>
<td>HIAS</td>
<td align="center" valign="top" width="14.28%">
<sub><b>苏鸿</b></sub>
<br />
<sub><b>张景瑞</b></sub>
<br />
<sub><b>汤丰杰</b></sub>
</td>
<td>0.84023</td>
<td>28</td>
<td>junda zhou</td>
<td align="center" valign="top" width="14.28%">
<sub><b>周均达</b></sub>
</td>
<td>0.80846</td>
</tr>
<tr>
<td>14</td>
<td>HanPeijia</td>
<td align="center" valign="top" width="14.28%">
<sub><b>韩佩佳</b></sub>
</td>
<td>0.84003</td>
<td>29</td>
<td>SCU_CTP</td>
<td align="center" valign="top" width="14.28%">
<sub><b>曹旭</b></sub>
<br />
<sub><b>高鸿飞</b></sub>
<br />
<sub><b>李志威</b></sub>
</td>
<td>0.80705</td>
</tr>
<tr>
<td>15</td>
<td>Zenghui Zou</td>
<td align="center" valign="top" width="14.28%">
<sub><b>邹增慧</b></sub>
<br />
<sub><b>李倾城</b></sub>
</td>
<td>0.83883</td>
<td>30</td>
<td>DESHUANGMeng</td>
<td align="center" valign="top" width="14.28%">
<sub><b>孟德双</b></sub>
</td>
<td>0.80462</td>
</tr>
  </tbody>
</table>          
  </tbody>
</table>


## Getting Started

Welcome to the course project! To get started with your programming assignments, you'll need to set up your workspace. Here's a step-by-step guide to help you through the process.

<details>
<summary>Step 1: Set Up Your GitHub Account and Fork the Repository</summary>

1. **Create a GitHub Account**: If you don't already have a GitHub account, go to [GitHub](https://github.com/) and sign up.
2. **Fork the Course Repository**:
    - Navigate to the course's GitHub repository: [GWData-Bootcamp](https://github.com/iphysresearch/GWData-Bootcamp).
    - Click on the `Fork` button at the top right of the page.
    - In the fork settings, make sure to **uncheck** the option 'copy `main` branch only'.
3. **Clone the Forked Repository**:
    - Open your terminal or Git Bash.
    - Clone the forked repository to your local machine using the following command:
      ```shell
      git clone git@github.com:<YourGitHubUsername>/GWData-Bootcamp.git
      ```
    - Replace `<YourGitHubUsername>` with your actual GitHub username.

</details>

<details>
<summary>Step 2: Set Up Your Local Workspace</summary>

1. **Switch to the `homework` Branch**:
    - Navigate to your cloned repository's directory:
      ```shell
      cd GWData-Bootcamp
      ```
    - Switch to the `homework` branch using:
      ```shell
      git switch homework
      ```
2. **Create Your Personal Homework Directory**:
    - Inside the `GWData-Bootcamp` directory, create a new directory path for your homework submissions:
      ```shell
      mkdir -p 2023/homework/<YourName>
      ```
      - Replace `<YourName>` with your name or a unique identifier.

</details>

<details>
<summary>Step 3: Submitting Your Homework</summary>

1. **Complete Your Assignments**:
     - Add your completed assignments to your personal homework directory that you created in the previous step.
     - The assignments should be named as `python_submit.txt`, `numpy_submit.txt`, or `pandas_submit.txt` depending on the type of the assignment.
2. **Push Your Changes**:
     - Stage and commit your changes. For example:
       ```shell
       git add .
       git commit -m "Add homework for <SpecificHomework>"
       ```
     - Push your `homework` branch to your forked repository:
       ```shell
       git push origin homework
       ```
3. **Create a Pull Request**:
    - Go to your forked repository on GitHub.
    - Switch to the `homework` branch.
    - Click on New Pull Request.
    - Ensure the base repository is set to the original `GWData-Bootcamp` repository and the base branch is set to `homework`.
    - Complete the PR form and submit.
    - The GitHub Actions workflow will automatically check your submission ([Homework](2023/python/readme.md#homework)) and compare it with the solution. If your submission passes the check, a merge request will be initiated. Please note that only the repository owners have the authority to merge the request.

</details>


### Important Notes

- **Do Not Modify Other Students' Work**: It's crucial that you do not make any changes to other students' homework directories and contents.
- **Regular Updates**: Keep your fork synchronized with the main repository to get the latest updates and assignments.
- Automated Checks: The GitHub Actions workflow will automatically check your submission when you create a pull request. Make sure your submission passes the check before you submit it.
- Happy Coding! 🚀👩‍💻👨

## Staff
This class is co-taught by [He Wang](https://iphysresearch.github.io/blog/) and several esteemed colleagues, including guest lecturers ([Junjie Zhao](https://orcid.org/0000-0002-9233-3683)) and industry experts ([Xinyao Tian](https://www.zhihu.com/people/winchester-26/activities) and [Minquan Gao](https://www.mqgao.com/)), whose names will be announced as they join.

## Questions
For any inquiries regarding the course, please email us at [📧 taiji@ucas.ac.cn](mailto:taiji@ucas.ac.cn).

We look forward to your participation and contribution to this exciting field of study!

## Contributing

We welcome contributions to enhance course materials. Please fork the repository, make your changes, and submit a pull request.

## Collaborating Institutions
- [University of Chinese Academy of Sciences](http://english.ucas.ac.cn/) (UCAS)

  <img src="logo-ucas.png" style="width:30%;height:auto;">

- [International Centre for Theoretical Physics Asia-Pacific](https://ictp-ap.org/) (ICTP-AP)

  <img src="logo-ictp-ap.png" style="width:30%;height:auto;"> 
  
- [Taiji Laboratory for Gravitational Wave Universe](https://ictp-ap.org/page/taiji-laboratory)

  <img src="logo-taiji-lab.png" style="width:20%;height:auto;">

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Contributions from the Gravitational Wave Open Science Center ([gwosc.org](https://gwosc.org/)).
- Educational resources and datasets from renowned institutions and projects in the field.

