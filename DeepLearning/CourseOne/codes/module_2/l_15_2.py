# -*- coding: utf-8 -*-

import tensorflow as tf
import random
import tensorboard
import datetime

# 这里，我们首先生成一个 tf.summary 的记录文件。
log_dir = "./log/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
summary_writer = tf.summary.create_file_writer(log_dir)
# 假设我们有一些二维坐标点，我们以函数 y=0.1x^2-4x+1 为例，此外，为了引入类似模型波动的效果，我们在 y 上乘一个 0.9～1 的随机数。
xs = list(range(100))
ys = [(0.1 * x * x - 4 * x + 1) * random.randint(90, 100) / 100 for x in xs]
# 任意一个二维坐标点，我们只需要使用 tf.summary.scalar，就可以记录该信息。
for i, j in zip(xs, ys):
    with summary_writer.as_default():
        tf.summary.scalar('fake_index', j, step=i)
summary_writer.close()
