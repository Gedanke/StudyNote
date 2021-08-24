# 图像分类: 实现你的第一个图像分类实战项目

上一讲中学习了 3 个图像分类中经典的卷积神经网络，今天要从实战的角度学习图像分类相关的知识。我们要做 2 件事: 

* 了解 AlexNet
* 搭建一个 AlexNet 的训练框架

---
---

## AlexNet

AlexNet 的提出可以说是具有里程碑的意义，在 ImageNet 分类比赛中它将 Top-5 的错误率降低到了 16.40，取得了巨大的进步。我们可以从下图中看到它的贡献: 



图 1: 历年来 ImageNet 上 Top-5 的错误率

虽然在当时 AlexNet 取得了卓越的成就，但随着深度学习技术的不断发展，AlexNet 很少会被用在实际中了。尽管很少被使用，但 Alex 的结构相对简单，非常适合入门学习。因此，我们就从它入手。

---

## AlexNet 特点

AlexNet 的特点现在看起来很普通，但它在当时具有里程碑式的意义: 

* 使用了 Relu 激活函数，而没有使用 Sigmoid 函数，解决了网络层数较深时产生的梯度弥散问题
* 为了防止过拟合，采用了 Dropout 与数据增强
* 采用多 GPU 训练(现在的深度学习框架都支持多 GPU 训练了)
* 提出了 LRN(Local Response Normalization)局部响应值归一化

以上 4 点就是 AlexNet 的主要特点。现在看看，是不是你已经掌握了其中大部分的内容了？

LRN 的目的是增强模型的泛化能力，使响应较大的值变得更大，并抑制反馈较小的神经元。

虽然 AlexNet 的论文中说 LRN 会提高模型性能，但在后续的一些经典卷积神经网络中几乎没有被使用过。VGG 论文的作者在其论文中也提到，LRN 没有起到提升网络性性能的作用，反而消耗了过多的内存。

---

## AlexNet 的网络结构

AlexNet 一共有 8 层，分为 5 层卷积层与 3 层全连接层，如下图所示: 



图 2: AlexNet 的网络结构

因为 AlexNet 采用 2 个 GPU 训练，所以网络分为上下结构。以现在的技术来说，我们不会再采用这种方式训练，因为深度学习框架为我们提供了多 GPU 的训练方式。所以，今天我只搭建 AlexNet 的一部分。为了能快速实验，我也减少了每一层的卷积核的数目。

我搭建的 AlexNet 结构如下: 

```python
layers.Conv2D(48, kernel_size=(5, 5), strides=(1,1), activation='relu'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
# Layer 2
layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
# Layer 3
layers.Conv2D(192, kernel_size=(3, 3), activation='relu'),
# Layer 4
layers.Conv2D(192, kernel_size=(3, 3), activation='relu'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
# Layer 5
layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
#Layer 6
layers.Dense(4096),
# Layer 7
layers.Dense(4096),
# Layer 8
layers.Dense(10, activation='softmax')
```

---

## 训练 AlexNet

我要在 CIFAR-10 上训练一个 AlexNet。

在 [14 | 工作机制与流程: 通过手写识别深入了解 TensorFlow](../module_2/lecture_14.md) 中，我讲过模型训练的 4 个基本要素。

* 数据: 主要是训练集与评估集，用来训练与评估我们的模型
* 网络结构: 也就是我们模型的主体
* 损失函数: 更新模型参数的核心
* 优化方法: 更新模型参数的方法

今天我们依然要从这 4 个方面出发，构建一个 AlexNet 的训练框架。不过这次稍有不同: 首先，我会更加侧重一下有关数据部分的操作；其余的部分我也不会采用低级 API，而是采用 Tensorflow 更推荐的高级 API 来实现。

话不多说，我们先来看看 CIFAR-10 数据。

---

### CIFAR-10 数据

CIFAR-10 数据集一共由 60000 张图片构成，共 10 个类别，每一类包含 6000 图片，每张图片都是 32x32 的 RGB 图片。其中 50000 张图片作为训练集，10000 张图片作为测试集。



图 3: CIFAR-10 数据集

CIFAR-10 已经是非常接近真实数据的数据集了。

---

### 数据加载的 Pipline

