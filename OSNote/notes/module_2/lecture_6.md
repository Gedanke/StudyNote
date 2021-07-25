# 目录结构和文件管理指令: rm -rf 指令的作用

本节通过一道常见题，引出本节的主要内容。面试题如下: 请说说 rm / -rf 的作用？

---
---

## 什么是 Shell

在学习 Linux 指令之前，先来说一下什么是 Shell？Shell 把输入的指令，传递给操作系统去执行，所以 Shell 是一个命令行的用户界面。

早期程序员没有图形界面用，就用 Shell。而且图形界面制作成本较高，不能实现所有功能，因此今天的程序员依然在用 Shell。

平时还经常会看到一个词叫作 bash(Bourne Again Shell)，它是用 Shell 组成的程序。这里的 Bourne 是一个人名，Steve Bourne 是 bash 的发明者。

学习的所有指令，不是写死在操作系统中的，而是一个个程序。比如 rm 指令，可以用 which 指令查看它所在的目录。

```shell
$ which rm
/usr/bin/rm
```

rm 指令在 ```/usr/bin/rm``` 目录中。输入了 ```which rm```，然后获得了 ```/usr/bin/rm``` 的结果，最终执行这条指令的是操作系统，连接使用者和操作系统的程序就是 Shell。

Linux 对文件目录操作的指令就工作在 Shell 上，接下来讲讲文件目录操作指令。

---

## Linux 对文件目录的抽象

Linux 对文件进行了一个树状的抽象。/ 代表根目录，每一节目录也用 / 分开，sm所展示的 ```/usr/bin/rm``` 中，第一级目录是 / 根目录，第二级目录是 usr 目录，第三级是 bin 目录。最后的 rm 是一个文件。

---

### 路径(path)

像 ```/usr/bin/rm``` 称为可执行文件 rm 的路径。路径就是一个文件在文件系统中的地址。如果文件系统是树形结构，那么通常一个文件只有一个地址(路径)。

目标文件的绝对路径(Absolute path)，也叫作完全路径(full path)，是从 / 开始，接下来每一层都是一级子目录，直到定位到目标文件为止。

如上面所示的例子中，```/usr/bin/rm``` 就是一个绝对路径。

---

### 工作目录

为了方便工作，Shell 还抽象出了工作目录。当用户打开 Shell 的时候，Shell 就会给用户安排一个工作目录。因此也就产生了相对路径。

相对路径(Relative path)是以工作目录为基点的路径。比如:

* 当用户在 ```/usr``` 目录下的时候，rm 文件的相对路径就是 ```bin/rm```
* 如果用户在 ```/usr/bin``` 目录下的时候，rm 文件的路径就是 ```./rm``` 或者 rm，这里用 . 代表当前目录
* 如果用户在 ```/usr/bin/somedir``` 下，那么 rm 的相对路径就是 ```../rm```，这里用 .. 代表上一级目录

使用 cd(change directory)指令切换工作目录，既可以用绝对路径，也可以用相对路径。

* 输入 ```cd```，不带任何参数会切换到用户的家目录，Linux 中通常是 ```/home/{用户名}```
* 输入 ```cd .``` 什么都不会发生，因为 . 代表当前目录
* 输入 ```cd..``` 会回退一级目录，因为 .. 代表上级目录

利用上面这 3 种能力，就可以方便的构造相对路径了。

Linux 提供了一个指令 pwd(Print Working Directory) 查看工作目录。

```shell
$ pwd
/home/user
```

正在 ```/home/user``` 目录下工作。

---

### 几种常见的文件类型

另一方面，Linux 下的目录也是一种文件；但是文件也不只有目录和可执行文件两种。常见的文件类型有以下 7 种:

* 普通文件(比如一个文本文件)
* 目录文件(目录也是一个特殊的文件，它用来存储文件清单，比如 / 也是一个文件)
* 可执行文件(上面的rm就是一个可执行文件)
* 管道文件(会在下一课时讨论管道文件)
* Socket 文件(会在模块七网络部分讨论 Socket 文件)
* 软链接文件(相当于指向另一个文件所在路径的符号)
* 硬链接文件(相当于指向另一个文件的指针，关于软硬链接将在 [模块六: 文件系统](../module_6) 部分讨论)

