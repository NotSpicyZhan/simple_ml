
<center>
<img src="./docs/imgs/logo2.png" width="100%" height="100%" />
</center>


Simple Machine Learning

一个简单的机器学习算法实现


![](https://img.shields.io/pypi/v/simple_male.svg) [![Build Status](https://travis-ci.org/Yangruipis/simple_ml.svg?branch=master)](https://travis-ci.org/Yangruipis/simple_ml) [![Coverage Status](https://coveralls.io/repos/github/Yangruipis/simple_ml/badge.svg?branch=master)](https://coveralls.io/github/Yangruipis/simple_ml?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/00c639db60364d12b0102456552fe806)](https://www.codacy.com/app/Yangruipis/simpleML?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Yangruipis/simpleML&amp;utm_campaign=Badge_Grade)

![](https://img.shields.io/npm/l/express.svg) [![Join the chat at https://gitter.im/simple_ml/Lobby](https://badges.gitter.im/simple_ml/Lobby.svg)](https://gitter.im/simple_ml/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

---


# 快速开始

## 安装

**环境和依赖库**
- python3.5及以上
- windows or Linux
- numpy      (数组)
- matplotlib (作图)
- scipy      (求解优化问题)
- requests   (用于在线数据集获取)
- cvxopt    (支持向量机中的二次规划问题)

`强烈推荐Anaconda环境`

**pip安装**

```bash
pip install simple_male
```
对，是`simple_ma(chine)le(arning)`，简单男人，因为`simple_ml`已经在pypi上被人注册了喵

**git安装**

```bash
git clone https://github.com/Yangruipis/simple_ml.git
cd ./simple_ml
python setup.py install
```

## 使用

```python
# 一个简单的例子，用CART树进行二分类
from simple_ml.tree import CART
import numpy as np

X = np.array([[1,1.1],
              [1,2.0],
              [0,3.0],
              [0,2.2]])
y = np.array([1,1,0,0])
cart = CART(min_samples_leaf=1)
cart.fit(X, y)
x_test = np.array([[1,2],[3,4]])
print(cart.predict(x_test))
```
```python
Out[1]: np.array([1,1])
```

- `./simple_ml/examples`文件夹中提供了大多数方法的使用范例
- 更详细的用法见帮助文档： [https://yangruipis.github.io/simple_ml/](https://yangruipis.github.io/simple_ml/)

# 它能做什么

## 最最最最主要的任务

如果你同时满足：
1. **机器学习入门阶段**
2. **python 进阶阶段**

那么恭喜你，这个项目可以给你提供如下帮助：

- **阅读源码**， 不像sklearn过于复杂难读的源码，这个轻量级的项目非常易读，并且我尽可能的增加了注释，提高代码的可读性
- **学习知识**，该项目梳理基本机器学习算法的种类和流程，工程实现上的大致步骤，中间出现的一些细节问题以及如何解决
- **实时交流**，我在 gitter 上建立了 [gitchat 聊天室](https://gitter.im/simple_ml/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)，欢迎大家就项目本身的具体问题，或者其他任何相关事项进行讨论，欢迎大家积极提 issues，我会第一时间回复


## 作为一个机器学习项目的任务

### 1. 数据和特征

#### 1.1 数据集获取

`simple_ml`提供了大量经典的机器学习数据集的获取接口`DataCollector`，数据集来自[UCI](http://archive.ics.uci.edu/ml/index.php)。

#### 1.2 数据预处理

`simple_ml` 提供了常用的数据预处理方法，包括了编码、独热编码、缺失值处理、异常值处理以及随机数据集划分等。

同时，`simple_ml` 提供了`PCA`降维方法以及针对高维数据的`SuperPCA`降维方法。

#### 1.3 特征选择
`simple_ml`提供了Filter和Embedded两种特征选择方法，包括了：
1. 方差法
2. 相关系数法
3. 卡方检验法
4. L1正则
5. GBDT特征选择

### 2. 模型

#### 2.1 二分类
`simple_ml`提供了非常多的二分类方法，以[wine数据集](http://archive.ics.uci.edu/ml/datasets/Wine)为例（见`./simple_ml/examples`），分类效果和方法名称见图1。

<center>
<img src="./docs/imgs/wine.jpg"  />

图 1. 二分类效果图
</center>

#### 2.2 多分类

`simple_ml`暂时只提供了一些多分类算法，见下图，同样是[wine数据集](http://archive.ics.uci.edu/ml/datasets/Wine)，后面作者将会进行补充。

<center>
<img src="./docs/imgs/wine2.jpg" />

图 2. 多分类效果图
</center>


#### 2.3 回归

`simple_ml`提供了回归方法如下
- `MultiRegression`
- `CART`
- `GBDT`
- `SVR`

#### 2.4 聚类

`simple_ml`提供了`K-means聚类`、`层次聚类`、`DBSCAN密度聚类`三种聚类方法

`注:`以上所有图均为simple_ml直出（需要matplotlib）

### 3. 效果评价

包括了分类和回归作图、以及针对二分类、多分类、回归问题的评价指标计算，包括Precision, Recall等等

# 为什么会有这个项目 & 致谢

作者就读于上海某商科院校经济学，从大二开始接触数据挖掘，以及编程相关知识（stata->R->C#->python)，对数据和编程非常感兴趣，基本上一路走过来全靠自学。作者希望可以用心做好一个项目，记录自己学习的轨迹，尤其是即将毕业之际。

在接下来的一年找工作的同时，作者将尽全力维护该项目，不断更新和修改，热烈欢迎任何贡献和讨论。

**致谢：**
- 首先感谢我自己，一路走来的不易如人饮水
- 其次感谢我的好友[何燕杰](https://github.com/YanjieHe)和[程刚](https://github.com/chenggang0815)对我在学习和工作上的帮助
- 最后感谢所有相关书籍、博客的作者，尤其感谢[刘建平Pinard](https://www.cnblogs.com/pinard/)一丝不苟的机器学习博客，无论是知识还是态度，都令人肃然起敬


# 更新日志

- 2018-04-20
  - 加入BP神经网络算法`simple.neural_network`和相关的example
  - 更新github pages
- 2018-04-23
  - 加入`Stacking model`
  - 更新每个模型的new()函数
  - 重写`BaseModel`的`predict`和`score`抽象方法，以检查测试集是否满足要求
  - fix SuperPCA bugs
- 2018-04-24
  - 加入类：
    `Multi2binary`，继承该类的`BaseClassifier`可以将多分类问题转为二分类问题
  - 添加SVM， Logistic，NeuralNetwork, AdaBoost 的继承关系和多分类方法
  - 增加相关的多分类例子，以及帮助文档
  - 重写特征类型推断函数，根据多种线索进行推断
- 2018-04-26
  - 重写自动化模块`auto`，实现`BaseAuto`抽象类以及数据自动预处理的`AutoDataHandle`类
  - 加入网格搜索方法
  - 加入[宫颈癌数据](https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29)的完整处理Example
  - 加入`helper`模块，用于格式化输出
  - 加入`data_handle`模块的缺失值统计方法`nan_summary`
- 2018-04-27
  - 加入自动特征选择类 `AutoFeatureHandle` ，以及对应的宫颈癌Example
- 2018-06-11
  - 加入回归作图方法
- 2018-06-12
  - 加入多元回归方法`MultiRegression`并测试
  - `MultiRegression`中加入加权回归方法
- 2018-06-13
  - 重写支持向量机`SVM`，调用优化库进行求解，而不是手写SMO
  - 加入支持向量回归`SVR`
  - 整个支持向量相关算法,包括了`Kernel`类, `BaseSupportVector`类以及`SVM`,`SVR`
- 2018-06-20
  - 添加相关测试用例
- 2018-06-23
  - 添加`optimal`模块，包括了爬山法和模拟退火法进行最小值求解
  - pypi发布，版本 `0.1.2`
- 2018-08-01
  - 添加`DBSCAN`聚类方法
  - 添加`DBSCAN`相关例子

# TODO list:

- [ ] test cases
- [x] an efficient bp network
- [ ] more optimal methods
- [x] train test split func in helper
- [x] other feature select method to add
- [x] lasso and Ridge
- [x] add GBDT feature select
- [x] update Readme
- [x] setup.py
- [x] examples
- [x] get more datasets
- [x] regression plot
- [x] more regression method
- [ ] kd_tree
- [x] Support Machine Regression
- [x] more metrics
- [x] github pages, especially the class map
- [x] stacking
- [x] 二分类转多分类器
- [x] recognize nan and inf
- [x] check x before predict, check x and y before score
- [x] "self.new()" function in each model
- [x] 支持向量相关算法测试和文档撰写
- [x] pypi发布
- [ ] 移除logistic.py 中对scipy的依赖,自己写fmin(),以及实现底层优化算法
- [ ] LSTM
- [x] DBSCAN cluster


# TODO List AUTO MODEL

- [x] auto data handle
- [x] auto feature select
- [ ] auto param select
- [ ] auto model select
