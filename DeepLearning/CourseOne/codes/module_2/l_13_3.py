# -*- coding: utf-8 -*-

import tensorflow as tf


# placeholder 是一个占位符，运行 session 时会将对应的值传进去。
# x = tf.placeholder(tf.float32)
# y = tf.placeholder(tf.float32)
# z = x + y
# with tf.Session() as sess:
#     print(sess.run(z, feed_dict={x: 3, y: 4.5}))


# output:
# 7.5

@tf.function
def f(x, y):
    z = x + y
    print('z is', z)
    return z


x = tf.constant(3, dtype=tf.float32)
y = tf.constant(4.5, dtype=tf.float32)
z = f(x, y)
print('z is', z)
# output:
# z is Tensor("add:0", shape=(), dtype=float32)
# z is tf.Tensor(7.5, shape=(), dtype=float32)
