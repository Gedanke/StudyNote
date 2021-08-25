# -*- coding: utf-8 -*-

import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
y_train = tf.one_hot(y_train, depth=10)
y_test = tf.one_hot(y_test, depth=10)  # [10k, 10]
print('datasets:', x_train.shape, y_train.shape, x_test.shape, y_test.shape, x_train.min(), x_train.max())
train_set = tf.data.Dataset.from_tensor_slices((x_train, y_train))
test_set = tf.data.Dataset.from_tensor_slices((x_test, y_test))


# output:
# datasets: (50000, 32, 32, 3) (50000, 1, 10) (10000, 32, 32, 3) (10000, 1, 10) 0 255

def preprocess(x, y):
    # [0~255] => [-1~1]
    x = 2 * tf.cast(x, dtype=tf.float32) / 255. - 1.
    y = tf.cast(y, dtype=tf.int32)
    return x, y