使用 ```ls -F``` 就可以看到当前目录下的文件和它的类型。

* ```*``` 结尾的是可执行文件
* ```=``` 结尾的是 Socket 文件
* ```@``` 结尾的是软链接
* ```|``` 结尾的管道文件
* 没有符号结尾的是普通文件
* ```/``` 结尾的是目录

```shell
$ ls -F
 anaconda3/   appilcations/   Desktop/     extend/        Pictures/   repository/   wekafiles/
 Android/     common/         Downloads/  'Nutstore Files'/   R/          snap/
```

---

### 设备文件

Socket 是网络插座，是客户端和服务器之间同步数据的接口。其实，Linux 不只把 Socket
抽象成了文件，设备基本也都被抽象成了文件。因为设备需要不断和操作系统交换数据。而交换方式只有两种——读和写。所以设备是可以抽象成文件的，因为文件也支持这两种操作。

Linux 把所有的设备都抽象成了文件，比如说打印机、USB、显卡等。这让整体的系统设计变得高度统一。

至此，就已经了解了 Linux 对文件目录的抽象，接下来看看具体的增删改查指令。

---

## 文件的增删改查

---

### 增加

创建一个普通文件的方法有很多，最常见的有 touch 指令。比如下面创建了一个 a.txt 文件。

```shell
$ touch a.txt
```

touch 指令本来是用来更改文件的时间戳的，但是如果文件不存在 touch 也会帮助创建一个空文件。

如果拿到一个指令不知道该怎么用，比如 touch，可以用 ```man touch``` 去获得帮助。man 意思是 manual，就是说明书的意思，这里指的是系统的手册。

```shell
$ man touch
TOUCH(1)                         User Commands                        TOUCH(1)

NAME
       touch - change file timestamps

SYNOPSIS
       touch [OPTION]... FILE...

DESCRIPTION
       Update  the  access  and modification times of each FILE to the current
       time.

       A FILE argument that does not exist is created empty, unless -c  or  -h
       is supplied.

       A  FILE  argument  string of - is handled specially and causes touch to
       change the times of the file associated with standard output.

       Mandatory arguments to long options are  mandatory  for  short  options
       too.

       -a     change only the access time

 Manual page touch(1) line 1 (press h for help or q to quit)
```

另外如果需要增加一个目录，就需要用到 mkdir 指令(make directory)，比如创建一个 hello 目录，如下图所示:

```shell
$ mkdir hello
```

---

### 查看

创建之后可以用 ls 指令看到这个文件，ls 是 list 的缩写。下面是指令 ls 的执行结果。

```shell
$ ls
a.txt  hello
```

看到在当前的目录下有一个 a.txt 文件，还有一个 hello 目录。

如果想看到 a.txt 更完善的信息，还可以使用 ```ls -l```。```-l``` 是 ls 指令的可选参数。

```shell
$ ls -l
total 4
-rw-rw-r-- 1 user user    0 7月  25 17:02 a.txt
drwxrwxr-x 2 user user 4096 7月  25 17:02 hello
```

如上图所示，可以看到两个 user，它们是 a.txt 所属的用户和所属的用户分组，刚好重名了。7月是日期。 中间有一个 0 是 a.txt 的文件大小，目前 a.txt 中还没有写入内容，因此大小是 0。

另外虽然 hello 是空的目录，但是目录文件 Linux 上来就分配了 4096 字节的空间。这是因为目录内需要保存很多文件的描述信息。

---

### 删除

如果想要删除 a.txt 可以用 ```rm a.txt```；如我们要删除 hello 目录，可以用 ```rm hello```。rm 是 remove 的缩写。

```shell
$ rm hello
rm: cannot remove 'hello': Is a directory
```

但当输入 ```rm hello``` 的时候，会提示 hello 是一个目录，不可以删除。因此我们需要增加一个可选项，比如 ```-r``` 即 recursive(递归)
。目录是一个递归结构，所以需要用递归删除。最后，```rm hello -r``` 删除了 hello 目录。

