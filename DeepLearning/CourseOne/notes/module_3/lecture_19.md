# 语义分割: 打造简单高效的人像分割模型

上一讲介绍了语义分割的原理。在理解上一课时中 U-Net 语义分割网络的基础上，这一讲，让我们来实际构建一个人像分割模型吧。

---
---

## 语义分割的评估

先简单回顾一下语义分割的目的: 把一张图中的每一个像素进行预测，并将它们分成对应的类别。如下图所示:

![](../../images/module_3/19_1.png)

你可能注意到，在图中有一个新的概念 Ground Truth(GT)，它在目标检测与语义分割项目中十分常见。其实 GT 实际的表现形式就是我们下面会讲到的 mask。

GT 也就是真实的类别、真实的结果，在语义分割中指每个像素真实的类别，这些类别是我们人工标记好的。所以在语义分割任务中，我们希望模型的输出(Prediction)，能够尽可能高精度地与 GT 重合。

那如何衡量这种重合程度呢？

在图像分割中，会采用一个新的指标来衡量模型分割的好坏，我们把它叫作 IoU(Intersection over Union，交并比)，用来衡量重合程度的高低。

关于 IoU 的计算过程也很简单，我们来看一个例子:

```python
# 为了易于理解，我们先定义几个方法
def count(area):
    """
    返回给定区域元素的个数
    """
    return area
    的元素个数


def intersection(area1, area2):
    """
    返回 area1 与 area2 的交集
    """
    return area1
    与
    area2
    的交集


def union(area1, area2):
    """
    返回 area1 与 area2 的并集
    """
    return area1
    与
    area2
    的并集


IoU = intersection(GT, Prediction) / union(GT, Prediction)
```

案例中 IoU 的取值范围是 0~1，其中 0 代表预测部分完全没有覆盖到真实区域，1 代表我们的预测完美地覆盖到了真实区域。

利用下面的例子，我们来可视化地了解一下 IoU 是如何计算。下图左边是 GT，右边是我们模型的预测结果。

![](../../images/module_3/19_2.png)

分子是 GT 与预测结果的交集(下图左边的图片)，分母是 GT 与预测结果的并集(下面右边的图片)，用分子除以分母就是我们需要的 IoU，即 Intersection / Union。

![](../../images/module_3/19_3.png)

我们可以使用 NumPy 编写一段 IoU 的计算程序:

```python
intersection = np.logical_and(target, prediction)
union = np.logical_or(target, prediction)
iou_score = np.sum(intersection) / np.sum(union)
```

在评价过程中，每个类别都会有一个 IoU。IoU 是语义分割中经常采用的一种评价方式，无论是论文还是各种比赛里都会看到。也许你会好奇，为什么不使用像素的精确度来衡量语义分割模型呢？

其实也不是不可以，只不过在类别严重不平衡的时候，像素的精确度会严重误导我们，无法客观有效地评价模型。

假设有如下场景:

* 一张图片有 100 个像素
* 只有背景与类别 A，且类别 A 的 GT 的像素个数为 5
* 模型将整张图片都预测为背景

具体如下图所示:

![](../../images/module_3/19_4.png)

在这个假设的场景下，模型将整张图片都预测为背景，也就是在这张图中，模型有 5 个像素预测错了，那此时模型像素的精确度为:

```python
accuracy = 95 / 100 = 0.95
```

显然，在这个类别严重不平衡的场景下，用 95% 的精准度来衡量我们的模型是不合理的。

我们希望模型能更好地分割出类别 A。但在这个场景中，我们的模型没有做到这一点，同时还有一个很高的精确度，这个精确度并不能反映出模型的实际情况。

为了避免这种情况，有时候我们会使用所有类别的 IoU 的均值来综合衡量当前模型，我们把这个均值称为 mean IoU，简称 mIoU。mIoU 会通过所有类别的 IoU
的均值来综合衡量当前模型，这样得到的数据也能更准确地反映模型的实际情况。

