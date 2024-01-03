# matplotlib 作业   韩佩佳


```python

```

# 数据可视化作业题目


```python
import matplotlib.pyplot as plt
import numpy as np
```

## 练习1：航班乘客变化分析 (2个题)

1. 分析年度乘客总量的变化情况（提示：折线图）
2. 分析乘客量在一年中12个月份的分布（提示：柱状图）


```python
import seaborn as sns
```


```python
data = sns.load_dataset("flights")
data.head()
# 年份，月份，乘客数
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>Jan</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>Feb</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>Mar</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>Apr</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 144 entries, 0 to 143
    Data columns (total 3 columns):
     #   Column      Non-Null Count  Dtype   
    ---  ------      --------------  -----   
     0   year        144 non-null    int64   
     1   month       144 non-null    category
     2   passengers  144 non-null    int64   
    dtypes: category(1), int64(2)
    memory usage: 2.9 KB



```python
# 设置图片尺寸
plt.figure(figsize=(8, 6))

# 不显示网格
plt.grid(False)

# 设置背景
plt.gca().set_facecolor('white')
# 按年份对乘客数量求和
yearly_passengers = data.groupby('year')['passengers'].sum()

# 绘制折线图
plt.plot(yearly_passengers.index, yearly_passengers.values, lw=2)

# 添加标题和标签
plt.title("The number of passengers in each year")
plt.xlabel("year")
plt.ylabel("number")

# 显示图形
plt.show()
```


    
![png](output_8_0.png)
    



```python
# 按月份对乘客数量求和
monthly_passengers = data.groupby('month')['passengers'].sum()

# 绘制折线图
plt.bar(monthly_passengers.index, monthly_passengers.values)

# 添加标题和标签
plt.title("The number of passengers in each month")
plt.xlabel("month", fontsize=14)
plt.ylabel("number", fontsize=14)

# 显示图形
plt.show()
```


    
![png](output_9_0.png)
    


## 练习2：鸢尾花花型尺寸分析 (3个题)

1. 萼片（sepal）和花瓣（petal）的大小关系（提示：散点图）
2. 不同种类（species）鸢尾花萼片和花瓣的大小关系（提示：箱图或者提琴图）
3. 不同种类鸢尾花萼片和花瓣大小的分布情况（六角箱图或者核密度估计）


```python
import seaborn as sns
```


```python
data = sns.load_dataset("iris")
data.head()
# 萼片长度，萼片宽度，花瓣长度，花瓣宽度，种类
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



#### 1. 萼片（sepal）和花瓣（petal）的大小关系（提示：散点图）


```python
# 设置图片尺寸、字体、网格和背景
plt.rcParams.update({
    'figure.figsize': (8, 8),
    'axes.grid': False,
    'axes.facecolor': 'white'
})

# 创建一个2x2的图表布局
fig, axs = plt.subplots(2, 2)

# 散点图和标题
plots = {
    (0, 0): ('sepal_length', 'petal_length', 's_l VS. p_l'),
    (0, 1): ('sepal_length', 'petal_width', 's_l VS. p_w'),
    (1, 0): ('sepal_width', 'petal_length', 's_w VS. p_l'),
    (1, 1): ('sepal_width', 'petal_width', 's_w VS. p_w')
}

# 绘制所有的散点图
for (i, j), (x, y, title) in plots.items():
    axs[i, j].scatter(data[x], data[y])
    axs[i, j].set_title(title)
    axs[i, j].set_xlabel(x)
    axs[i, j].set_ylabel(y)

# 显示图形
plt.show()
```


    
![png](output_14_0.png)
    


### 2. 不同种类（species）鸢尾花萼片和花瓣的大小关系（提示：箱图或者提琴图）


