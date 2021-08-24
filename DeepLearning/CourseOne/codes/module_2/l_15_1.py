# -*- coding: utf-8 -*-

import tensorflow as tf
import tensorboard
import datetime
import numpy as np

# 加载 mnist 数据
mnist = tf.keras.datasets.mnist
# 将数据进行切分，分为训练集和验证集
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 还记得为什么要除以 255 么
x_train, x_test = x_train / 255.0, x_test / 255.0


# 构建一个简单的模型，拍平--全连接--dropout--全链接
def create_model():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])


model = create_model()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 定义日志目录，这里需要注意的是，它必须是启动 Web 应用时指定目录的子目录
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
model.fit(
    x=x_train,
    y=y_train,
    epochs=5,
    validation_data=(x_test, y_test),
    callbacks=[tensorboard_callback]
)

(x_train, y_train), (x_test, y_test) = mnist.load_data()
log_dir = "./logss/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
summary_writer = tf.summary.create_file_writer(log_dir)
img = np.reshape(x_train[0], (-1, 28, 28, 1))

text = 'tenboard is so cool!'
with summary_writer.as_default():
    tf.summary.image("Training image data", img, step=1)
    tf.summary.text('fake_text', tf.convert_to_tensor(text), step=1)