我们训练的时候会采用 GPU 来进行硬件加速，但是数据读取部分的操作是在 CPU 上进行的。Tensorflow 为我们提供了一个 tf.data 模块，它帮助我们快速构建相关数据的 Pipline，加快了数据读取、处理的速度。

在 ```tf.data``` 中我们会经常使用到 ```tf.data.Dataset``` 模块。Dataset 代表了一个序列的元素，其中每个元素又包含 1 个或者多个子元素。举个例子: 在图像分类中，训练集就是 1 个 Dataset，训练集是 1 个由图片和对应标签组成的序列，这个序列中的每个元素是图片与标签，元素中又有子元素，子元素是图像、标签。

我们要创建一个 Pipline，首先需要 1 个数据源。数据源可以来自 Numpy 数组，也可以来自 TFRecord 文件、CSV 文件等地方。

我们来看一个最简单的 Dataset 构建方法: 使用 ```from_tensor_slices``` 从 Numpy 数组中构建 Dataset。

请看下面的代码: 

````python
import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
y_train = tf.one_hot(y_train, depth=10)
y_test = tf.one_hot(y_test, depth=10) # [10k, 10]
print('datasets:', x_train.shape, y_train.shape, x_test.shape, y_test.shape, x_train.min(), x_train.max())
train_set = tf.data.Dataset.from_tensor_slices((x_train, y_train))
test_set = tf.data.Dataset.from_tensor_slices((x_test, y_test))
# output:
# datasets: (50000, 32, 32, 3) (50000, 1, 10) (10000, 32, 32, 3) (10000, 1, 10) 0 255
````

我们通过这段代码将 CIFAR-10 的数据通过 from_tensor_slices 从 Numpy 数组中创建一个 Dataset。

构建了一个 Dataset 之后，我们来了解一下其中几个常用的函数，它们分别是 ```batch()、map()、shuffle()``` 和 ```repeat()```。

---

#### batch()

设定 Dataset 读取数据的 batch size。使用方式如下: 

```python
dataset = dataset.batch(64)
```

---

#### map()

map 的作用是让 Dataset 中的每一个元素都执行 map_func ，通常是预处理操作。map 函数定义如下: 

```python
map(
    map_func, num_parallel_calls=None, deterministic=None
)
```

```num_parallel_calls``` 是让 map 使用多线程方式。deterministic 可以设定是否需要保证原有的顺序，设定为 False时会提升 map 的性能。

map 的使用例子如下: 

```python
def preprocess(x, y):
	    # [0~255] => [-1~1]
	    x = 2 * tf.cast(x, dtype=tf.float32) / 255. - 1.
	    y = tf.cast(y, dtype=tf.int32)
	    return x,y
dataset = dataset.map(preprocess)
```

---

#### shuffle()

顾名思义，会按照 ```buffer_size``` 对 Dataset 进行 shuffle。```buffer_size``` 的大小最好大于整个数据集的数据量。```shuffle``` 函数定义如下: 

```python
shuffle(
    buffer_size, seed=None, reshuffle_each_iteration=None
)
```

```reshuffle_each_iteration``` 是指每个 Epoch 中 shuffle 的顺序是否应该不一样。

Shuffle 的使用例子如下: 

```python
dataset = dataset.shuffle(3, reshuffle_each_iteration=True)
```

---

#### repeat()

repeat 的作用是重复 Dataset 多少次，定义如下: 

```python
repeat(
    count=None
)
```

如果 count 为 None 或者 -1 的时候，Dataset 将无限重复下去。

在我们的项目中，对训练集做如下处理: 

```python
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32) / 255.
    y = tf.cast(y, dtype=tf.int32)
    return x,y
batch_size = 128
train_set = train_set.map(preprocess).shuffle(10000).batch(batch_size)
test_set = test_set.map(preprocess).batch(batch_size)
```

创建好 Dataset 之后，我们就要消费数据了。

Tensorflow 2 之后，默认是 Eager 模式，Session 与 placeholder 被弃用，读取数据的方式变得非常简单。使用 Python 内置的 iter 就可以了，如下所示: 

```python
iterator = iter(dataset)
while True:
    try:
        image, _ = next(iterator)
        ....
    except StopIteration:
        print("iterator done")
        break
```

当然，更加常用的方式是直接将 Dataset 作为参数传入 fit 方法中。

---

### 模型搭建与训练

