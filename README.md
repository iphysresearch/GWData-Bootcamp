# 引力波数据探索：编程与分析实战训练营
# Gravitational Wave Data Exploration: A Practical Training in Programming and Analysis

> Under construction...

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

  - Date：[2023/11/08](2023/intro/readme.md) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=a1f3c150-eeb3-4266-a4cc-4099bb28d382&from=3) | Slide: [PDF](2023/intro/slide.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_0)
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

  - Date：[2023/11/12](2023/workflow/readme.md#2023-11-12) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=af256140-e032-4b0c-9116-5741fad5010b&from=3) | Slide: [PDF](2023/workflow/slide.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_1)
  - [Homework](2023/workflow/readme.md#homework)
      - Docker Container Setup
      - Remote Development for Python/Jupyter with GPU Support and LALsuite/LISAcode Compilation
  - Date：[2023/11/19](2023/workflow/readme.md#2023-11-19) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=d1e10208-857a-429c-80ee-8a5bfbb88d52&from=3) | Slide: [PDF](2023/workflow/slide_git.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_1_git)
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

  - Date：[2023/11/19](2023/TechTalk1/readme.md) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=8582150d-9dae-4938-b912-162e6b98bf63&from=3) | Slide: [markdown](2023/TechTalk1/readme.md)
    
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

  - Date：[2023/11/29](2023/python/readme.md#2023-11-29) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=38d62612-d754-413f-b6a9-2d0d960f4549&from=3) | Slide: [PDF](2023/python/slide_python.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_python)
  - Date：[2023/12/01](2023/python/readme.md#2023-12-01) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=0e5f06cb-8c5b-4e28-a1ba-a766025510e4&from=3) | Slide: [PDF](2023/python/slide_numpy.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_numpy)
  - Date：[2023/12/03](2023/python/readme.md#2023-12-03) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=eef300fb-a794-4aff-93e2-0ec36501b1b6&from=3) | Slide: [PDF](2023/python/slide_pandas.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_pandas)
  - [Homework](2023/python/readme.md#homework)
      - Python, Numpy, Pandas Basic Homework
      - Leetcode Extension Tasks
  - Date：[2023/12/08](2023/python/readme.md#2023-12-08) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=dd9f5242-b3a8-4500-9436-ba190a739c10&from=3) | Slide: [PDF](2023/python/slide_visualization.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_2_visualization)
  - Date：[2023/12/10](2023/python/readme.md#2023-12-10) | Video [recording](https://pan.baidu.com/s/1MiqCAMGP7-B76uOHCDgErg?pwd=ph8c)
  - [Homework](2023/python/readme.md#homework-1)
      - Data visualization and analysis using Python libraries, matplotlib and seaborn.
  - [Homework](2023/python/4-GWTC3.ipynb)
      - Recreate Figure 7 from the GWTC-3 paper using numpy, pandas, matplotlib, and seaborn.
  - Date：[2023/12/15](2023/python/readme.md#2023-12-15) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=2f4d95c6-424e-400e-b822-2bf3095ab3be&from=3) | [ipynb](2023/python/5-GW150914.ipynb) | [html](2023/python/5-GW150914.html)
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

  - Date：[2023/12/16](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/README.md) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=eb4e542d-a49d-4b38-ad1d-1d362ecddbea&from=3) | Slide: [PDF](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/Junjie%20-%202023%20-%20bayesian%20for%20GWData-Bootcamp.pdf)
  - Date：[2023/12/17](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/README.md) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=11e13d08-ed8a-4455-a373-6df7bcc0d43a&from=3) | Slide: [PDF](https://github.com/BenjaminDbb/BayesianInference4GW_GWData_Bootcamp/blob/main/Junjie%20-%202023%20-%20bayesian%20for%20GWData-Bootcamp.pdf)


- **Part Three**: _Basics of Machine Learning_
    <details>
    <summary>Description</summary>
  
      - Overview of Artificial Intelligence
      - Definitions, Objectives, and Types of Machine Learning
      - Machine Learning Project Development and Preparation
      - Hands-On: Clustering Analysis of LIGO's Glitch Data

    </details>

  - Date：[2023/12/22](2023/machine_learning/readme.md#2023-12-22) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=9972f117-e915-431e-9124-c2417f561304&from=3) | Slide: [PDF](2023/machine_learning/slide_ml_1.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_3_intro)
  - [Homework](2023/machine_learning/readme.md#homework)
      - Implement a classification model for credit scoring using the sklearn library in Python.
  - Date：[2023/12/24](2023/machine_learning/readme.md#2023-12-24) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=d4b30c68-910c-4c19-943d-9e49a419ebe7&from=3) | Slide: [PDF](2023/machine_learning/slide_ml_2.pdf) or [online](https://slides.com/iphysresearch/gwda_coding_3_adv)
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

  - Date：[2023/12/27](2023/deep_learning/readme.md#2023-12-27) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=b2bbb9da-94dd-45df-94f2-b5bf9e095e60&from=3) | Slide: [PDF](https://pan.baidu.com/s/1kX8KbQMiMMOubyTwiqTdXQ?pwd=audc) or [online](https://slides.com/iphysresearch/gwda_coding_4_ann)
  - Date：[2023/12/29](2023/deep_learning/readme.md#2023-12-29) | Video [recording](https://meeting.tencent.com/v2/cloud-record/share?id=9dd600c1-9183-443c-9fd5-ad7116440f47&from=3) | Slide: [PDF](https://pan.baidu.com/s/1nwaAbHIl1Ed7JATm3tGxlw?pwd=6h69) or [online](https://slides.com/iphysresearch/gwda_coding_4_cnn)

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

  - Date：[2023/12/31]() | Video [recording]()


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

- This competition will start at 10:00 PM (Beijing Time) on December 29, 2023, and end at 11:59 PM (Beijing Time) on January 5, 2024.
- Please make sure to submit your solutions before the deadline.

- Good luck and may the best team win!

### Files

- [data_prep_bbh.py](2023/deep_learning/baseline/data_prep_bbh.py) - script for data generation (credit: [Dr. Hunter Gabbard](https://github.com/hagabbar/cnn_matchfiltering/))
- [utils.py](2023/deep_learning/baseline/utils.py) - supplemental script containing some useful functions
- [main.py](2023/deep_learning/baseline/main.py) - main script for training / evaluation / submission
- [test.npy](https://www.kaggle.com/competitions/2023-gwdata-bootcamp/data?select=test.npy) - test data for submission (You can load the test data in the [Kaggle notebook](https://www.kaggle.com/code/herbwang/baseline-kaggle))

> Anyway, just check the [baseline notebook](2023/deep_learning/baseline/baseline_sugon.ipynb) for everything!


## Getting Started

Welcome to the course project! To get started with your programming assignments, you'll need to set up your workspace. Here's a step-by-step guide to help you through the process.

### Step 1: Set Up Your GitHub Account and Fork the Repository

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

### Step 2: Set Up Your Local Workspace

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

### Step 3: Submitting Your Homework

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