接下来尝试在 hello 目录下新增一个文件，比如相对路径是 ```hello/world/os.txt```。需要先创建 ```hello/world``` 目录。这种情况会用到 mkdir 的 ```-p``` 参数，这个参数控制
mkdir 当发现目标目录的父级目录不存在的时候会递归的创建。

```shell
$ mkdir -p hello/world
$ touch hello/world/os.txt
$ ls hello/world/
os.txt
```

---

### 修改

如果需要修改一个文件，可以使用 nano 或者 vi 编辑器。类似的工具还有很多，但是 nano 和 vi 一般是 linux 自带的。

---

### 查阅文件内容

在了解了文件的增删改查操作后，下面来学习查阅文件内容。Linux 下查阅文件内容，可以根据不同场景选择不同的指令。

---

#### cat

当文件较小时，比如一个配置文件，想要快速浏览这个文件，可以用 cat 指令。下面 cat 指令可以快速查看 ```/etc/hosts``` 文件。cat 指令将文件连接到标准输出流并打印到屏幕上。

```shell
 cat /etc/hosts
127.0.0.1	localhost
127.0.1.1	user
199.232.68.133 raw.githubusercontent.com
199.232.68.133 githubusercontent.com
199.232.96.133 camo.githubusercontent.com
199.232.96.133 avatars.githubusercontent.com/

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
0.0.0.0 www.xmind.net
```

标准输出流(Standard Output)也是一种文件，进程可以将要输出的内容写入标准输出流文件，这样就可以在屏幕中打印。

如果用 cat 查看大文件，比如一个线上的日志文件，因为动辄有几个 G，控制台打印出所有的内容就要非常久，而且刷屏显示看不到东西。

而且如果在线上进行查看大文件的操作，会带来不必要的麻烦:

* 首先因为需要把文件拷贝到输入输出流，这需要花费很长时间，这个过程会占用机器资源；
* 其次，本身文件会读取到内存中，这时内存被大量占用，很危险，这可能导致其他应用内存不足。因此就需要一些不用加载整个文件，就能查看文件内容的指令。

---

#### more

more 可以读取文件，但不需要读取整个文件到内存中。本身 more 的定位是一个阅读过滤器，在 more 里除了可以向下翻页，还可以输入一段文本进行搜索。