```python
# 创建一个2x2的图表布局
fig, axs = plt.subplots(2, 2)

# 创建一个字典，包含所有的散点图和标题
plots = {
    (0, 0): ('sepal_length', 'petal_length', 's_l VS. p_l'),
    (0, 1): ('sepal_length', 'petal_width', 's_l VS. p_w'),
    (1, 0): ('sepal_width', 'petal_length', 's_w VS. p_l'),
    (1, 1): ('sepal_width', 'petal_width', 's_w VS. p_w')
}

# 绘制所有的散点图
for (i, j), (x, y, title) in plots.items():
    for species in data['species'].unique():
        subdata = data[data['species'] == species]
        axs[i, j].scatter(subdata[x], subdata[y])
    axs[i, j].set_title(title)
    axs[i, j].set_xlabel(x)
    axs[i, j].set_ylabel(y)

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
```


    
![png](output_16_0.png)
    


### 3. 不同种类鸢尾花萼片和花瓣大小的分布情况（六角箱图或者核密度估计）


```python
# 创建一个1x3的图表布局
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 创建一个列表，包含所有的花的种类
species = ['setosa', 'versicolor', 'virginica']

# 创建一个列表，包含所有的特征
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# 绘制所有的箱线图
for i, spec in enumerate(species):
    axs[i].boxplot([data[data['species'] == spec][feature] for feature in features], labels=features)
    axs[i].set_title('The box with 4 features for the '+ spec +' flowers')
    axs[i].set_xlabel('Features of the '+ spec +' flowers')
    axs[i].set_ylabel('Values')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
```


    
![png](output_18_0.png)
    


## 练习3：餐厅小费情况分析 (7个题)

1. 小费和总消费之间的关系（提示：散点图+回归分析）
2. 男性顾客和女性顾客，谁更慷慨（提示：箱图或者提琴图）
3. 抽烟与否是否会对小费金额产生影响（提示：箱图或者提琴图）
4. 工作日和周末，什么时候顾客给的小费更慷慨（提示：箱图或者提琴图）
5. 午饭和晚饭，哪一顿顾客更愿意给小费（提示：箱图或者提琴图）
6. 就餐人数是否会对慷慨度产生影响（提示：箱图或者提琴图）
7. 性别+抽烟的组合因素对慷慨度的影响（提示：统计柱状图）


```python
data = sns.load_dataset("tips")
data.head()
# 总消费，小费，性别，吸烟与否，就餐星期，就餐时间，就餐人数
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### 1. 小费和总消费之间的关系（提示：散点图+回归分析）


```python
# 计算回归线的系数
coefficients = np.polyfit(data['total_bill'], data['tip'], 1)
# 创建回归线的函数
polynomial = np.poly1d(coefficients)
# 计算对应于total_bill的tip预测值
x_sorted = data['total_bill'].sort_values() # .sort_values() 用于排序，因为 data['total_bill'] 不是有序的
line = polynomial(x_sorted)

# total_bill vs. tip
plt.scatter(data['total_bill'],data['tip'])
plt.plot(x_sorted, line, color='red')
plt.title('total_bill VS. tip')
plt.xlabel('total_bill')
plt.ylabel('tip')

# 显示图形
plt.show()
```


    
![png](output_22_0.png)
    


### 2. 男性顾客和女性顾客，谁更慷慨（提示：箱图或者提琴图）


```python
# 绘制箱线图
data.boxplot(column='tip', by='sex')

# 添加标题和标签
plt.title('The box with 2 features for the tip')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Features of the sex')
plt.ylabel('Vaules of tip')

# 显示图形
plt.show()
```


    
![png](output_24_0.png)
    


### 3. 抽烟与否是否会对小费金额产生影响（提示：箱图或者提琴图）


```python
# 绘制箱线图
data.boxplot(column='tip', by='smoker')

# 添加标题和标签
plt.title('The box with 2 features for the tip')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Features of the smoker')
plt.ylabel('Vaules of tip')

# 显示图形
plt.show()
```


    
![png](output_26_0.png)
    


### 4. 工作日和周末，什么时候顾客给的小费更慷慨（提示：箱图或者提琴图）


```python
# 绘制箱线图
data.boxplot(column='tip', by='day')

# 添加标题和标签
plt.title('The box with 2 features for the tip')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Features of the day')
plt.ylabel('Vaules of tip')

