# -*- coding: utf-8 -*-

from sklearn import datasets
# 分割数据的模块，把数据集分为训练集和测试集
from sklearn.model_selection import train_test_split
# 导入回归方法
from sklearn.linear_model import SGDRegressor
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

boston_data = datasets.load_boston()
# sklearn 把数据分为了 data(输入)与 target(输出)两部分
data_X = boston_data.data
data_y = boston_data.target
# 将数据集分割成训练集与测试集，其中测试集占 30%
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.3)

model = SGDRegressor(loss='squared_loss', l1_ratio=0.001, max_iter=2000, verbose=1)
model.fit(X_train, y_train)
print(boston_data.keys())
print(boston_data['DESCR'])

# 加载数据到dataframe中
df = pd.DataFrame(data=boston_data['data'], columns=boston_data['feature_names'])
print(df.head())

# 观察属性间的相关性
df['PRICE'] = boston_data.target
correlation_matrix = df.corr().round(2)
plt.figure(figsize=(10, 10))
sns.heatmap(data=correlation_matrix, annot=True)
plt.savefig("../../images/module_1/6_9.png")
plt.show()

y_predict = model.predict(X_test)
# 使用 mean_squared_error 模块，并输出评估结果。
print('The mean squared error of SGDRegressor is', mean_squared_error(y_test, y_predict))
