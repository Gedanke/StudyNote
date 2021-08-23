# -*- coding: utf-8 -*-

import tensorflow as tf

# 定义一个常量 tensor
a = tf.constant([[1, 2],
                 [3, 4]])
print(a)
# output:
# tf.Tensor(
# [[1 2]
#  [3 4]], shape=(2, 2), dtype=int32)

import numpy as np

# 将 a 作为参数传入 numpy 的方法
b = np.multiply(a, a)
print(b)
# output:
# [[ 1  4]
#  [ 9 16]]

# 将 tensor 的值以 numpy array 的形式返回:
print(a.numpy())


# output:
# array([[1, 2],
#        [3, 4]], dtype=int32)

def dynamic_control(num):
    if num.numpy() == 1:
        print("num is 1.")
    else:
        print(num)


dynamic_control(tf.convert_to_tensor(1))
dynamic_control(tf.convert_to_tensor(3))
# output:
# num is 1.
# tf.Tensor(3, shape=(), dtype=int32)
