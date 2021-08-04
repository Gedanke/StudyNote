# 高级技巧之集群部署: 利用 Linux 指令同时在多台机器部署程序

通过前面的学习，相信你已经掌握了一些基础指令的使用方法，本节继续挑战一个更复杂的问题——用 Linux 指令管理一个集群。这属于 Linux
指令的高级技巧，所谓高级技巧并不是要学习更多的指令，而是要把之前所学的指令进行排列组合。当你从最初只能写几条指令、执行然后看结果，成长到具备书写一个拥有几十行、甚至上百行的 bash
脚本的能力时，就意味着你具备了解决复杂问题的能力。而最终的目标，是提升对指令的熟练程度，锻炼工程能力。

本课时通过把简单的指令组合起来，分层组织成最终的多个脚本文件，解决一个复杂的工程问题: 在成百上千的集群中安装一个 Java 环境。

---
---

## 第一步: 搭建学习用的集群

第一步先搭建一个学习用的集群。这里我使用的是一台 ubuntu 物理机(桌面版)，使用 [multipass](https://multipass.run/) 创建两个 ubuntu 服务器实例。

相对于桌面版，服务器版对资源的消耗会少很多。本次桌面版的 ubuntu 命名为 user，两个用来被管理的服务器版叫作 ubuntu 和 ubuntu1。

```shell
$ multipass list
Name                    State             IPv4             Image
ubuntu                  Stopped           --               Ubuntu 20.04 LTS
ubuntu1                 Stopped           --               Ubuntu 20.04 LTS
```

注意，在这里只用了 3 个实例(一个桌面版和两个服务器)，但是接下来要写的脚本是可以在很多台服务器之间复用的。

---

## 第二步: 循环遍历 IP 列表

可以想象一个局域网中有很多服务器需要管理，它们彼此之间网络互通，我们通过一台主机对它们进行操作，即通过 user 操作 ubuntu 和 ubuntu1。

首先分别登陆两个实例:

```shell
$ multipass shell ubuntu                                   
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-80-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Aug  3 18:32:41 CST 2021

  System load:  0.39              Processes:             106
  Usage of /:   31.1% of 4.67GB   Users logged in:       0
  Memory usage: 19%               IPv4 address for ens4: 10.100.94.141
  Swap usage:   0%


0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Tue Aug  3 18:30:06 2021 from 10.100.94.1
ubuntu@ubuntu:~$ 
```

```shell
$ multipass shell ubuntu1
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-80-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Aug  3 18:33:18 CST 2021

  System load:  0.04              Processes:             105
  Usage of /:   31.3% of 4.67GB   Users logged in:       0
  Memory usage: 19%               IPv4 address for ens4: 10.100.94.102
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Tue Aug  3 18:32:33 2021 from 10.100.94.1
ubuntu@ubuntu1:~$ 
```

登陆之后，从 user 可以看到:

```shell
$ multipass list
Name                    State             IPv4             Image
ubuntu                  Running           10.100.94.141    Ubuntu 20.04 LTS
ubuntu1                 Running           10.100.94.102    Ubuntu 20.04 LTS
```

在主服务器上我们维护一个 ip 地址的列表，保存成一个文件，如下图所示:

```shell
$ cat iplist
10.100.94.141
10.100.94.102 
```

目前 iplist 中只有两项，但是如果有足够的机器，可以在里面放成百上千项。接下来，请思考 shell 如何遍历这些 ip？

可以先尝试实现一个最简单的程序，从文件 iplist 中读出这些 ip 并尝试用 for 循环遍历这些 ip，具体 [程序](../../images/module_2/foreach.sh) 如下:

```shell
#!/usr/bin/bash
readarray -t ips < iplist
for ip in ${ips[@]}
do
  echo $ip
done
```

首行的 #! 叫作 Shebang。Linux 的程序加载器会分析 Shebang 的内容，决定执行脚本的程序。这里我们希望用 bash 来执行这段程序，因为用到的 readarray 指令是 bash 4.0 后才增加的能力。

readarray 指令将 iplist 文件中的每一行读取到变量 ips 中。ips 是一个数组，可以用 ```echo ${ips[@]}``` 打印其中全部的内容: @代 表取数组中的全部内容；$ 符号是一个求值符号。不带 $
的话，```ips[@]``` 会被认为是一个字符串，而不是表达式。

for 循环遍历数组中的每个 ip 地址，echo 把地址打印到屏幕上。

如果用 shell 执行上面的程序会报错，因为 readarray 是 bash 4.0 后支持的能力，因此用 chomd 为 foreach.sh 增加执行权限，然后直接利用 shebang 的能力用 bash 执行，如下所示:

```shell
$ chmod +x foreach.sh 
$ ./foreach.sh 
10.100.94.141
10.100.94.102
```

---

## 第三步: 创建集群管理账户

为了方便集群管理，通常使用统一的用户名管理集群。这个账号在所有的集群中都需要保持命名一致。比如这个集群账号的名字就叫作 user。

接下来探索一下如何创建这个账户 user，如下所示:

```shell
$ sudo useradd -m -d /home/user user
$ sudo passwd user
New password:
Retype new password: 
passwd: password updated sucessfully
```

上面创建了 user 账号，然后把 user 加入 sudo 分组。这样 user 就有了 sudo 成为 root 的能力，如下所示:

```shell
$ sudo usermod -G sudo user
```

接下来，设置 user 用户的初始化 shell 是 bash，如下所示:

```shell
$ sudo usermod -shell /bin/bash user
```

这个时候如果使用命令 ```su user```，可以切换到 user 账号，但是会发现命令行没有了颜色。可以将原来用户下面的 ```.bashrc``` 文件拷贝到 ```/home/user``` 目录下，如下所示:

```shell
$ sudo cp ~/.bashrc /home/user
$ sudo chowm user.user /home/user/.bashrc
```

这样，就把一些自己平时用的设置拷贝了过去，包括终端颜色的设置。```.bashrc``` 是启动 bash 的时候会默认执行的一个脚本文件。

接下来编辑一下 ```/etc/sudoers``` 文件，增加一行 ```user ALL=(ALL) NOPASSWD:ALL``` 表示 user 账号 sudo 时可以免去密码输入环节，如下所示:

```shell
$ su user
Password:
$ sudo su root
root@user:/home/user
```

可以把上面的完整过程整理成指令文件，[create_user.sh](../../images/module_2/create_user.sh) :

```shell
$ sudo useradd -m -d /home/user user
$ sudo passwd user
$ sudo usermod -G sudo user
$ sudo usermod --shell /bin/bash user
$ sudo cp ~/.bashrc /home/user/
$ sudo chown user.user /home/user/.bashrc
$ sduo sh -c 'echo "user ALL=(ALL) NOPASSWD:ALL">>/etc/sudoers'
```

可以删除用户 user，并清理 ```/etc/sudoers``` 文件最后一行。用指令 ```userdel user``` 删除账户，然后执行 create_user.sh 重新创建回 user 账户。如果发现结果一致，就代表
create_user.sh 功能没有问题。

最后我们想在 ubuntu 和 ubuntu1 上都执行 create_logou.sh 这个脚本。但是不要忘记，我们的目标是让程序在成百上千台机器上传播，因此还需要一个脚本将 create_user.sh 拷贝到需要执行的机器上去。

这里，可以对 foreach.sh 稍做修改，然后分发 create_user.sh 文件。

```shell
#!/usr/bin/bash
readarray -t ips < iplist
for ip in ${ips[@]}
do
  scp ~/remote/create_user.sh ramroll@$ip:~/create_user.sh
done
```

这里，我们在循环中用 scp 进行文件拷贝，然后分别去每台机器上执行 create_user.sh。

如果机器非常多，上述过程会变得非常烦琐。你可以先带着这个问题学习下面的 Step4，然后再返回来重新思考这个问题，当然你也可以远程执行脚本。另外，还有一个叫作 sshpass
的工具，可以帮你把密码传递给要远程执行的指令，如果对这块内容感兴趣，可以自己研究下这个工具。

---

## 第四步:  打通集群权限

接下来需要打通从主服务器到 ubuntu 和 ubuntu1 的权限。当然也可以每次都用 ssh 输入用户名密码的方式登录，但这并不是长久之计。如果有成百上千台服务器，输入用户名密码就成为一件繁重的工作。

这时候可以考虑利用主服务器的公钥在各个服务器间登录，避免输入密码。接下来聊聊具体的操作步骤:

首先需要在u1上用 ```ssh-keygen``` 生成一个公私钥对，然后把公钥写入需要管理的每一台机器的 authorized_keys 文件中。如下所示: 使用 ssh-keygen 在主服务器 ubuntu 中生成公私钥对。

```shell
$ mkdir -p ~/.ssh
$ cd ~/.ssh/
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): 
/home/ubuntu/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ubuntu/.ssh/id_rsa
Your public key has been saved in /home/ubuntu/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:noCn753mL37h788B5gbM1urnAthDs5QKrgJANboakYg ubuntu@ubuntu
The key's randomart image is:
+---[RSA 3072]----+
|  .o             |
|oo. .            |
|E.       .       |
|... ..  =o .     |
|o. ...o*So= +    |
|o.  .ooo=o.= .   |
|o  ..   o+..o .  |
|. .  . .oo+... . |
| .   .o+=+o*+.o  |
+----[SHA256]-----+
```

在演示之前提前创建过，所以会显示 Overwrite。

然后使用 ```mkdir -p``` 创建 ```~/.ssh``` 目录，-p 的优势是当目录不存在时，才需要创建，且不会报错。~ 代表当前家目录。如果文件和目录名前面带有一个 .，就代表该文件或目录是一个需要隐藏的文件。平时用 ls
的时候，并不会查看到该文件，通常这种文件拥有特别的含义，比如 ```~/.ssh``` 目录下是对 ssh 的配置。

用 cd 切换到 ```.ssh``` 目录，然后执行 ssh-keygen。这样会在 ```~/.ssh``` 目录中生成两个文件，id_rsa.pub 公钥文件和 is_rsa 私钥文件。如下所示:

```shell
$ ls
authorized_keys  id_rsa  id_rsa.pub  known_hosts
$ cat id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC8cuNmk4dd4q9bdpaNXf4RadjgFQX69CcC7OsvLhanD2yIqYcVXjEqZLVYFVSSXIWVfQlrGPZubIz5O4DbD0I29fblp96fCxzyvNolexqLNdlzIDawpQSe+gm4zhnAIKEvM2W7vEcZt5rsKt6znVCJY2/PEjWzL6hhH/uBSLtSZ9Em8M7yJS7Yy5pvTP/Y4aZ4Mdl5i4upo6G4xlrTGPGNPw8XBlALB+oPLs+4p0vQi3t2RHKT5ouR1w+uyaVkd9p/llEi4XKTqzpBQgx/qDNfhGNTjAOokh2yFqceSju3ejM4Pfnpl0ZIMfSD2YHlbddJtiDE3XQx3oM72pAZy7c3YH97k5t32be9ZBkHYgQ7ftp8VLcackd+fomD+xSd3XBmlHUQ/dR5QWnJMlWx/6LKWScqBs6eENDtU2Q1vAthf49lv/+rzrFKEYgPdOL8RJNjosgGHeTbrWJylkhdYxcAYlnCkMu8YxdwRwy+c5LXywiLgj/M1w23RSApgD27U2c= user@ubuntu
```

可以看到 id_rsa.pub 文件中是加密的字符串，我们可以把这些字符串拷贝到其他机器对应用户的 ```~/.ssh/authorized_keys``` 文件中，当 ssh 登录其他机器的时候，就不用重新输入密码了。
这个传播公钥的能力，可以用一个 shell 脚本执行，这里用 transfer_key.sh 实现。

修改一下 foreach.sh，并写一个 transfer_key.sh 配合 [foreach.sh](../../images/module_2/foreach.sh)
的工作。[transfer_key.sh](../../images/module_2/transfer_key.sh) 内容如下:

```shell
#!/usr/bin/bash
readarray -t ips < iplist
for ip in ${ips[@]}
do
  sh ./transfer_key.sh $ip
done
```

```shell
#!/bin/bash
ip=$1
pubkey=$(cat ~/.ssh/id_rsa.pub)
echo "execute on .. $ip"
ssh user@$ip "
mkdir -p ~/.ssh
echo $pubkey >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
"
```

在 foreach.sh 中执行 transfer_key.sh，并且将 IP 地址通过参数传递过去。在 transfer_key.sh 中，用 $1 读出 IP 地址参数，再将公钥写入变量
pubkey，然后登录到对应的服务器，执行多行指令。用 mkdir 指令检查 ```.ssh``` 目录，如不存在就创建这个目录。最后将公钥追加写入目标机器的 ```~/.ssh/authorized_keys``` 中。

```chmod 700``` 和 ```chmod 600``` 是因为某些特定的linux版本需要 ```.ssh``` 的目录为可读写执行，authorized_keys
文件的权限为只可读写。而为了保证安全性，组用户、所有用户都不可以访问这个文件。

此前，执行 foreach.sh 需要输入两次密码。完成上述操作后，再登录这两台服务器就不需要输入密码了。

---

## 第五步: 单机安装 Java 环境

在远程部署 Java 环境之前，先单机完成以下 Java 环境的安装，用来收集需要执行的脚本。

在 ubuntu 上安装 java 环境可以直接用 apt。

通过下面几个步骤脚本配置 Java 环境:

```shell
$ sudo apt install openjdk-11-jdk
```

经过一番等待已经安装好了 java，然后执行下面的脚本确认 java 安装。

```shell
$ which java
java --version
```

根据最小权限原则，执行 Java 程序考虑再创建一个用户 ujava。

```shell
$ sudo useradd -m -d /opt/ujava ujava
$ sudo usermod --shell /bin/bash user
```

这个用户可以不设置密码，因为我们不会真的登录到这个用户下去做任何事情。接下来为用户配置 Java 环境变量，如下所示:

```shell
$ ls -l /usr/bin/java
lrwxrwxrwx 1 root root 22 Oct 3 06:36 /usr/bin/java -> /etc/alternatives/java
$ ls -l /etc/alternatives/java
lrwxrwxrwx 1 root root 43 Oct 3 06:36 /etc/alternatives/java -> /usr/lib/jvm/java-11-openjdk-amd64/bin/java
```

通过两次 ls 追查，可以发现 java 可执行文件软连接到 ```/etc/alternatives/java``` 然后再次软连接到 ```/usr/lib/jvm/java-11-openjdk-amd64``` 下。

这样就可以通过下面的语句设置 JAVA_HOME 环境变量了。

```shell
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
```

Linux 的环境变量就好比全局可见的数据，这里使用 export 设置 JAVA_HOME 环境变量的指向。如果想看所有的环境变量的指向，可以使用 env 指令。

```shell
$ env
SHELL=/bin/bash
SESSION_MANAGER=local/user-P65xRP:@/tmp/.ICE-unix/2739,unix/user-P65xRP:/tmp/.ICE-unix/2739
QT_ACCESSIBILITY=1
COLORTERM=truecolor
XDG_CONFIG_DIRS=/etc/xdg/xdg-ubuntu:/etc/xdg
XDG_MENU_PREFIX=gnome-
no_proxy=localhost,127.0.0.0/8,::1
GNOME_DESKTOP_SESSION_ID=this-is-deprecated
GTK_IM_MODULE=fcitx
CONDA_EXE=/home/user/anaconda3/bin/conda
_CE_M=
JUNIT_HOME=/home/user/repository/jar/Juint
LANGUAGE=en_US:en
MANDATORY_PATH=/usr/share/gconf/ubuntu.mandatory.path
LC_ADDRESS=zh_CN.UTF-8
JAVA_HOME=/opt/java/jdk-14.0.1
//...
```

其中有一个环境变量比较重要，就是 PATH。

```shell
$ echo $PATH
/home/user/anaconda3/bin:/home/user/anaconda3/condabin:/usr/local/apache-maven-3.6.3/bin:/home/user/go/bin:/usr/local/go/bin:/home/user/.local/bin:/usr/local/apache-maven-3.6.3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/java/jdk-14.0.1/bin:/opt/java/jdk-14.0.1/bin
```

如图，可以使用 shell 查看 PATH 的值，PATH 中用 : 分割，每一个目录都是 linux 查找执行文件的目录。当用户在命令行输入一个命令，Linux 就会在 PATH 中寻找对应的执行文件。

当然我们不希望 JAVA_HOME 配置后重启一次电脑就消失，因此可以把这个环境变量加入 ujava 用户的 profile 中。这样只要发生用户登录，就有这个环境变量。

```shell
$ sudo sh -c 'echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/" >> /opt/ujava/.bash_profile'
```

将 JAVA_HOME 加入 bash_profile，这样后续远程执行 java 指令时就可以使用 JAVA_HOME 环境变量了。

最后，将上面所有的指令整理起来，形成一个 [install_java.sh]()。

```shell
#!/bin/bash
$ sudo apt -y install openjdk-11-jdk
$ sudo useradd -m -d /opt/ujava ujava
$ sudo usermod --shell /bin/bash ujava
$ sudo sh -c 'echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/" >> /opt/ujava/.bash_profile'
```

apt 后面增了一个 -y 是为了让执行过程不弹出确认提示。

---

## 第六步: 远程安装 Java 环境

终于到了远程安装 Java 环境这一步，又需要用到 foreach.sh。为了避免每次修改，可以考虑允许 foreach.sh 带一个文件参数，指定需要远程执行的脚本。

```shell
#!/usr/bin/bash
readarray -t ips < iplist
script=$1
for ip in ${ips[@]}
do
  ssh $ip 'bash -s' < $script
done
```

改写后的 foreach 会读取第一个执行参数作为远程执行的脚本文件。 而 ```bash -s``` 会提示使用标准输入流作为命令的输入； ```< $script``` 负责将脚本文件内容重定向到远程 bash 的标准输入流。

然后执行 ```foreach.sh install_java.sh```，机器等待 1 分钟左右，在执行结束后，可以用下面这个脚本- [check.sh]() 检测两个机器中的安装情况。

```shell
#!/bin/bash
sudo -u ujava -i /bin/bash -c 'echo $JAVA_HOME'
sudo -u ujava -i java --version
```

check.sh 中我们切换到 ujava 用户去检查 JAVA_HOME 环境变量和 Java 版本。执行的结果如下所示:

```shell
/usr/lib/jvm/java-ll-openjdk-amd64/
openjdk 11.0.8 2020-07-14
OpenJDK Runtime Environment (build 11.0.8+10-post-Ubuntu-0ubuntu120.04)
OpenJDK 64-Bit Server VM (build 11.0.8+10-post-Ubuntu-0ubuntu120.04, mixed mo de, sharing)
/usr/lib/jvm/java-11-openjdk-amd64/
openjdk 11.0.8 2020-07-14
OpenJDK Runtime Environment (build 11.0.8+10-post-Ubuntu-0ubuntu120.04)
OpenJDK 64-Bit Server VM (build 11.0.8+10-post-Ubuntu-0ubuntu120.04 mixed mode, sharing)
```

---

## 总结

这节课所讲的场景是自动化运维的一些皮毛。通过这样的场景练习，复习了很多之前学过的 Linux 指令。在尝试用脚本文件构建一个又一个小工具的过程中，可以发现复用很重要。

在工作中，优秀的工程师，总是善于积累和复用，而 shell 脚本就是积累和复用的利器。如果是第一次安装 java
环境，可以把今天的安装脚本保存在自己的笔记本中，下次再安装就能自动化完成了。除了积累和总结，另一个非常重要的就是你要尝试自己去查资料，包括使用 man 工具熟悉各种指令的使用方法，用搜索引擎查阅资料等。

---

## 课后练习题

最后再给出一道题: ```~/.bashrc```，```~/.bash_profile```，```~/.profile``` 和 ```/etc/profile``` 的区别是什么？

---
---