# 显示图形
plt.show()
```


    
![png](output_28_0.png)
    


### 5. 午饭和晚饭，哪一顿顾客更愿意给小费（提示：箱图或者提琴图）


```python
# 绘制箱线图
data.boxplot(column='tip', by='time')

# 添加标题和标签
plt.title('The box with 2 features for the tip')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Features of the time')
plt.ylabel('Vaules of tip')

# 显示图形
plt.show()
```


    
![png](output_30_0.png)
    


### 6. 就餐人数是否会对慷慨度产生影响（提示：箱图或者提琴图）


```python
# 绘制箱线图
data.boxplot(column='tip', by='size')

# 添加标题和标签
plt.title('The box with 2 features for the tip')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Features of the size')
plt.ylabel('Vaules of tip')

# 显示图形
plt.show()
```


    
![png](output_32_0.png)
    


### 7. 性别+抽烟的组合因素对慷慨度的影响（提示：统计柱状图）


```python
# 计算每个sex和smoker组合的小费
sex_smoker = data.groupby(['sex', 'smoker'])['tip'].mean().unstack()

# 绘制柱状图
sex_smoker.plot(kind='bar', rot=0)

# 添加标题和轴标签
plt.title('Values by Sex (Male or Female) and Smoker (Yes or No)')
plt.xlabel('Sex')
plt.ylabel('Values of tip')

# 显示图形
plt.show()
```


    
![png](output_34_0.png)
    


## 练习4：泰坦尼克号海难幸存状况分析 (8个题)

1. 不同仓位等级中幸存和遇难的乘客比例（提示：箱图或者提琴图）
2. 不同性别的幸存比例（提示：箱图或者提琴图）
3. 幸存和遇难乘客的票价分布（提示：箱图或者提琴图）
4. 幸存和遇难乘客的年龄分布（提示：箱图或者提琴图）
5. 不同上船港口的乘客仓位等级分布（提示：箱图或者提琴图）
6. 幸存和遇难乘客堂兄弟姐妹的数量分布（提示：箱图或者提琴图）
7. 幸存和遇难乘客父母子女的数量分布（提示：箱图或者提琴图）
8. 单独乘船与否和幸存之间有没有联系（提示：统计柱状图）


```python
import seaborn as sns
data = sns.load_dataset("titanic")
data.head()
# 幸存与否，仓位等级，性别，年龄，堂兄弟姐妹数，父母子女数，票价，上船港口缩写，仓位等级，人员分类，是否成年男性，所在甲板，上船港口，是否幸存，是否单独乘船
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



### 1. 不同仓位等级中幸存和遇难的乘客比例（提示：箱图或者提琴图）


```python
# 设置图片尺寸、字体、网格和背景
plt.rcParams.update({
    'figure.figsize': (5, 5),
    'font.size': 10,
    'axes.grid': False,
    'axes.facecolor': 'white'
})

# 添加遇难列
data['unsurvived'] = 1 - data['survived']  

# 按仓位等级分组
survied_unsurvied = data.groupby('pclass')[['survived', 'unsurvived']].sum()

# 计算生存率和遇难率
survied_unsurvied['total'] = survied_unsurvied['survived'] + survied_unsurvied['unsurvived']
survied_unsurvied['survived_prop'] = survied_unsurvied['survived'] / survied_unsurvied['total']
survied_unsurvied['unsurvived_prop'] = survied_unsurvied['unsurvived'] / survied_unsurvied['total']

# 绘制堆叠柱状图
ax = survied_unsurvied[['survived_prop','unsurvived_prop']].plot(kind='bar', stacked=True)

# 添加标题和标签
ax.set_title('Proportion of survived/unsurvived by Pclass (1, 2, 3)')
ax.set_xlabel('Pclass')
ax.set_ylabel('Proportion of survived/unsurvived')

# 将x轴的标签设置为水平
plt.xticks(rotation=0)

# 显示图形
plt.show()
```


    
![png](output_38_0.png)
    


### 2. 不同性别的幸存比例（提示：箱图或者提琴图）