我们来看类别 A 的 IoU 以及模型的 mIoU 分别是多少。

```python
类别
A
的
IoU:
IoU_A = intersection(GT_A, Prediction_A) / union(GT_A, Prediction_A)
= 0 / (5 + 0 - 0) = 0
背景的
IoU:
IoU_BG = intersection(GT_BG, Prediction_BG) / union(GT_BG, Prediction_BG)
= 95 / (95 + 100 - 95) = 0.95
mIoU = (IoU_A + IoU_BG) / 2 = (0 + 0.95) = 0.475
```

通过计算可以发现，类别 A 的 IoU 是 0%，模型的 mIoU 是 47.5%。

虽然模型的性能依然很差，无法很好地分割类别 A，但它的评估指标也不是很高。相比 95%的精确度，mIoU 的 47.5% 显然更加客观、合理。你可以根据 mIoU 反映的情况查看是哪里出了问题，然后进一步提升模型的性能。

从这一简单的场景中能很明显地看到，在数据量严重不平衡的时候，像素的精确度是无法衡量我们的模型的。模型如果将所有的像素都预测为背景，模型的精确度再高都没有用。所以，mIoU 是我们在语义分割中经常使用的一个指标。

---

## 语义分割网络的训练

在介绍"如何训练语义分割网络"前，我要引入一个概念 mask 图片。mask 图片一般是一张单通道的图片，里面的数值标记对应图片在相同位置的像素类别。

以人像分割举例，我们的目的是把一张图片中的人像与背景分割出来。那么人像的像素在 mask 中对应的位置就是 1，背景就是 0。

1 代表人像这个类别，0 代表背景这个类别。

当然，根据项目的不同，数值是可以任意取的。

刚才讲到的 GT 与语义分割模型的最终的输出都是一个 mask。不过对于 GT 的 mask，我们经常会省略 mask，直接叫 GT。

在训练语义分割模型的时候，训练数据一般包含 2 个文件夹。

* JPEGImages文件夹: 存放原图
* SementationClass文件夹: 存放 GT 的 mask 图片

以上 2 个文件夹的名字并没有硬性要求，举例的只是较为常用的名字。

以下 2 张图片分别是原图与 mask 图片:

![](../../images/module_3/19_5.png)

![](../../images/module_3/19_6.png)

为什么需要 mask 图片呢？

机器学习或者说深度学习的目标就是让机器像人一样思考，但机器怎么像人一样思考呢？答案是人来教机器如何思考。

在 [16 | 图像分类: 技术背景与常用模型解析](lecture_16.md)
中，我们学习了图像分类模型的训练方式。图像分类模型最初所有的参数都是随机初始化的，所以我们要把训练数据中的图片提前分好类，然后在训练时，通过不断地前向/后向传播来降低 loss(也就是让我们预测的类别无限的接近真实的类别)
，从而更新网络参数。这个真实的类别需要我们事先人工分好。

例如我们要训练一个模型来分类猫和狗，那么在训练前，我们要把狗的图片放到 dog 文件夹里，猫的图片放到 cat 文件夹里。在训练的时候，模型会读取对应类别文件夹的数据进行训练。

![](../../images/module_3/19_7.png)

那么在语义分割中，应该如何训练呢？

语义分割的目的是把每一个像素都分成相应的类别，但是我们又怎么把图像中的像素，像图片那样提前分好类别呢？

在语义分割中我们首先要定义模型的目标，即 GT，告诉模型每张图片每个像素所属的类别。在训练过程中，模型会不断更新参数来减小 loss。这样，我们就可以获得一个语义分割的模型了。

---

## 图片标记工具

在这里我要向你介绍一下如何标记语义分割的数据(图片)，生成 GT。

好的数据集是获得一个高精度模型的第一步，尤其是在我们的语义分割任务中。现在有很多公开的数据集可以用，例如 COCO Person、VOC
Person、Supervisely。但是这些公开数据中，有些数据可能并不适合我们的场景，并且标记的质量不是很高。

