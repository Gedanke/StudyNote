# -*- coding: utf-8 -*-

import numpy
import random
import matplotlib.pyplot as plt

numpy.random.seed(123)
w_real = 2
b_real = -15
xlim = [-15, 15]
x_gen = numpy.random.randint(low=xlim[0], high=xlim[1], size=30)
y_real = w_real * x_gen + b_real
plt.plot(x_gen, y_real, 'bo')
plt.savefig("../../images/module_1/6_7.png")
plt.show()


def sgd(x, y, lr, epochs=1):
    # x 为训练集中的数据
    # y 为训练集中标签
    # lr 学习率
    # epochs 训练 epoch 数

    # 随机初始化 w 与 b
    w = random.random()
    b = random.random()
    for e in range(epochs):
        w_list.append(w)
        b_list.append(b)
        for x_, y_ in zip(x, y):
            w = w - lr * x_ * (w * x_ + b - y_)
            b = b - lr * (w * x_ + b - y_)
    return w, b


# 用于记录 w 与 b 的变化
w_list = []
b_list = []
w, b = sgd(x_gen, y_real, 0.001, epochs=150)
print("w = {:.3f} , b = {:.3f}".format(w, b))
# 输出: w = 2.006 , b = -14.732