```python
# 添加遇难列
data['unsurvived'] = 1 - data['survived']  

# 按性别分组并计算生存率和遇难率
sex = data.groupby('sex')[['survived', 'unsurvived']].sum()
sex['total'] = sex.sum(axis=1)
sex[['survived_prop', 'unsurvived_prop']] = sex[['survived', 'unsurvived']].div(sex['total'], axis=0)

# 绘制堆叠柱状图
ax = sex[['survived_prop','unsurvived_prop']].plot(kind='bar', stacked=True, rot=0)

# 添加标题和标签
ax.set_title('Proportion of survived/unsurvived by sex')
ax.set_xlabel('Sex')
ax.set_ylabel('Proportion of survived/unsurvived')

# 显示图形
plt.show()
```


    
![png](output_40_0.png)
    


### 3. 幸存和遇难乘客的票价分布（提示：箱图或者提琴图）


```python
# 绘制箱线图
data.boxplot(column='fare', by='survived')
     # column 参数指定了数据列（票价），by 参数指定了分组的基准（幸存与否）

# 添加标题和标签
plt.title('The box with 2 features for the fare')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Features of the survived')
plt.ylabel('Vaules of fare')
plt.xticks([1, 2], ['Not survived', 'Survived'])  # 重命名x轴标签

# 显示图形
plt.show()
```


    
![png](output_42_0.png)
    


### 4. 幸存和遇难乘客的年龄分布（提示：箱图或者提琴图）


```python
# 绘制箱线图
data.boxplot(column='age', by='survived')

# 添加标题和标签
plt.title('The box with 2 features for the age')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Features of the survived')
plt.ylabel('Vaules of age')
plt.xticks([1, 2], ['Not survived', 'Survived'])  # 重命名x轴标签

# 显示图形
plt.show()
```


    
![png](output_44_0.png)
    


### 5. 不同上船港口的乘客仓位等级分布（提示：箱图或者提琴图）


```python
# 计算每个Pclass和Embarked组合的乘客数量
Embarked = data.groupby(['embarked','pclass']).size().unstack()

# 绘制柱状图
Embarked.plot(kind='bar', rot=0)

# 添加标题和轴标签
plt.title('Number of people for different kind of pclass by embarked')
plt.xlabel('Embarked')
plt.ylabel('Number of people for different kind of pclass')

# 显示图形
plt.show()
```


    
![png](output_46_0.png)
    


### 6. 幸存和遇难乘客堂兄弟姐妹的数量分布（提示：箱图或者提琴图）


```python
# 按 sibsp 分组求和
data['unsurvived'] = 1 - data['survived']
data['total'] = data['survived'] + data['unsurvived']

# 绘制箱线图
data.boxplot(column='sibsp', by='survived')

# 添加标题和标签
plt.title('The box with 2 features for the sibsp')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Survived')
plt.ylabel('Values of sibsp')
plt.xticks([1, 2], ['Not survived', 'Survived'])  # 重命名x轴标签

# 显示图形
plt.show()
```


    
![png](output_48_0.png)
    


### 7. 幸存和遇难乘客父母子女的数量分布（提示：箱图或者提琴图）


```python
# 按 parch 分组求和
data.groupby('parch')[['survived','unsurvived','total']].sum()

# 绘制箱线图
data.boxplot(column='parch', by='survived')

# 添加标题和标签
plt.title('The box with 2 features for the parch')
plt.suptitle('')  # 去除默认的子标题
plt.xlabel('Survived')
plt.ylabel('Values of parch')
plt.xticks([1, 2], ['Not survived', 'Survived'])  # 重命名x轴标签

# 显示图形
plt.show()
```


    
![png](output_50_0.png)
    


### 8. 单独乘船与否和幸存之间有没有联系（提示：统计柱状图）


```python
# 计算每个alone和survived组合的乘客数量
alone = data.groupby(['alone','survived']).size().unstack()

# 绘制柱状图
alone.plot(kind='bar', rot=0)

# 添加标题和轴标签
plt.title('Number of people for different kind of pclass by alone or not')
plt.xlabel('Alone or not')
plt.ylabel('Number of people')

# 显示图形
plt.show()
```


    
![png](output_52_0.png)
    



```python

```
