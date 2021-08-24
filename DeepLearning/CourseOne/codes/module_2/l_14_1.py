# -*- coding: utf-8 -*-

from keras.datasets import mnist
import numpy as np
import tensorflow as tf
from math import ceil

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
print('train set:', X_train.shape, X_train.dtype, Y_train.shape, Y_train.dtype)
print('test set:', X_test.shape, X_test.dtype, Y_test.shape, Y_test.dtype)
# output:
# train set: (60000, 28, 28) uint8 (60000,) uint8
# test set: (10000, 28, 28) uint8 (10000,) uint8

X_train = np.array(X_train, np.float32)
X_test = np.array(X_test, np.float32)
# 归一化
X_train, X_test = X_train / 255, X_test / 255

batch_size = 128
epoch = 2
# 使用 tf.data API 对数据进行随机排序和批处理
train_set = tf.data.Dataset.from_tensor_slices((X_train, Y_train))
train_set = train_set.repeat(epoch).shuffle(5000).batch(batch_size).prefetch(batch_size)

# MNIST 输入的 tensor
input = tf.Variable(tf.random.normal([1, 28, 28, 1]))
# 3x3 的卷积
filter = tf.Variable(tf.random.normal([3, 3, 1, 32]))
print(input.shape)
output = tf.nn.conv2d(input, filter, strides=[1, 3, 3, 1], padding='SAME')
print(output.shape)
# output:
# (1, 28, 28, 1)
# (1, 10, 10, 32)
filter = tf.Variable(tf.random.normal([3, 3, 1, 32]))
print(input.shape)
output = tf.nn.conv2d(input, filter, strides=[1, 3, 3, 1], padding='VALID')
print(output.shape)


# output:
# (1, 28, 28, 1)
# (1, 9, 9, 32)

def conv(x, W, b, strides=1, activation=tf.nn.relu):
    """
    :param x:
    :param W:
    :param b:
    :param strides:
    :param activation:
    :return:
    """
    # Conv2D 包装器, 带有偏置和 relu 激活
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return activation(x)


def maxpooling(x, k=2):
    """
    :param x:
    :param k:
    :return:
    """
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='SAME')


num_classes = 10
# 随机值生成器初始化权重
random_normal = tf.initializers.RandomNormal()
# 第一层卷积层的权重: 3 * 3 卷积，1 个输入，32 个卷积核
conv_w = tf.Variable(random_normal([3, 3, 1, 32]))
# 第一层卷积层的偏移
conv_b = tf.Variable(tf.zeros([32]))
# fc1: 14*14*32 个输入，1024 个神经元
# 第一个全连接层的权重
fc1_w = tf.Variable(random_normal([14 * 14 * 32, 1024]))
# 第一个全连接层的权重
fc1_b = tf.Variable(tf.zeros([1024]))
# fc2: 1024 个输入，10 个神经元
# 第二个全连接层的权重
fc2_w = tf.Variable(random_normal([1024, num_classes]))
# 第二个全连接层的权重
fc2_b = tf.Variable(tf.zeros([10]))


def net(x):
    """
    :param x:
    :return:
    """
    # 输入形状: [batch_size, 28, 28, 1]
    x = tf.reshape(x, [-1, 28, 28, 1])
    # 输出形状: [batch_size, 28, 28 ,32]
    conv1 = conv(x, conv_w, conv_b)

    # maxpooling 输出形状: [batch_size, 14, 14, 32]
    conv1 = maxpooling(conv1, k=2)
    # 对 conv1 进行 reshape， 输出形状: [batch_size, 14*14*32]
    fc1 = tf.reshape(conv1, [-1, fc1_w.get_shape().as_list()[0]])

    # 全连接层， 输出形状:  [batch_size, 1024]
    fc1 = tf.add(tf.matmul(fc1, fc1_w), fc1_b)
    # 将 ReLU 应用于 fc1 输出以获得非线性
    fc1 = tf.nn.relu(fc1)
    # 全连接层，输出形状 [batch_size, num_classes]
    out = tf.add(tf.matmul(fc1, fc2_w), fc2_b)
    return tf.nn.softmax(out)


def cross_entropy(y_pred, y_true):
    """
    交叉熵损失函数
    :param y_pred:
    :param y_true:
    :return:
    """
    y_true = tf.one_hot(y_true, depth=num_classes)
    # 计算交叉熵
    return tf.math.reduce_mean(-tf.math.reduce_sum(y_true * tf.math.log(y_pred)))


x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x ** 2
# dy = 2x * dx
dy_dx = tape.gradient(y, x)
dy_dx.numpy()


def run_optimization(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    # 将计算封装在 GradientTape 中以实现自动微分
    with tf.GradientTape() as g:
        pred = net(x)
        loss = cross_entropy(pred, y)

    # 要更新的变量，就是网络中需要训练的参数
    trainable_variables = [conv_w, conv_b, fc1_w, fc1_b, fc2_w, fc2_b]
    # 计算梯度
    gradients = g.gradient(loss, trainable_variables)

    # 按 gradients 更新参数
    tf.optimizers.Optimizer.apply_gradients(zip(gradients, trainable_variables))