我们可以下载开源的人像数据集: [Supervisely Dataset](https://supervise.ly/explore/projects/supervisely-person-dataset-23304/datasets)(
需要自己注册账号)与 [AISegment](https://github.com/aisegmentcn/matting_human_datasets) 。你可以分别点击链接获取。

* Supervisely Dataset: 一共有 5711 张图片，图片标记质量高，包含多人的图片
* AISegment: 目前最大的公开数据集，包含 34427 张高质量的标注图片。用这部分数据训练的模型已经投入商用

为了提高模型的健壮性与精度，我们经常需要收集一些符合我们应用场景的图片，然后将其标记。

我们标记的工具叫作Labelme，安装地址为 [https://github.com/wkentaro/labelme](https://github.com/wkentaro/labelme)

标记共分为 6 个步骤。

(1) 将需要标记的图片放入一个文件夹。

(2) 准备一个 labels.txt 文件，内容是需要标记类别的名字。

因为是人像分割任务，所以 labels.txt 的内容是 _background_ 与 person 就可以了，每一类占用一行，如下所示:

```shell
_background_
person
```

(3) 在命令行中输入以下代码:

```shell
labelme --labels labels.txt --nodata
```

然后会出现一个界面:

![](../../images/module_3/19_8.png)

(4) 点击 open dir，选择第一步中的文件夹，将需要标记的图片导入进来。

![](../../images/module_3/19_9.png)

(5) 点击 Create Polygons，把需要标记的每一类都框起来。

在人像分割任务中，你需要把图中的人物沿着人物的轮廓标记出来。需要注意的是，标记的时候起点和终点必须是同一个地方。在标记完成之后，从弹出的对话框中选择对应的类别。如图所示:

![](../../images/module_3/19_10.png)

每编辑完一张图，点击 save，就会自动生成一张同名的 json 文件。

(6) 在命令行中执行下面的命令，就可以将标记好的图片转换为一张 mask 图片。

```shell
labelme_json_to_dataset json 文件名
```

执行完上述的命令之后，会生成下面的文件，其中 label.png 就是我们所需要的 GT 的 mask。

![](../../images/module_3/19_11.png)

到这里，咱们的标记就算完成了。

---

## 视频虚拟背景: 人像分割

这篇文章写于 2020 年，这一年对所有人来说都是不平凡的一年。突如其来的疫情席卷了全球，在家办公成了常态。在家使用视频会议时，你肯定接触过虚拟背景这个功能。

所谓人像分割模型，就是把一张图片作为输入，有人的部分作为前景输出。一般，人的部分作为类别 1 输出，而背景则作为类别 0 输出。

接下来，我们就要具体来实现一个 U-Net，用它来训练一个人像分割模型了。我会从以下 4 个方面进行介绍: 数据加载、网络结构定义、层的定义、损失函数。

为什么主要介绍这 4 个方面呢？因为机器学习任务离不开数据加载、计算 loss、更新权重这三大块。其中，权重就是网络结构中的参数，网络结构中的参数又体现于 U-Net 的网络结构与层的定义。

---

### 数据加载

在我们的人像分割项目中，我们要把原图(JPEGImages)的数据读取到一个 NumPy 的数组中，GT(SegementationClass)的数据读取到另一个 NumPy 的数组中，这一过程就是数据加载。

我们先创建一个工作目录，叫 u-net-dev。在 u-net-dev 下面创建一个 data_set 文件夹，用来存放我们的数据。

我从 VOC 数据集中把和人有关的图片都挑选出来了，把数据加载成 NumPy 的数组，提供给模型训练。

![](../../images/module_3/19_12.png)

JPEGImages 文件夹用于存放原图，SegmentationClass 文件夹用于存放对应的 GT。

在工作目录下面创建一个 utils 文件夹，用来存放与本项目有关的一切工具代码，包括 loader.py 和 dataset.py。

* loader.py: 所有和数据相关的代码都会写在 loader.py 文件中
* dataset.py: 定义一个 DataSet 类别，用来抽象我们的数据

完成上面 2 个 py 文件之后，我们只需要在训练时通过下面的 [代码](../../codes/module_3/l_19_1.py) 即可导入训练数据:

```python
import loader as data_loader


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
```

具体的 [loader.py](../../codes/module_3/loader.py) 与 [dataset.py](../../codes/module_3/dataset.py) 的定义，因为代码过长，我将其放在了 GitHub
中，你可以点击相应的链接，我已经写好了注释。

---

### U-Net 网络结构

U-Net 网络结构是我们的重中之重，有了它模型可以知道以何种方式进行前向传播，分割图片，推断出图片中的前景(人像)与背景。我在 [18｜语义分割: 技术背景与算法剖析](lecture_18.md) 向你介绍了 U-Net
的运作原理，这里我们就来看 U-Net 的网络结构。

我把 U-Net 的网络定义命名为 unet.py，也放在 util 文件夹中。

这里我定义的是 1 个输入输出大小均为 256x256 的 U-Net，网络结构和参数与我在"18 课时"中介绍一样。

有关 [unet.py](../../codes/module_3/unet.py) 的定义，你可以点击链接查看。

---

### 层的定义

完成 U-Net 的网络定义之后，我们就算是搭建好了一个模型的主要框架。这个框架中的细节该如何实现呢？方法就是层的定义。接下来我们看一下 U-Net 使用到层的具体实现。

我定义了 U-Net 网络中使用到的一些层与操作。

* conv: 卷积层
* pooling: 池化层
* up_conv: 上采样层
* copy_and_crop: 连接操作

我们把这些层与操作写在 layers.py 文件中，也把它放在 util 中。

有关 [layers.py]() 的定义，我同样放在了 GitHub 中，你可以点击链接查看，我已经写好注释了。

---

### 损失函数

我们的人像分割问题也是分类问题，所以可以使用常见的交叉熵损失函数，一般有 Sigmoid 交叉熵损失函数与 Softmax 交叉熵损失函数:

* Sigmoid 函数可以把一个数值映射到(0, 1)的区间内，所以经常用在二分类任务中
* Softmax 函数可以把一组数中的每个数映射到(0, 1)的区间内，并且和是 1，所以 Softmax 函数经常用于多分类

我们的人像分割模型是一个二分类任务，可以使用上述交叉熵损失函数的任意一种。

接下来，我们就看看该如何定义我们的损失函数以及优化方法吧。我选择的是 Softmax 交叉熵损失函数。当然，你也可以换成 Sigmoid 交叉熵损失。具体代码如下:

```python
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
```

训练中最主要的几个环节我已经讲完了，我们来回顾一下训练流程，把它们串起来。

* 加载数据，生成训练集与验证集(参考 loader.py)
* 设定 batch_size 与 epoch 数，以 batch_size 为单位循环读取训练集
* 利用每个 batch 的数据进行前向传播与反向传播，计算 loss，更新权重
    * 根据我们写好的 u-net 的网络结构进行前向传播，这里会用到 layers.py 中使用到的层
    * loss 我们也已经定义好了
    * 反向传播与更新权重是由我们使用的框架(TensorFlow)来帮助我们完成
* 通过在 [15 | TensorBoard: 实验统计分析助手](../module_2/lecture_15.md) 中学习的 TensorBoard 观察每个 batch 或者每个 epoch 的
  loss，检验我们模型训练是否有问题
* 保存模型
* 评估模型，计算 mIoU

如果 mIoU 的结果越接近 1，那么你建立的人像分割模型就越好。

---

## 结语

恭喜你，你已经可以自己建立一个人像分割模型了。训练模型是一个需要根据结果优化的过程，要想直接建立一个性能非常好的人像分割模型是很难的。

那么，对于人像分割模型，你觉得从哪些方面着手，可以提高模型的精度呢？

下一讲，我将带你了解"文本分类"，这是我们要实现的最后一个应用场景了。

---
---

