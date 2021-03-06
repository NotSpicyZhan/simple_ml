# 线性学习模块 **simple_ml.logistic**




<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [线性学习模块 **simple_ml.logistic**](#线性学习模块-simple_mllogistic)
    - [一、标准Logistic回归](#一标准logistic回归)
        - [1.1 初始化](#11-初始化)
        - [1.2 类方法](#12-类方法)
        - [1.3 类属性](#13-类属性)
    - [二、 最小损失回归 (Lasso)](#二-最小损失回归-lasso)
        - [2.1 初始化](#21-初始化)
        - [2.2 类方法](#22-类方法)
        - [2.3 类属性](#23-类属性)
    - [三、岭回归 (Ridge)](#三岭回归-ridge)
        - [3.1 初始化](#31-初始化)
        - [3.2 类方法](#32-类方法)
        - [3.3 类属性](#33-类属性)
    - [四、多元线性回归 (MultiRegression)](#四多元线性回归-multiregression)
        - [4.1 初始化](#41-初始化)
        - [4.2 类方法](#42-类方法)
        - [4.3 成员属性](#43-成员属性)
    - [Examples](#examples)
- [返回主页](#返回主页)

<!-- /code_chunk_output -->


## 一、标准Logistic回归


```python
from simple_ml.base.base_model import BaseClassifier

class LogisticRegression(BaseClassifier):

    __doc__ = "Logistic Regression"

    def __init__(self, tol=0.01, alpha=0.01, threshold=0.5, 
                has_intercept=True):
        """
        不包含惩罚项的Logistic回归
        :param tol:            误差容忍度，越大时收敛越快，但是越不精确
        :param alpha:           步长，梯度下降的参数
        :param threshold:      决策阈值，当得到的概率大于等于阈值时输出1，否则输出0
        :param has_intercept:  是否包含截距项
        """
        pass
```

`simple_ml`
提供了标准的Logistic回归模型，采用**梯度下降**进行参数估计，后面会加入更多优化方法

`Logistic`回归支持：
- 二分类问题


* * *

### 1.1 初始化

|             |     名称      |     类型     |              描述               |
|------------:|:-------------:|:------------:|:-------------------------------:|
| Parameters: |      tol      |    float     |            误差容忍度            |
|             |     step      | float, (0,1] |           梯度下降步长           |
|             |   threshold   | float,(0,1)  | 分类阈值，大于该值为1，小于该值为0 |
|             | has_intercept |     bool     |          是否含有截距项          |


### 1.2 类方法

1 拟合

```python
def fit(self, x, y)
```

拟合特征

|             | 名称 |    类型     |     描述      |
|------------:|:----:|:----------:|:------------:|
| Parameters: |  x   | np.2darray |     训练集特征      |
|             |  y   |  np.array  | 训练集标签 |
|    Returns: |      |    Void    |              |


2 预测

```python
def predict(self, x)
```


给定测试集特征x，进行预测

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|    Returns: |      |  np.array  | 预测的结果 |

3 结果评价

```python
def score(self, x, y)
```

拟合并进行预测，最后给出预测效果的得分


|             | 名称 |    类型     |                            描述                            |
|------------:|:----:|:----------:|:---------------------------------------------------------:|
| Parameters: |  x   | np.2darray |                         测试集特征                         |
|             |  y   |  np.array  |                         测试集标签                         |
|    Returns: |      |   float    | 预测结果评分，此处给出F1值 |

4 分类作图

`logistic`模块提供了直接绘制分类效果图的方法，如果维度大于2，则通过PCA降至两维

```python
def classify_plot(self, x, y, title="")
```

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|             |  y   |  np.array  | 测试集标签 |
|    Returns: |      |    Void    |           |

5 概率预测

```python
def predict_prob(self, x)
```

给定测试集特征x，对其正负类的概率进行预测

|             | 名称 |       类型       |             描述              |
|------------:|:----:|:---------------:|:----------------------------:|
| Parameters: |  x   |   np.2darray    |          测试集特征           |
|    Returns: |      | np.array(float) | 预测的结果，表示为正类(1)的概率 |

6 ROC曲线绘制

针对二分类且可以包含
`predict_prob`方法的模型，我们均给出了ROC曲线的绘制方法`auc_plot`，并且在图中输出AUC值

```python
def auc_plot(self, x, y)
```

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|             |  y   |  np.array  | 测试集标签 |


### 1.3 类属性


|     名称      |    类型    |         描述          |
|:-------------:|:----------:|:---------------------:|
| weight |   np.array(float)   | 每个特征的参数 |



## 二、 最小损失回归 (Lasso)



```python
from simple_ml.base.base_model import BaseFeatureSelect
from simple_ml.logistic import LogisticRegression

class Lasso(LogisticRegression, BaseFeatureSelect):

    __doc__ = "Lasso Regression"

    def __init__(self, tol=0.01, lamb=0.1, alpha=0.01, threshold=0.5, has_intercept=True):
        """
        包含L1惩罚项的Logistic回归
        :param tol:            误差容忍度，越大时收敛越快，但是越不精确
        :param lamb            lambda，即惩罚项前面的参数，越大越不容易过拟合，但是偏差也越大
        :param alpha:           步长，梯度下降的参数
        :param threshold:      决策阈值，当得到的概率大于等于阈值时输出1，否则输出0
        :param has_intercept:  是否包含截距项
        """
        super(Lasso, self).__init__(tol, alpha, threshold, has_intercept)
        self.lamb = lamb
```

`simple_ml` 提供了带`L1正则项`的Logistic回归模型，即Lasso模型，采用**坐标下降**进行参数估计，后面会加入更多优化方法

同时,`Lasso`继承了`BaseFeatureSelect`类，可以进行特征选择

`Lasso`回归支持：
- 二分类问题


* * *

### 2.1 初始化

|             |     名称      |     类型     |              描述               |
|------------:|:-------------:|:------------:|:-------------------------------:|
| Parameters: |      tol      |    float     |            误差容忍度            |
|             |     step      | float, (0,1] |           梯度下降步长           |
|             |   threshold   | float,(0,1)  | 分类阈值，大于该值为1，小于该值为0 |
|             | has_intercept |     bool     |          是否含有截距项          |
|             |      lamb         |    float          |                    正则项系数             |


### 2.2 类方法

1 拟合

```python
def fit(self, x, y)
```

拟合特征

|             | 名称 |    类型     |     描述      |
|------------:|:----:|:----------:|:------------:|
| Parameters: |  x   | np.2darray |     训练集特征      |
|             |  y   |  np.array  | 训练集标签 |
|    Returns: |      |    Void    |              |


2 预测

```python
def predict(self, x)
```


给定测试集特征x，进行预测

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|    Returns: |      |  np.array  | 预测的结果 |

3 结果评价

```python
def score(self, x, y)
```

拟合并进行预测，最后给出预测效果的得分


|             | 名称 |    类型     |                            描述                            |
|------------:|:----:|:----------:|:---------------------------------------------------------:|
| Parameters: |  x   | np.2darray |                         测试集特征                         |
|             |  y   |  np.array  |                         测试集标签                         |
|    Returns: |      |   float    | 预测结果评分，此处给出F1值 |

4 分类作图

`logistic`模块提供了直接绘制分类效果图的方法，如果维度大于2，则通过PCA降至两维

```python
def classify_plot(self, x, y, title="")
```

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|             |  y   |  np.array  | 测试集标签 |
|    Returns: |      |    Void    |           |

5 概率预测

```python
def predict_prob(self, x)
```

给定测试集特征x，对其正负类的概率进行预测

|             | 名称 |       类型       |             描述              |
|------------:|:----:|:---------------:|:----------------------------:|
| Parameters: |  x   |   np.2darray    |          测试集特征           |
|    Returns: |      | np.array(float) | 预测的结果，表示为正类(1)的概率 |

6 ROC曲线绘制

针对二分类且包含
`predict_prob`方法的模型，我们均给出了ROC曲线的绘制方法`auc_plot`，并且在图中输出AUC值

```python
def auc_plot(self, x, y)
```

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|             |  y   |  np.array  | 测试集标签 |

7 特征选择

```python
def feature_select(self, top_n)
```

|             | 名称 |       类型       |             描述              |
|------------:|:----:|:---------------:|:----------------------------:|
| Parameters: |  top_n   |   int   |          希望选择前几个特征           |
|    Returns: |      | np.array(int) | 选中特征的id数组 |



### 2.3 类属性

|     名称      |    类型    |         描述          |
|:-------------:|:----------:|:---------------------:|
| weight |   np.array(float)   | 每个特征的参数 |


## 三、岭回归 (Ridge)

```python
from simple_ml.logistic import Lasso

class Ridge(Lasso):

    __doc__ = "Ridge Regression"

    def __init__(self, tol=0.01, lamb=0.1, alpha=0.01, threshold=0.5, has_intercept=True):
        """
        包含L2惩罚项的Logistic回归
        :param tol:            误差容忍度，越大时收敛越快，但是越不精确
        :param lamb            lambda，即惩罚项前面的参数，越大越不容易过拟合，但是偏差也越大
        :param alpha:           步长，梯度下降的参数
        :param threshold:      决策阈值，当得到的概率大于等于阈值时输出1，否则输出0
        :param has_intercept:  是否包含截距项
        """
        super(Ridge, self).__init__(tol, lamb, alpha, threshold, has_intercept)

```

`simple_ml` 提供了带`L2正则项`的Logistic回归模型，即`Ridge`模型，采用**坐标下降**进行参数估计，后面会加入更多优化方法


`Ridge`回归支持：
- 二分类问题


* * *

### 3.1 初始化

|             |     名称      |     类型     |              描述               |
|------------:|:-------------:|:------------:|:-------------------------------:|
| Parameters: |      tol      |    float     |            误差容忍度            |
|             |     step      | float, (0,1] |           梯度下降步长           |
|             |   threshold   | float,(0,1)  | 分类阈值，大于该值为1，小于该值为0 |
|             | has_intercept |     bool     |          是否含有截距项          |
|             |      lamb         |    float          |                    正则项系数             |


### 3.2 类方法

1 拟合

```python
def fit(self, x, y)
```

拟合特征

|             | 名称 |    类型     |     描述      |
|------------:|:----:|:----------:|:------------:|
| Parameters: |  x   | np.2darray |     训练集特征      |
|             |  y   |  np.array  | 训练集标签 |
|    Returns: |      |    Void    |              |


2 预测

```python
def predict(self, x)
```


给定测试集特征x，进行预测

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|    Returns: |      |  np.array  | 预测的结果 |

3 结果评价

```python
def score(self, x, y)
```

拟合并进行预测，最后给出预测效果的得分


|             | 名称 |    类型     |                            描述                            |
|------------:|:----:|:----------:|:---------------------------------------------------------:|
| Parameters: |  x   | np.2darray |                         测试集特征                         |
|             |  y   |  np.array  |                         测试集标签                         |
|    Returns: |      |   float    | 预测结果评分，此处给出F1值 |

4 分类作图

`logistic`模块提供了直接绘制分类效果图的方法，如果维度大于2，则通过PCA降至两维

```python
def classify_plot(self, x, y, title="")
```

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|             |  y   |  np.array  | 测试集标签 |
|    Returns: |      |    Void    |           |

5 概率预测

```python
def predict_prob(self, x)
```

给定测试集特征x，对其正负类的概率进行预测

|             | 名称 |       类型       |             描述              |
|------------:|:----:|:---------------:|:----------------------------:|
| Parameters: |  x   |   np.2darray    |          测试集特征           |
|    Returns: |      | np.array(float) | 预测的结果，表示为正类(1)的概率 |

6 ROC曲线绘制

针对二分类且可以包含
`predict_prob`方法的模型，我们均给出了ROC曲线的绘制方法`auc_plot`，并且在图中输出AUC值

```python
def auc_plot(self, x, y)
```

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|             |  y   |  np.array  | 测试集标签 |


### 3.3 类属性

|     名称      |    类型    |         描述          |
|:-------------:|:----------:|:---------------------:|
| weight |   np.array(float)   | 每个特征的参数 |


## 四、多元线性回归 (MultiRegression)

```python
from simple_ml.regression import MultiRegression

class MultiRegression(BaseClassifier):

    def __init__(self, has_intercept=False):
        super(MultiRegression, self).__init__()
        self.has_intercept = has_intercept
```

`simple_ml` 提供了一般的多元线性回归模型`MultiRegression`


`MultiRegression`回归支持：
- 一般回归问题
- 加权回归问题


* * *

### 4.1 初始化

|             |     名称      |     类型     |              描述               |
|------------:|:-------------:|:------------:|:-------------------------------:|
| Parameters:            | has_intercept |     bool     |          是否含有截距项          |



### 4.2 类方法

1 拟合

```python
def fit(self, x, y, weight=None)
```

拟合特征

|             | 名称 |    类型     |     描述      |
|------------:|:----:|:----------:|:------------:|
| Parameters: |  x   | np.2darray |     训练集特征      |
|             |  y   |  np.array  | 训练集标签  |
|              |  weight| np.array |   训练集样本权重（长度必须等于样本数）       |
|    Returns: |      |    Void    |              |


2 预测

```python
def predict(self, x, weight=None)
```


给定测试集特征x，进行预测

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|              |  weight| np.array |   测试集样本权重（长度必须等于样本数）       |
|    Returns: |      |  np.array  | 预测的结果 |

3 结果评价

```python
def score(self, x, y, weight=None)
```

拟合并进行预测，最后给出预测效果的得分


|             | 名称 |    类型     |                            描述                            |
|------------:|:----:|:----------:|:---------------------------------------------------------:|
| Parameters: |  x   | np.2darray |                         测试集特征                         |
|             |  y   |  np.array  |                         测试集标签                         |
|              |  weight| np.array |   测试集样本权重（长度必须等于样本数）       |
|    Returns: |      |   float    | 预测结果评分，此处给出F1值 |

4 回归作图

绘制回归图

```python
def regression_plot(self, x, weight=None)
```

|             | 名称 |    类型     |    描述    |
|------------:|:----:|:----------:|:---------:|
| Parameters: |  x   | np.2darray | 测试集特征 |
|             |  weight   |  np.array  | 测试集权重 |
|    Returns: |      |    Void    |           |


### 4.3 成员属性

|     名称      |    类型    |         描述          |
|:-------------:|:----------:|:---------------------:|
| beta | np.array | 每个特征的参数 |
| r_square | float | 解释平方和 |


## Examples

```python
from simple_ml.logistic import *
from simple_ml.classify_data import get_iris, get_wine
from simple_ml.data_handle import train_test_split


x, y = get_wine()
x = x[(y==0)|(y==1)]
y = y[(y==0)|(y==1)]
x_train, y_train, x_test, y_test = train_test_split(x, y, 0.5, 918)

logistic = LogisticRegression(has_intercept=True)
logistic.fit(x_train, y_train)
print(logistic.w)
logistic.classify_plot(x_test, y_test)
logistic.auc_plot(x_test, y_test)

lasso = Lasso()
lasso.fit(x_train, y_train)
print(lasso.w)
lasso.classify_plot(x_test, y_test)
lasso.auc_plot(x_test, y_test)

ridge = Ridge()
ridge.fit(x_train, y_train)
print(ridge.w)
ridge.classify_plot(x_test, y_test)
ridge.auc_plot(x_test, y_test)
```

# [返回主页](../index.md)