模型搭建我采用的是 Tensorflow 中的高级 ```API-tf.keras```。有关 keras 的介绍你同样可以在 [14 | 工作机制与流程: 通过手写识别深入了解 TensorFlow](../module_2/lecture_14.md) 中复习一下。tf.keras 保持 Tensorlfow 原有优点的同时，让 Tensorflow 变得更加易用。

在我们要搭建的 AlexNet 中，会涉及卷积层、最大池化层与全连接层，我们就依次看看 ```tf.kerase``` 中的这三个层。与层相关的内容都封装在 ```tf.keras.layers``` 模块中。

---

#### Conv2D

Conv2D 的定义如下: 

```python
tf.keras.layers.Conv2D(
    filters, kernel_size, strides=(1, 1), padding='valid', data_format=None,
    dilation_rate=(1, 1), groups=1, activation=None, use_bias=True,
    kernel_initializer='glorot_uniform', bias_initializer='zeros',
    kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None,
    kernel_constraint=None, bias_constraint=None, **kwargs
)
```

其中大部分参数我在之前已经介绍过了，相信从它们的名字你也能看出它们的作用，这里我就不赘述了。

我们重点来看一下 group 这个参数。通过指定 group 参数，我们可以将输入的特征图按通道方向划分为 group 个组，每个组被不同的 fiters/groups 个卷积进行卷积。在输出中，不同组的输出会拼接在一起然后输出。

---

#### MaxPool2D

max polling 操作的定义如下: 

```python
tf.keras.layers.MaxPool2D(
    pool_size=(2, 2), strides=None, padding='valid', data_format=None, **kwargs
)
```

想必你现在对它也不陌生了，这里我就先省略了。

---

#### Desne

我们在使用低级 API 构建网络的时候曾说过，低级 API 中不包含全连接层。在 ```tf.keras``` 中，Tensorflow 为我们提供了全连接层，即 ```tf.keras.layers.Dense```。

Dense 定义如下: 

```python
tf.keras.layers.Dense(
    units, activation=None, use_bias=True, kernel_initializer='glorot_uniform',
    bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None,
    activity_regularizer=None, kernel_constraint=None, bias_constraint=None,
    **kwargs
)
```

units 是全连接层中神经元的个数，其余参数的作用正如它们名字显示的那样。

现在我们已经知道了每一层的定义方式，那么如何将它们组装在一起呢？

```tf.keras``` 提供了一种叫作 Sequential 的模型组装方式，用这种方式创建的模型叫作"顺序模型"，因为这种方式构建的模型就是按照层的顺序，一层一层堆叠起来的。

使用方式非常简单，通过下面的代码，就可以将我们之前介绍的 AlexNet 搭建起来。

```python
model = tf.keras.Sequential(
[
# Layer 1
layers.Conv2D(24, kernel_size=(5, 5), strides=(1,1), activation='relu', kernel_initializer='he_uniform', padding='same'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
# Layer 2
layers.Conv2D(64, kernel_size=(3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
# Layer 3
layers.Conv2D(128, kernel_size=(3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'),
# Layer 4
layers.Conv2D(64, kernel_size=(3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
# Layer 5
layers.Conv2D(64, kernel_size=(3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'),
layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
# 需要对全连接层的输入进行铺平处理
layers.Flatten(),
#Layer 6
layers.Dense(4096),
# Layer 7
layers.Dense(4096),
# Layer 8
layers.Dense(10, activation='softmax')
]
)
```

对于顺序模型我们还可以这样创建: 

```python
model = tf.keras.Sequential()
model.add(layers.Conv2D(...))
...
model.add(layers.Dense(10))
```

---

#### 优化方法与损失函数

创建好模型之后还要对模型进行编译，编译时会指定优化方法与损失函数。请看下面的例子: 

```python
model.compile(
    optimizer=tf.keras.optimizers.SGD(0.001), 
    loss=tf.losses.CategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)
```

优化方法使用封装在 ```tf.keras.optimizers``` 模块中的类，有 Adam、SGD 等。

损失函数封装在 ```tf.keras.losses``` 模块中，根据问题的不同你可以查找需要的损失函数。

metrics 用来设定模型的评价函数。

在我们的项目中，采用的是 SGD 优化函数、交叉熵损失函数，并采用精确率来评价模型。