```shell
$ more /var/log/kern.log
Jul 25 09:28:10 user kernel: [    8.234020] aufs 5.x-rcN-20200622
Jul 25 09:28:10 user kernel: [    8.272069] r8169 0000:6d:00.1 enp109s0f1: Link is Down
Jul 25 09:28:10 user kernel: [    8.292653] iwlwifi 0000:6e:00.0: Applying debug destination EXTERNAL_DRAM
Jul 25 09:28:10 user kernel: [    8.370632] iwlwifi 0000:6e:00.0: Applying debug destination EXTERNAL_DRAM
Jul 25 09:28:10 user kernel: [    8.372220] iwlwifi 0000:6e:00.0: FW already configured (0) - re-configuring
Jul 25 09:28:11 user kernel: [    9.033887] ACPI Warning: \_SB.PCI0.PEG0.PEGP._DSM: Argument #4 type mismatch - Found [Buffer], ACPI requires [Package] (20200528/nsarg
uments-59)
Jul 25 09:28:11 user kernel: [    9.547334] Bluetooth: RFCOMM TTY layer initialized
Jul 25 09:28:11 user kernel: [    9.547338] Bluetooth: RFCOMM socket layer initialized
Jul 25 09:28:11 user kernel: [    9.547347] Bluetooth: RFCOMM ver 1.11
Jul 25 09:28:12 user canonical-livepatch[1118]: starting client daemon version 9.6.2
Jul 25 09:28:12 user canonical-livepatch[1118]: starting svc "mitigation loop"
Jul 25 09:28:12 user canonical-livepatch[1118]: service "mitigation loop" started
Jul 25 09:28:12 user canonical-livepatch[1118]: starting svc "socket servers"
Jul 25 09:28:12 user canonical-livepatch[1118]: service "socket servers" started
Jul 25 09:28:12 user canonical-livepatch[1118]: starting svc "refresh loop"
Jul 25 09:28:12 user canonical-livepatch[1118]: service "refresh loop" started
Jul 25 09:28:12 user canonical-livepatch[1118]: client daemon started
Jul 25 09:28:12 user canonical-livepatch[1118]: Client.Check
Jul 25 09:28:12 user canonical-livepatch[1118]: No payload available.
Jul 25 09:28:12 user canonical-livepatch[1118]: during refresh: cannot check: No machine-token. Please run 'canonical-livepatch enable'!
Jul 25 09:28:14 user kernel: [   12.127280] wlp110s0: authenticate with 90:12:34:d2:fc:de
Jul 25 09:28:14 user kernel: [   12.130683] wlp110s0: send auth to 90:12:34:d2:fc:de (try 1/3)
Jul 25 09:28:14 user kernel: [   12.235993] wlp110s0: send auth to 90:12:34:d2:fc:de (try 2/3)
Jul 25 09:28:14 user kernel: [   12.263705] wlp110s0: authenticated
Jul 25 09:28:14 user kernel: [   12.264159] wlp110s0: associate with 90:12:34:d2:fc:de (try 1/3)
Jul 25 09:28:14 user kernel: [   12.265541] wlp110s0: RX AssocResp from 90:12:34:d2:fc:de (capab=0x411 status=0 aid=1)
Jul 25 09:28:14 user kernel: [   12.267316] wlp110s0: associated
Jul 25 09:28:14 user kernel: [   12.283826] IPv6: ADDRCONF(NETDEV_CHANGE): wlp110s0: link becomes ready
Jul 25 09:28:14 user kernel: [   12.315220] wlp110s0: Limiting TX power to 30 (30 - 0) dBm as advertised by 90:12:34:d2:fc:de
Jul 25 09:28:17 user kernel: [   15.465132] Guest personality initialized and is inactive
Jul 25 09:28:17 user kernel: [   15.465197] VMCI host device registered (name=vmci, major=10, minor=58)
Jul 25 09:28:17 user kernel: [   15.465197] Initialized host personality
Jul 25 09:28:17 user kernel: [   15.484547] NET: Registered protocol family 40
Jul 25 09:28:18 user kernel: [   15.772779] kauditd_printk_skb: 48 callbacks suppressed
Jul 25 09:28:18 user kernel: [   15.772780] audit: type=1400 audit(1627176498.124:60): apparmor="STATUS" operation="profile_load" profile="unconfined" name="docker-def
ault" pid=2387 comm="apparmor_parser"
Jul 25 09:28:18 user kernel: [   16.169743] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you n
eed this.
Jul 25 09:28:18 user kernel: [   16.171367] Bridge firewalling registered
Jul 25 09:28:18 user kernel: [   16.187128] bpfilter: Loaded bpfilter_umh pid 2404
Jul 25 09:28:18 user kernel: [   16.265766] Initializing XFRM netlink socket
Jul 25 09:28:19 user kernel: [   17.333653] rfkill: input handler disabled
--More--(12%)
```

---

#### less

less 是一个和 more 功能差不多的工具，打开 man 能够看到 less 的介绍上写着自己是 more 的反义词(opposite of more)。less 支持向上翻页，这个功能 more 是做不到的。所以现在 less
用得更多一些。

---

#### head/tail

head 和 tail 是一组，它们用来读取一个文件的头部 N 行或者尾部 N 行。比如一个线上的大日志文件，当线上出了 bug，服务暂停的时候，就可以用 ```tail -n 1000``` 去查看最后的 1000
行日志文件，寻找导致服务异常的原因。

另一个比较重要的用法是，如果想看一个实时的 nginx 日志，可以使用 ```tail -f 文件名```，这样会看到用户的请求不断进来。查一下 man，会发现 ```-f``` 是 follow
的意思，就是文件追加的内容会跟随输出到标准输出流。

---

#### grep

有时候查看一个指定 ip 的 nginx 日志，或者查看一段时间内的 nginx 日志。如果不想用 less 和 more 进入文件中去查看，就可以用 grep 命令。

grep 这个词分成三段来看，是 g|re|p。

* g 就是 global，全局
* re 就是 regular expression，正则表达式
* p 就是 pattern，模式

所以这个指令的作用是通过正则表达式全局搜索一个文件找到匹配的模式。

下面举两个例子看看 grep 的用法:

