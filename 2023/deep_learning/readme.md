
# 第 4 部分 深度学习基础

## 2023-12-27
- Video: [https://meeting.tencent.com/v2/cloud-record/share?id=b2bbb9da-94dd-45df-94f2-b5bf9e095e60&from=3](https://meeting.tencent.com/v2/cloud-record/share?id=b2bbb9da-94dd-45df-94f2-b5bf9e095e60&from=3)
- Slide: [PDF](https://pan.baidu.com/s/1kX8KbQMiMMOubyTwiqTdXQ?pwd=audc) or [https://slides.com/iphysresearch/gwda_coding_4_ann](https://slides.com/iphysresearch/gwda_coding_4_ann)
- Notebooks:
  - Multilayer Neural Network Tutorial: [ipynb](./neural_network_scratch.ipynb) or [html](./neural_network_scratch.html)

## 2023-12-29
- Video: [https://meeting.tencent.com/v2/cloud-record/share?id=9dd600c1-9183-443c-9fd5-ad7116440f47&from=3](https://meeting.tencent.com/v2/cloud-record/share?id=9dd600c1-9183-443c-9fd5-ad7116440f47&from=3)
- Slide: [PDF](https://pan.baidu.com/s/1nwaAbHIl1Ed7JATm3tGxlw?pwd=6h69) or [https://slides.com/iphysresearch/gwda_coding_4_cnn](https://slides.com/iphysresearch/gwda_coding_4_cnn)
- Notebooks:
  - Convolutional Neural Network Tutorial and gravitational wave detection: [ipynb](./baseline/baseline_sugon.ipynb) or [html](./baseline/baseline_sugon.html)

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

- [data_prep_bbh.py](baseline/data_prep_bbh.py) - script for data generation (credit: [Dr. Hunter Gabbard](https://github.com/hagabbar/cnn_matchfiltering/))
- [utils.py](baseline/utils.py) - supplemental script containing some useful functions
- [main.py](baseline/main.py) - main script for training / evaluation / submission
- [test.npy](https://www.kaggle.com/competitions/2023-gwdata-bootcamp/data?select=test.npy) - test data for submission (You can load the test data in the [Kaggle notebook](https://www.kaggle.com/code/herbwang/baseline-kaggle))

> Anyway, just check the [baseline notebook](baseline/baseline_sugon.ipynb) for everything!
---



> 曙光智算的计算服务账号申请入口：华东一区【昆山】
> 
> ![](https://cdn.sa.net/2023/12/22/8mG4fpAkhnLTyNW.jpg)
>
> 在【镜像仓库】中找到镜像：`gwdata-bootcamp:v1.0`,
>
> 【克隆】到【我的镜像】后，即可在【notebook】中新建notebook里找到。
>
> ![](https://cdn.sa.net/2023/12/22/Xs7UFtfa9g4ScTD.jpg)
