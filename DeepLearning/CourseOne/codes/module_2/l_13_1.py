# -*- coding: utf-8 -*-

import tensorflow as tf

# 查看 Eager Execution 的状态
tf.executing_eagerly()
output: True
x = [[2.]]
m = tf.matmul(x, x)
print("x * x is ,  {}".format(m))
# output:
# x * x is ,  Tensor("MatMul_1:0", shape=(1, 1), dtype=float32)

# 手动关闭 Eager Execution
# tf.compat.v2.disable_eager_Execution()
# tf.compat.v2.executing_eagerly()
tf.executing_eagerly()
# output: Fasle
x = [[2.]]
m = tf.matmul(x, x)
print("x * x is ,  {}".format(m))
# x * x is ,  Tensor("MatMul_2:0", shape=(1, 1), dtype=float32)

with tf.compat.v1.Session() as sess:
    print("x * x is, {}".format(sess.run(m)))
# output:
# x * x is, [[4.]]