例 1: 查找 ip 地址

可以通过 grep 命令定位某个 ip 地址的用户都做了什么事情，如下图所示:

```shell
$ cd /var/log/nginx
$ grep 165.227.136.172 ./access.log
165.227.136.172 - - [25/Jul/2021:12:02:26 +0800] "GET / HTTP/1.0" 200 240 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:27 +0800] "GET / HTTP/1.1" 200 240 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:27 +0800] "HEAD / HTTP/1.0" 200 0 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:32 +0800] "OPTIONS / RTSP/1.0" 400 166 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:34 +0800] "GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0" 404 162 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:34 +0800] "OPTIONS / HTTP/1.0" 405 166 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:36 +0800] "GET / HTTP/1.1" 200 240 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:37 +0800] "l\x00\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x00" 400 166 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:39 +0800] "\x89\xC1\x9C\x1C*\xFF\xFC\xF1Q999\x00" 400 166 "-" "-"
165.227.136.172 - - [25/Jul/2021:12:02:40 +0800] "GET / HTTP/1.1" 200 240 "-" "-"
```

例 2: 查找时间段的日志

可以通过 grep 命令查找某个时间段内用户都做了什么事情。

```shell
$ grep 25/Jul/2021 ./access.log
101.133.155.170 - - [25/Jul/2021:00:50:22 +0800] "\x16\x03\x01\x02\x00\x01\x00\x01\xFC\x03\x03\x94\xB9\x99\xF4\xF4\xB8\x90\x00\x5C\x01V\xEC\xCFj\x08\x07vBB\xFB\x03\xDE!oA\xCC\x8C\xECz\xE6o\xA1 \xD9\xF3\x13\xF3l\xC4\x1D\x09\xF5 \x19z\x07;7=\xD5\x87p\xF1\xF9\x98\xCCC\xD1|\x14\x0B\xC6\xE8~\xDF\x00>\x13\x02\x13\x03\x13\x01\xC0,\xC00\x00\x9F\xCC\xA9\xCC\xA8\xCC\xAA\xC0+\xC0/\x00\x9E\xC0$\xC0(\x00k\xC0#\xC0'\x00g\xC0" 400 166 "-" "-"
101.133.155.170 - - [25/Jul/2021:00:50:22 +0800] "GET / HTTP/1.1" 200 240 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
80.82.77.192 - - [25/Jul/2021:01:15:13 +0800] "GET / HTTP/1.1" 200 201 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
34.79.107.251 - - [25/Jul/2021:02:14:15 +0800] "GET / HTTP/1.1" 200 201 "-" "python-requests/2.26.0"
47.100.9.101 - - [25/Jul/2021:03:43:51 +0800] "GET / HTTP/1.1" 200 201 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0"
47.101.59.121 - - [25/Jul/2021:03:44:10 +0800] "GET / HTTP/1.1" 200 201 "-" "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D)"
106.15.191.180 - - [25/Jul/2021:03:45:43 +0800] "GET / HTTP/1.1" 200 201 "-" "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D)"
114.119.133.67 - - [25/Jul/2021:03:49:41 +0800] "GET /robots.txt HTTP/1.1" 404 134 "-" "Mozilla/5.0 (compatible;PetalBot;+https://webmaster.petalsearch.com/site/petalbot)"
101.132.193.68 - - [25/Jul/2021:04:25:22 +0800] "GET / HTTP/1.1" 200 201 "-" "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D)"
101.132.131.7 - - [25/Jul/2021:04:26:16 +0800] "GET / HTTP/1.1" 200 201 "-" "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D)"
185.36.81.24 - - [25/Jul/2021:04:41:51 +0800] "GET / HTTP/1.1" 200 201 "-" "Linux Gnu (cow)"
47.101.150.223 - - [25/Jul/2021:04:52:42 +0800] "\x16\x03\x03\x00\x88\x01\x00\x00\x84\x03\x03`\xFC}\x9A\xD7dp\xE7\x98\xCA@\x13\xD0 O\xB0\xF9\xC5\x9D%\xCCR\xF1\x01\x22e\xF8Ar9\x0E\x80\x00\x00\x16\xC0\x14\x005\xC0\x13\x00/\xC0,\xC0+\xC00\x00\x9D\xC0/\x00\x9C\x00" 400 166 "-" "-"
209.141.50.63 - - [25/Jul/2021:05:58:07 +0800] "POST /boaform/admin/formLogin HTTP/1.1" 404 134 "http://47.99.100.211:80/admin/login.asp" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
//..
```

### 查找文件

用户经常还会有一种诉求，就是查找文件。

之前使用过一个 which 指令，这个指令可以查询一个指令文件所在的位置，比如 ```which grep``` ，会看到 grep 指令被安装的位置是 ```/usr/bin```。但是you一个更加通用的指令查找文件，也就是 find
指令。

---

#### find

find 指令帮助我们在文件系统中查找文件。比如如果想要查找所有 ```.txt``` 扩展名的文件，可以使用 ```find / -iname "*.txt"```，```-iname``` 这个参数是用来匹配查找的，i
字母代表忽略大小写，这里也可以用 ```-name``` 替代。输入这条指令，会看到不断查找文件:

```shell
$ find / -iname "*.txt"
/usr/src/linux-headers-5.4.0-80-generic/scripts/spelling.txt
/usr/src/linux-headers-5.4.0-77-generic/scripts/spelling.txt
/usr/src/linux-headers-5.4.0-66/arch/sh/include/mach-ecovec24/mach/partner-jet-setup.txt
/usr/src/linux-headers-5.4.0-66/arch/sh/include/mach-kfr2r09/mach/partner-jet-setup.txt
/usr/src/linux-headers-5.4.0-66/scripts/spelling.txt
/usr/src/linux-headers-5.4.0-80/arch/sh/include/mach-ecovec24/mach/partner-jet-setup.txt
/usr/src/linux-headers-5.4.0-80/arch/sh/include/mach-kfr2r09/mach/partner-jet-setup.txt
/usr/src/linux-headers-5.4.0-80/scripts/spelling.txt
/usr/src/linux-headers-5.4.0-66-generic/scripts/spelling.txt
/usr/src/linux-headers-5.4.0-77/arch/sh/include/mach-ecovec24/mach/partner-jet-setup.txt
/usr/src/linux-headers-5.4.0-77/arch/sh/include/mach-kfr2r09/mach/partner-jet-setup.txt
/usr/src/linux-headers-5.4.0-77/scripts/spelling.txt
/usr/share/doc/linux-firmware/licenses/LICENCE.rtlwifi_firmware.txt
/usr/share/doc/linux-firmware/licenses/LICENCE.ralink-firmware.txt
/usr/share/doc/linux-firmware/licenses/LICENCE.realtek-firmware.txt
/usr/share/doc/linux-firmware/licenses/LICENCE.tda7706-firmware.txt
/usr/share/doc/python3-setuptools/development.txt
/usr/share/doc/python3-setuptools/index.txt
//..
```

---

## 总结

这节课学习了很多指令，最后再一起复习一下。

* ```pwd``` 指令查看工作目录
* ```cd``` 指令切换工作目录
* ```which``` 指令查找一个执行文件所在的路径
* ```ls``` 显示文件信息
* ```rm``` 删除文件
* ```touch``` 修改一个文件的时间戳，如果文件不存在会触发创建文件
* ```vi``` 和 ```nano``` 可以用来编辑文件
* ```cat``` 查看完成的文件适合小型文件
* ```more less``` 查看一个文件但是只读取用户看到的内容到内存，因此消耗资源较少，适合在服务器上看日志
* ```head tail```可以用来看文件的头和尾
* ```grep``` 指令搜索文件内容
* ```find``` 指令全局查找文件

来到本节关联的题目: ```rm / -rf``` 的作用是？

答:

* ```/``` 是文件系统根目录
* ```rm``` 是删除指令
* ```-r``` 是 recursive(递归)
* ```-f``` 是 force(强制)，遇到只读文件也不提示，直接删除

所以 ```rm -rf /``` 就是删除整个文件系统上的所有文件，而且不用给用户提示。

---

## 课后习题

最后再给出一道题，搜索文件系统中所有以包含 std 字符串且以 ```.h``` 扩展名结尾的文件。

---
---

