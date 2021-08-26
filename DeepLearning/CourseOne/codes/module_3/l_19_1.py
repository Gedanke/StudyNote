# -*- coding: utf-8 -*-

import loader as data_loader
from unet import *


def load_dataset(train_rate):
    """
    按比例将数据分割为训练数据与评估数据

    Args:
    train_rate: 训练数据所占的比例
    Returns:
        训练集、测试集
    """
    loader = data_loader.Loader(dir_original="data_set/JPEGImages",
                                dir_segmented="data_set/SegmentationClass")
    return loader.load_train_test(train_rate=train_rate, shuffle=False)


train, test = load_dataset(train_rate=parser.trainrate)


# 加载数据，刚才已经讲过了
def load_dataset(train_rate):
    loader = ld.Loader(dir_original="data_set/VOCdevkit/person/JPEGImages",
                       dir_segmented="data_set/VOCdevkit/person/SegmentationClass")
    return loader.load_train_test(train_rate=train_rate)


def train():
    # 加载数据
    train, test = load_dataset(train_rate=parser.trainrate)
    # 创建模型
    model = U_Net()
    # 使用 Softmax 交叉熵损失函数以及 Adam 优化方法
    cross_entropy = tf.reduce_mean(tf.nn.Softmax_cross_entropy_with_logits(labels=model.labels, logits=model.predict))
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    with tf.control_dependencies(update_ops):
        train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