---

#### 训练

编译之后我们就可以开始训练模型了。训练时需要指定训练集、验证集、训练的 Epoch 数。如代码所示: 

```shell
model.fit(train_set, epochs=5, validation_data=test_set)
output:
391/391 [==============================] - 8s 20ms/step - loss: 2.2427 - accuracy: 0.1885 - val_loss: 2.1569 - val_accuracy: 0.2704
Epoch 2/3
391/391 [==============================] - 9s 22ms/step - loss: 2.0377 - accuracy: 0.2835 - val_loss: 1.9392 - val_accuracy: 0.3223
Epoch 3/3
391/391 [==============================] - 9s 23ms/step - loss: 1.8864 - accuracy: 0.3302 - val_loss: 1.8301 - val_accuracy: 0.3542
```

训练时会将训练过程中的信息打印出来。

---

### 函数式 API

在这里我要向你介绍 tf.keras 中另外一种构建模型的方式。

刚才介绍的顺序模型使用起来也中规中矩，可以应对绝大多数问题，但在实际应用中可能会遇到更加复杂的问题，例如模型有多个输入、共享中间变量。此时就需要用到 ```tf.keras``` 为我们提供的另一种更加灵活的模型搭建方式，函数式 API。函数式 API 中的层可以像函数一样被调用，且输入输出均为 tensor。

为了简单明了，我将上述的 AlexNet 缩减到如下结构，请看代码: 

```python
# 首先创建一个输入层
inputs = tf.keras.Input(shape=(32, 32, 3))
x = layers.Conv2D(64, (3, 3), activation='relu')(inputs)
x = layers.Flatten()(x)
x = layers.Dense(128, activation='relu')(x)
# 输出层
output = layers.Dense(10, activation='softmax')(x)
```

与顺序模型不同的地方是，定义完网络结构之后，需要创建一个模型，指定模型的输入输出。

```python
model = tf.keras.Model(inputs=inputs, outputs=output)
```

其余部分就一样了。函数式 API搭建的模型同样需要编译，然后执行 fit 就可以开始训练了。

---

### 回调函数

最后再介绍一下回调函数。回调函数可以让我们在训练的过程中做一些事情，例如: 定期保存模型、提前终止训练、改变学习率。

回调函数可以在每个 Epoch 的开始或者结束、每个 batch 的开始或者结束执行。

下面是几个常用的内置回调函数。

* EarlyStopping:  当被监控指标在设定的若干个 epoch 后没有提升，则提前终止训练
* TensorBoard:  保存 TensorBoard 信息
* ModelCheckpoint:  定期保存模型
* TerminateOnNaN: 如果遇到 loss 为 NaN，则终止训练

请看下面这个例子，我们在训练代码中定义如下几个回调函数: 

```python
callbacks = [
# 如果验证集上的损失 val_accuracy 连续 2 个 epoch 没有变化，则终止训练
tf.keras.callbacks.EarlyStopping(patience=2, monitor='val_accuracy'),
# 将 TensorBoard 信息保存到'./logs'目录中
tf.keras.callbacks.TensorBoard(log_dir='./logs'),
# 每个 Epoch 之后保存一个模型
tf.keras.callbacks.ModelCheckpoint(filepath='./models/weights.{epoch:02d}.hdf5',save_freq='epoch')
]
```

定义好需要的回调函数之后，只需在 fit 函数中传入即可。

```python
model.fit(train_set, epochs=30, validation_data=test_set, callbacks=callbacks)
```

这时，Tensorboard 的信息回报存在 ```./logs``` 目录下，每个 epoch 之后模型会保存在 models 目录下面。

---

## 结语

这一讲中我们通过训练一个缩减版的 AlexNet 完成了图像分类的项目的训练环节。虽然 AlexNet 网络结构简单，但整体流程大致是相同的。如果你在实际中遇到了较为复杂的问题，只需要将网络结构更换成 VGG、ResNet 等经典网络结构即可。

那么，在最后给你留一个小练习: 你可以将我们在顺序模型中的网络结构改为函数式 API 的网络结构吗？

下一讲，我将带你进入到图像分割算法的学习。图像分割是深度学习中另一个重要的应用场景，算法的复杂度要比图像分类更加复杂一些，你做好准备了吗？

---
---

