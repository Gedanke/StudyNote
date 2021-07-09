# command

本篇介绍 Linux 常见命令，也是日常中使用率非常高的操作命令

---

## 基本命令

```shell
$ uname --help
Usage: uname [OPTION]...
Print certain system information.  With no OPTION, same as -s.

  -a, --all                print all information, in the following order,
                             except omit -p and -i if unknown:
  -s, --kernel-name        print the kernel name
  -n, --nodename           print the network node hostname
  -r, --kernel-release     print the kernel release
  -v, --kernel-version     print the kernel version
  -m, --machine            print the machine hardware name
  -p, --processor          print the processor type (non-portable)
  -i, --hardware-platform  print the hardware platform (non-portable)
  -o, --operating-system   print the operating system
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/uname>
or available locally via: info '(coreutils) uname invocation'
```

### 显示机器的处理器架构

```shell
$ uname -m 
x86_64
```

### 显示正在使用的内核版本

```shell
$ uname -r
5.8.0-59-generic
```

### 显示硬件系统部件，需要 root 权限

```shell
$ dmidecode -q 
BIOS Information
//...
Group Associations
	Name: $MEI
	Items: 1
		0x0000 (OEM-specific)

```

### 罗列一个磁盘的架构特性，需要 root 权限

```shell
$ hdparm -i /dev/hda 

/dev/sda:

 Model=
//..

 * signifies the current active mode

```

### 在磁盘上执行测试性读取操作系统信息

```shell
$ sudo hdparm -tT /dev/sda

/dev/sda:
 Timing cached reads:   21184 MB in  1.99 seconds = 10658.87 MB/sec
 Timing buffered disk reads: 1556 MB in  3.00 seconds = 518.12 MB/sec
```

### 显示机器的处理器架构

```shell
$ arch
x86_64
```

### 显示CPU info的信息

```shell
$ cat /proc/cpuinfo 
processor	: 0
vendor_id	: GenuineIntel
//..
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

```

### 显示中断

```shell
$ cat /proc/interrupts 
            CPU0       CPU1       CPU2       CPU3       
   0:          7          0          0          0  IR-IO-APIC    2-edge      timer
   1:          0         27          0          0  IR-IO-APIC    1-edge      i8042
   8:          0          0          1          0  IR-IO-APIC    8-edge      rtc0
   9:          0        146          0          0  IR-IO-APIC    9-fasteoi   acpi
//..
 PIW:          0          0          0          0   Posted-interrupt wakeup event
```

### 校验内存使用

```shell
$ cat /proc/meminfo
MemTotal:       16278680 kB
MemFree:         2640628 kB
//..
DirectMap4k:      639580 kB
DirectMap2M:    11825152 kB
DirectMap1G:     4194304 kB
```

## 显示哪些 swap 被使用

```shell
$ cat /proc/swaps 
Filename                                Type            Size            Used            Priority
/swapfile                               file            2097148         0               -2
```

## 显示内核的版本

```shell
$ cat /proc/version
Linux version 5.8.0-59-generic (buildd@lcy01-amd64-022) (gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #66~20.04.1-Ubuntu SMP Thu Jun 17 11:14:10 UTC 2021
```

or

```shell
$ uname -a
Linux dfs-P65xRP 5.8.0-59-generic #66~20.04.1-Ubuntu SMP Thu Jun 17 11:14:10 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

### 显示网络适配器及统计

```shell
$ cat /proc/net/dev
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo: 191210248 1362752    0    0    0     0          0         0 191210248 1362752    0    0    0     0       0          0
enp109s0f1:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
wlp110s0: 37919262   76509    0    0    0     0          0         0 19918796   74559    0    0    0     0       0          0
docker0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
```

### 显示已加载的文件系统

```shell
$ cat /proc/mounts 
sysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0
proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0
//..
nsfs /run/snapd/ns/canonical-livepatch.mnt nsfs rw 0 0
/dev/fuse /run/user/1000/doc fuse rw,nosuid,nodev,relatime,user_id=1000,group_id=1000 0 0
nsfs /run/snapd/ns/snap-store.mnt nsfs rw 0 0
```

### 罗列 PCI 设备

```shell
$ lspci -tv
-[0000:00]-+-00.0  Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers
           +-01.0-[01]--+-00.0  NVIDIA Corporation GP106M [GeForce GTX 1060 Mobile]
           |            \-00.1  NVIDIA Corporation GP106 High Definition Audio Controller
           +-02.0  Intel Corporation HD Graphics 530
           +-14.0  Intel Corporation 100 Series/C230 Series Chipset Family USB 3.0 xHCI Controller
           +-16.0  Intel Corporation 100 Series/C230 Series Chipset Family MEI Controller #1
           +-17.0  Intel Corporation HM170/QM170 Chipset SATA Controller [AHCI Mode]
           +-1c.0-[02-6c]--
           +-1c.4-[6d]--+-00.0  Realtek Semiconductor Co., Ltd. RTL8411B PCI Express Card Reader
           |            \-00.1  Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           +-1c.6-[6e]----00.0  Intel Corporation Wireless 3165
           +-1f.0  Intel Corporation HM170 Chipset LPC/eSPI Controller
           +-1f.2  Intel Corporation 100 Series/C230 Series Chipset Family Power Management Controller
           +-1f.3  Intel Corporation 100 Series/C230 Series Chipset Family HD Audio Controller
           \-1f.4  Intel Corporation 100 Series/C230 Series Chipset Family SMBus
```

### 显示 USB 设备

```shell
$ lsusb -tv
/:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/8p, 5000M
    ID 1d6b:0003 Linux Foundation 3.0 root hub
/:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/16p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
    |__ Port 2: Dev 2, If 2, Class=Human Interface Device, Driver=usbhid, 12M
        ID 24ae:4005  
    |__ Port 2: Dev 2, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        ID 24ae:4005  
    |__ Port 2: Dev 2, If 1, Class=Human Interface Device, Driver=usbhid, 12M
        ID 24ae:4005  
    |__ Port 5: Dev 3, If 1, Class=Human Interface Device, Driver=usbhid, 1.5M
        ID 18f8:1286 [Maxxter] 
    |__ Port 5: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
        ID 18f8:1286 [Maxxter] 
    |__ Port 8: Dev 4, If 1, Class=Wireless, Driver=btusb, 12M
        ID 8087:0a2a Intel Corp. 
    |__ Port 8: Dev 4, If 0, Class=Wireless, Driver=btusb, 12M
        ID 8087:0a2a Intel Corp. 
    |__ Port 9: Dev 5, If 0, Class=Video, Driver=uvcvideo, 480M
        ID 04f2:b5a7 Chicony Electronics Co., Ltd 
    |__ Port 9: Dev 5, If 1, Class=Video, Driver=uvcvideo, 480M
        ID 04f2:b5a7 Chicony Electronics Co., Ltd 
```

### 显示系统日期

```shell
$ date
2021年 07月 06日 星期二 16:54:26 CST
```

### 显示 2020 年的日历表

```shell
$ cal 2020
                            2020
         一月                    二月                    三月           
日 一 二 三 四 五 六  日 一 二 三 四 五 六  日 一 二 三 四 五 六  
          1  2  3  4                     1   1  2  3  4  5  6  7  
 5  6  7  8  9 10 11   2  3  4  5  6  7  8   8  9 10 11 12 13 14  
12 13 14 15 16 17 18   9 10 11 12 13 14 15  15 16 17 18 19 20 21  
19 20 21 22 23 24 25  16 17 18 19 20 21 22  22 23 24 25 26 27 28  
26 27 28 29 30 31     23 24 25 26 27 28 29  29 30 31              
                                                                  

         四月                    五月                    六月           
日 一 二 三 四 五 六  日 一 二 三 四 五 六  日 一 二 三 四 五 六  
          1  2  3  4                  1  2      1  2  3  4  5  6  
 5  6  7  8  9 10 11   3  4  5  6  7  8  9   7  8  9 10 11 12 13  
12 13 14 15 16 17 18  10 11 12 13 14 15 16  14 15 16 17 18 19 20  
19 20 21 22 23 24 25  17 18 19 20 21 22 23  21 22 23 24 25 26 27  
26 27 28 29 30        24 25 26 27 28 29 30  28 29 30              
                      31                                          

         七月                    八月                    九月           
日 一 二 三 四 五 六  日 一 二 三 四 五 六  日 一 二 三 四 五 六  
          1  2  3  4                     1         1  2  3  4  5  
 5  6  7  8  9 10 11   2  3  4  5  6  7  8   6  7  8  9 10 11 12  
12 13 14 15 16 17 18   9 10 11 12 13 14 15  13 14 15 16 17 18 19  
19 20 21 22 23 24 25  16 17 18 19 20 21 22  20 21 22 23 24 25 26  
26 27 28 29 30 31     23 24 25 26 27 28 29  27 28 29 30           
                      30 31                                       

         十月                   十一月                   十二月           
日 一 二 三 四 五 六  日 一 二 三 四 五 六  日 一 二 三 四 五 六  
             1  2  3   1  2  3  4  5  6  7         1  2  3  4  5  
 4  5  6  7  8  9 10   8  9 10 11 12 13 14   6  7  8  9 10 11 12  
11 12 13 14 15 16 17  15 16 17 18 19 20 21  13 14 15 16 17 18 19  
18 19 20 21 22 23 24  22 23 24 25 26 27 28  20 21 22 23 24 25 26  
25 26 27 28 29 30 31  29 30                 27 28 29 30 31        
                                                                  
```

---

## 关机

### 关闭系统(1)

```shell
$ shutdown -h now
```

### 关闭系统(2)

```shell
$ init 0
```

### 关闭系统(3)

```shell
$ telinit 0 
```

### 按预定时间关闭系统

```shell
$ shutdown -h hours:minutes
```

### 取消按预定时间关闭系统

```shell
$ shutdown -c 
```

### now 重启(1)

```shell
$ shutdown -r 
```

### 重启(2)

```shell
$ reboot 
```

### 注销

```shell
$ logout 
```

---

## 文件和目录

### 进入 home 目录

```shell
$ cd /home 
```

### 返回上一级目录

```shell
$ cd .. 
```

### 返回上两级目录

```shell
cd ../.. 
```

### 进入个人的主目录

```shell
cd 
```

### 进入个人的主目录

```shell
cd ~user
```

### 返回上次所在的目录

```shell
cd - 
```

### 显示工作路径

```shell
pwd
```

### 查看目录中的文件

```shell
ls 
```

### 查看目录中的文件

```shell
ls -F 
```

### 显示文件和目录的详细资料

```shell
ls -l 
```

### 显示隐藏文件

```shell
ls -a
```

### 显示包含数字的文件名和目录名

```shell
ls *[0-9]* 
```

### 显示文件和目录由根目录开始的树形结构(1)

```tree```

```shell
tree
```

### 显示文件和目录由根目录开始的树形结构(2)

```shell
lstree 
```

### 创建一个叫 dir 的目录

```shell
$ mkdir --help
Usage: mkdir [OPTION]... DIRECTORY...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   set file mode (as in chmod), not a=rwx - umask
  -p, --parents     no error if existing, make parent directories as needed
  -v, --verbose     print a message for each created directory
  -Z                   set SELinux security context of each created directory
                         to the default type
      --context[=CTX]  like -Z, or if CTX is specified then set the SELinux
                         or SMACK security context to CTX
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/mkdir>
or available locally via: info '(coreutils) mkdir invocation'
```

```shell
mkdir dir
```

### 同时创建两个目录

```shell
mkdir dir1 dir2 
```

### 创建一个目录树

```shell
mkdir -p /tmp/dir1/dir2 
```

### 删除一个叫 file 的文件

```shell
$ rm --help
Usage: rm [OPTION]... [FILE]...
Remove (unlink) the FILE(s).

  -f, --force           ignore nonexistent files and arguments, never prompt
  -i                    prompt before every removal
  -I                    prompt once before removing more than three files, or
                          when removing recursively; less intrusive than -i,
                          while still giving protection against most mistakes
      --interactive[=WHEN]  prompt according to WHEN: never, once (-I), or
                          always (-i); without WHEN, prompt always
      --one-file-system  when removing a hierarchy recursively, skip any
                          directory that is on a file system different from
                          that of the corresponding command line argument
      --no-preserve-root  do not treat '/' specially
      --preserve-root[=all]  do not remove '/' (default);
                              with 'all', reject any command line argument
                              on a separate device from its parent
  -r, -R, --recursive   remove directories and their contents recursively
  -d, --dir             remove empty directories
  -v, --verbose         explain what is being done
      --help     display this help and exit
      --version  output version information and exit

By default, rm does not remove directories.  Use the --recursive (-r or -R)
option to remove each listed directory, too, along with all of its contents.

To remove a file whose name starts with a '-', for example '-foo',
use one of these commands:
  rm -- -foo

  rm ./-foo

Note that if you use rm to remove a file, it might be possible to recover
some of its contents, given sufficient expertise and/or time.  For greater
assurance that the contents are truly unrecoverable, consider using shred.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/rm>
or available locally via: info '(coreutils) rm invocation'
```

```shell
rm -f file
```

### 删除一个叫 dir 的kong目录

```shell
~$ rmdir --help
Usage: rmdir [OPTION]... DIRECTORY...
Remove the DIRECTORY(ies), if they are empty.

      --ignore-fail-on-non-empty
                  ignore each failure that is solely because a directory
                    is non-empty
  -p, --parents   remove DIRECTORY and its ancestors; e.g., 'rmdir -p a/b/c' is
                    similar to 'rmdir a/b/c a/b a'
  -v, --verbose   output a diagnostic for every directory processed
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/rmdir>
or available locally via: info '(coreutils) rmdir invocation'
```

```shell
rmdir dir
```

### 删除一个叫 dir 的目录并同时删除其内容

```shell
rm -rf dir
```

### 同时删除两个目录及它们的内容

```shell
rm -rf dir1 dir2 
```

### 重命名/移动 一个目录

```shll
$ mv --help
Usage: mv [OPTION]... [-T] SOURCE DEST
  or:  mv [OPTION]... SOURCE... DIRECTORY
  or:  mv [OPTION]... -t DIRECTORY SOURCE...
Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
  -f, --force                  do not prompt before overwriting
  -i, --interactive            prompt before overwrite
  -n, --no-clobber             do not overwrite an existing file
If you specify more than one of -i, -f, -n, only the final one takes effect.
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  move all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 move only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -Z, --context                set SELinux security context of destination
                                 file to default type
      --help     display this help and exit
      --version  output version information and exit

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/mv>
or available locally via: info '(coreutils) mv invocation'
```

```shell
mv old_dir new_dir 
```

### 复制一个文件

```shell
$ cp --help
Usage: cp [OPTION]... [-T] SOURCE DEST
  or:  cp [OPTION]... SOURCE... DIRECTORY
  or:  cp [OPTION]... -t DIRECTORY SOURCE...
Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
  -a, --archive                same as -dR --preserve=all
      --attributes-only        don't copy the file data, just the attributes
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
      --copy-contents          copy contents of special files when recursive
  -d                           same as --no-dereference --preserve=links
  -f, --force                  if an existing destination file cannot be
                                 opened, remove it and try again (this option
                                 is ignored when the -n option is also used)
  -i, --interactive            prompt before overwrite (overrides a previous -n
                                  option)
  -H                           follow command-line symbolic links in SOURCE
  -l, --link                   hard link files instead of copying
  -L, --dereference            always follow symbolic links in SOURCE
  -n, --no-clobber             do not overwrite an existing file (overrides
                                 a previous -i option)
  -P, --no-dereference         never follow symbolic links in SOURCE
  -p                           same as --preserve=mode,ownership,timestamps
      --preserve[=ATTR_LIST]   preserve the specified attributes (default:
                                 mode,ownership,timestamps), if possible
                                 additional attributes: context, links, xattr,
                                 all
      --no-preserve=ATTR_LIST  don't preserve the specified attributes
      --parents                use full source file name under DIRECTORY
  -R, -r, --recursive          copy directories recursively
      --reflink[=WHEN]         control clone/CoW copies. See below
      --remove-destination     remove each existing destination file before
                                 attempting to open it (contrast with --force)
      --sparse=WHEN            control creation of sparse files. See below
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -s, --symbolic-link          make symbolic links instead of copying
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  copy all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 copy only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -x, --one-file-system        stay on this file system
  -Z                           set SELinux security context of destination
                                 file to default type
      --context[=CTX]          like -Z, or if CTX is specified then set the
                                 SELinux or SMACK security context to CTX
      --help     display this help and exit
      --version  output version information and exit

By default, sparse SOURCE files are detected by a crude heuristic and the
corresponding DEST file is made sparse as well.  That is the behavior
selected by --sparse=auto.  Specify --sparse=always to create a sparse DEST
file whenever the SOURCE file contains a long enough sequence of zero bytes.
Use --sparse=never to inhibit creation of sparse files.

When --reflink[=always] is specified, perform a lightweight copy, where the
data blocks are copied only when modified.  If this is not possible the copy
fails, or if --reflink=auto is specified, fall back to a standard copy.
Use --reflink=never to ensure a standard copy is performed.

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

As a special case, cp makes a backup of SOURCE when the force and backup
options are given and SOURCE and DEST are the same name for an existing,
regular file.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/cp>
or available locally via: info '(coreutils) cp invocation'
```

```shell
cp file1 file2 
```

### 复制一个目录下的所有文件到当前工作目录

```shell
cp dir/* . 
```

### 复制一个目录到当前工作目录

```shell
cp -a /tmp/dir1 . 
```

### 复制一个目录

```shell
cp -a dir1 dir2 
```

### 创建一个指向文件或目录 file 的软链接 link

```shell
$ ln --help
Usage: ln [OPTION]... [-T] TARGET LINK_NAME
  or:  ln [OPTION]... TARGET
  or:  ln [OPTION]... TARGET... DIRECTORY
  or:  ln [OPTION]... -t DIRECTORY TARGET...
In the 1st form, create a link to TARGET with the name LINK_NAME.
In the 2nd form, create a link to TARGET in the current directory.
In the 3rd and 4th forms, create links to each TARGET in DIRECTORY.
Create hard links by default, symbolic links with --symbolic.
By default, each destination (name of new link) should not already exist.
When creating hard links, each TARGET must exist.  Symbolic links
can hold arbitrary text; if later resolved, a relative link is
interpreted in relation to its parent directory.

Mandatory arguments to long options are mandatory for short options too.
      --backup[=CONTROL]      make a backup of each existing destination file
  -b                          like --backup but does not accept an argument
  -d, -F, --directory         allow the superuser to attempt to hard link
                                directories (note: will probably fail due to
                                system restrictions, even for the superuser)
  -f, --force                 remove existing destination files
  -i, --interactive           prompt whether to remove destinations
  -L, --logical               dereference TARGETs that are symbolic links
  -n, --no-dereference        treat LINK_NAME as a normal file if
                                it is a symbolic link to a directory
  -P, --physical              make hard links directly to symbolic links
  -r, --relative              create symbolic links relative to link location
  -s, --symbolic              make symbolic links instead of hard links
  -S, --suffix=SUFFIX         override the usual backup suffix
  -t, --target-directory=DIRECTORY  specify the DIRECTORY in which to create
                                the links
  -T, --no-target-directory   treat LINK_NAME as a normal file always
  -v, --verbose               print name of each linked file
      --help     display this help and exit
      --version  output version information and exit

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

Using -s ignores -L and -P.  Otherwise, the last option specified controls
behavior when a TARGET is a symbolic link, defaulting to -P.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/ln>
or available locally via: info '(coreutils) ln invocation'
```

```shell
ln -s file link
```

### 创建一个指向文件或目录 file 的物理链接 link

```shell
ln file link
```

### 修改一个文件或目录 file 的时间戳 - (YYMMDDhhmm)

```shell
touch -t 0712250000 file
```

### file

```shell
$ file p.txt
p.txt: UTF-8 Unicode text
```

### iconv

```shell
$ iconv -l
The following list contains all the coded character sets known.  This does
not necessarily mean that all combinations of these names can be used for
the FROM and TO command line parameters.  One coded character set can be
listed with several different names (aliases).

  437, 500, 500V1, 850, 851, 852, 855, 856, 857, 858, 860, 861, 862, 863, 864,
//..
  WINDOWS-936, WINDOWS-1250, WINDOWS-1251, WINDOWS-1252, WINDOWS-1253,
  WINDOWS-1254, WINDOWS-1255, WINDOWS-1256, WINDOWS-1257, WINDOWS-1258,
  WINSAMI2, WS2, YU
```

通过假设它以 fromEncoding 编码并将其转换为 toEncoding，从给定的输入文件创建一个新文件

```shell
iconv -f fromEncoding -t toEncoding inputFile > outputFile
```

批量调整当前目录中的文件并将它们发送到缩略图目录(需要从 Imagemagick 转换)

---

## 文件搜索

### find

```shell
$ find --help
Usage: find [-H] [-L] [-P] [-Olevel] [-D debugopts] [path...] [expression]

default path is the current directory; default expression is -print
expression may consist of: operators, options, tests, and actions:
operators (decreasing precedence; -and is implicit where no others are given):
      ( EXPR )   ! EXPR   -not EXPR   EXPR1 -a EXPR2   EXPR1 -and EXPR2
      EXPR1 -o EXPR2   EXPR1 -or EXPR2   EXPR1 , EXPR2
positional options (always true): -daystart -follow -regextype

normal options (always true, specified before other expressions):
      -depth --help -maxdepth LEVELS -mindepth LEVELS -mount -noleaf
      --version -xdev -ignore_readdir_race -noignore_readdir_race
tests (N can be +N or -N or N): -amin N -anewer FILE -atime N -cmin N
      -cnewer FILE -ctime N -empty -false -fstype TYPE -gid N -group NAME
      -ilname PATTERN -iname PATTERN -inum N -iwholename PATTERN -iregex PATTERN
      -links N -lname PATTERN -mmin N -mtime N -name PATTERN -newer FILE
      -nouser -nogroup -path PATTERN -perm [-/]MODE -regex PATTERN
      -readable -writable -executable
      -wholename PATTERN -size N[bcwkMG] -true -type [bcdpflsD] -uid N
      -used N -user NAME -xtype [bcdpfls]      -context CONTEXT

actions: -delete -print0 -printf FORMAT -fprintf FILE FORMAT -print 
      -fprint0 FILE -fprint FILE -ls -fls FILE -prune -quit
      -exec COMMAND ; -exec COMMAND {} + -ok COMMAND ;
      -execdir COMMAND ; -execdir COMMAND {} + -okdir COMMAND ;

Valid arguments for -D:
exec, opt, rates, search, stat, time, tree, all, help
Use '-D help' for a description of the options, or see find(1)

Please see also the documentation at http://www.gnu.org/software/findutils/.
You can report (and track progress on fixing) bugs in the "find"
program via the GNU findutils bug-reporting page at
https://savannah.gnu.org/bugs/?group=findutils or, if
you have no web access, by sending email to <bug-findutils@gnu.org>.
```

```shell
find . -maxdepth 1 -name *.jpg -print -exec convert "{}" -resize 80x60 "thumbs/{}" 
```

### 开始进入根文件系统搜索文件和目录 file

```shell
find / -name file
```

### 搜索属于用户 user 的文件和目录

```shell
find / -user user
```

### 在目录 home/user 中搜索带有'.bin' 结尾的文件

```shell
find /home/user -name \*.bin 
```

### n 搜索在过去100天内未被使用过的执行文件

```shell
find /usr/bin -type f -atime +100 
```

### 搜索在10天内被创建或者修改过的文件

```shell
find /usr/bin -type f -mtime -10 
```

### 搜索以 .rpm 结尾的文件并定义其权限

```shell
find / -name \*.rpm -exec chmod 755 
```

### 搜索以 .rpm 结尾的文件，忽略光驱、捷盘等可移动设备

```shell
find / -xdev -name \*.rpm 
```

### 寻找以 .ps 结尾的文件

```shell
locate \*.ps
```

### 显示一个二进制文件、源码或 man 的位置

```shell
whereis halt 
```

### 显示一个二进制文件或可执行文件的完整路径

```shell
which halt 
```

## 挂载一个文件系统

### mount

```shell
$ mount --help

Usage:
 mount [-lhV]
 mount -a [options]
 mount [options] [--source] <source> | [--target] <directory>
 mount [options] <source> <directory>
 mount <operation> <mountpoint> [<target>]

Mount a filesystem.

Options:
 -a, --all               mount all filesystems mentioned in fstab
 -c, --no-canonicalize   don't canonicalize paths
 -f, --fake              dry run; skip the mount(2) syscall
 -F, --fork              fork off for each device (use with -a)
 -T, --fstab <path>      alternative file to /etc/fstab
 -i, --internal-only     don't call the mount.<type> helpers
 -l, --show-labels       show also filesystem labels
 -n, --no-mtab           don't write to /etc/mtab
     --options-mode <mode>
                         what to do with options loaded from fstab
     --options-source <source>
                         mount options source
     --options-source-force
                         force use of options from fstab/mtab
 -o, --options <list>    comma-separated list of mount options
 -O, --test-opts <list>  limit the set of filesystems (use with -a)
 -r, --read-only         mount the filesystem read-only (same as -o ro)
 -t, --types <list>      limit the set of filesystem types
     --source <src>      explicitly specifies source (path, label, uuid)
     --target <target>   explicitly specifies mountpoint
 -v, --verbose           say what is being done
 -w, --rw, --read-write  mount the filesystem read-write (default)
 -N, --namespace <ns>    perform mount in another namespace

 -h, --help              display this help
 -V, --version           display version

Source:
 -L, --label <label>     synonym for LABEL=<label>
 -U, --uuid <uuid>       synonym for UUID=<uuid>
 LABEL=<label>           specifies device by filesystem label
 UUID=<uuid>             specifies device by filesystem UUID
 PARTLABEL=<label>       specifies device by partition label
 PARTUUID=<uuid>         specifies device by partition UUID
 <device>                specifies device by path
 <directory>             mountpoint for bind mounts (see --bind/rbind)
 <file>                  regular file for loopdev setup

Operations:
 -B, --bind              mount a subtree somewhere else (same as -o bind)
 -M, --move              move a subtree to some other place
 -R, --rbind             mount a subtree and all submounts somewhere else
 --make-shared           mark a subtree as shared
 --make-slave            mark a subtree as slave
 --make-private          mark a subtree as private
 --make-unbindable       mark a subtree as unbindable
 --make-rshared          recursively mark a whole subtree as shared
 --make-rslave           recursively mark a whole subtree as slave
 --make-rprivate         recursively mark a whole subtree as private
 --make-runbindable      recursively mark a whole subtree as unbindable

For more details see mount(8).
```

### 挂载一个叫做 hda2 的盘(确定目录 /mnt/hda2 已经存在)

```shell
mount /dev/hda2 /mnt/hda2 
```

### 卸载一个叫做 hda2 的盘 - 先从挂载点 /mnt/hda2 退出

```shell
umount /dev/hda2 
```

### 当设备繁忙时强制卸载

```shell
fuser -km /mnt/hda2 
```

### 运行卸载操作而不写入 /etc/mtab 文件

```shell
umount -n /mnt/hda2 
```

当文件为只读或当磁盘写满时非常有用

### 挂载一个软盘

```shell
mount /dev/fd0 /mnt/floppy 
```

### 挂载一个 cdrom 或 dvdrom

```shell
mount /dev/cdrom /mnt/cdrom 
```

### 挂载一个cdrw或dvdrom

```shell
mount /dev/hdc /mnt/cdrecorder 
```

### 挂载一个 cdrw 或 dvdrom

```shell
mount /dev/hdb /mnt/cdrecorder
```

### 挂载一个文件或 ISO 镜像文件

```shell
mount -o loop file.iso /mnt/cdrom 
```

### 挂载一个 Windows FAT32 文件系统

```shell
mount -t vfat /dev/hda5 /mnt/hda5 
```

### 挂载一个 usb 捷盘或闪存设备

```shell
mount /dev/sda1 /mnt/usbdisk 
```

### 挂载一个 windows 网络共享

```shell
mount -t smbfs -o username=user,password=pass //WinClient/share /mnt/share 
```

---

## 磁盘空间

### 显示已经挂载的分区列表

```shell
df -h 
```

### 以尺寸大小排列文件和目录

```shell
ls -lSr |more 
```

### 估算目录 dir 已经使用的磁盘空间

```shell
du -sh dir
```

### 以容量大小为依据依次显示文件和目录的大小

```shell
du -sk * | sort -rn 
```

### 以大小为依据依次显示已安装的rpm包所使用的空间

```shell
rpm -q -a --qf '%10{SIZE}t%{NAME}n' | sort -k1,1n 
```

fedora, redhat类系统

### 以大小为依据显示已安装的deb包所使用的空间

```shell
dpkg-query -W -f='${Installed-Size;10}t${Package}n' | sort -k1,1n 
```

ubuntu, debian 类系统

---

## 用户和群组

### 创建一个新用户组 group_name

```shell
groupadd group_name 
```

### 删除一个用户组 group_name

```shell
groupdel group_name 
```

### 重命名一个用户组

```shell
groupmod -n new_group_name old_group_name 
```

### 创建一个属于 admin 用户组的用户 user

```shell
useradd -c "Name Surname " -g admin -d /home/user -s /bin/bash user
```

### 创建一个新用户 user

```shell
useradd user
```

### 删除一个用户 user

```shell
userdel -r user
```

-r 排除主目录

### 修改用户 user 属性

```shell
usermod -c "User FTP" -g system -d /ftp/user -s /bin/nologin user 
```

### 修改口令

```shell
passwd
```

### 修改一个用户 user 的口令

```shell
passwd user
```

只允许 root 执行

### 设置用户 user 口令的失效期限

```shell
chage -E 2021-12-31 user
```

### 检查 /etc/passwd 的文件格式和语法修正以及存在的用户

```shell
pwck 
```

### 检查 /etc/passwd 的文件格式和语法修正以及存在的群组

```shell
grpck 
```

### 登陆进一个新的群组以改变新创建文件的预设群组

```shell
newgrp group_name 
```

## 文件的权限 使用 "+" 设置权限，使用 "-" 用于取消

### 显示权限

```shell
ls -lh 
```

### 将终端划分成5栏显示

```shell
ls /tmp | pr -T5 -W$COLUMNS 
```

### 设置目录的权限

```shell
$ chmod --help
Usage: chmod [OPTION]... MODE[,MODE]... FILE...
  or:  chmod [OPTION]... OCTAL-MODE FILE...
  or:  chmod [OPTION]... --reference=RFILE FILE...
Change the mode of each FILE to MODE.
With --reference, change the mode of each FILE to that of RFILE.

  -c, --changes          like verbose but report only when a change is made
  -f, --silent, --quiet  suppress most error messages
  -v, --verbose          output a diagnostic for every file processed
      --no-preserve-root  do not treat '/' specially (the default)
      --preserve-root    fail to operate recursively on '/'
      --reference=RFILE  use RFILE's mode instead of MODE values
  -R, --recursive        change files and directories recursively
      --help     display this help and exit
      --version  output version information and exit

Each MODE is of the form '[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+'.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation at: <https://www.gnu.org/software/coreutils/chmod>
or available locally via: info '(coreutils) chmod invocation'
```

```shell
chmod ugo+rwx directory
```

设置目录 directory 的所有人(u)、群组(g)以及其他人(o)以读(r)、写(w)和执行(x)的权限

### 删除群组(g)与其他人(o)对目录 directory 的读写执行权限

```shell
chmod go-rwx directory
```

### 改变一个文件 file 的所有者 user 属性

```shell
chown user file
```

### 改变一个目录 directory 的所有者 user 属性并同时改变改目录 directory 下所有文件的属性

```shell
chown -R user directory
```

### 改变文件 file 的群组 group

```shell
chgrp group file
```

### 改变一个文件 file 的所有者 user 和群组 group 属性

```shell
chown user:group file
```

### 罗列一个系统中所有使用了 SUID 控制的文件

```shell
find / -perm -u+s 
```

### 设置一个二进制文件 file 的 SUID 位

```shell
chmod u+s /bin/file
```

运行该文件的用户也被赋予和所有者同样的权限

### 禁用一个二进制文件 file 的 SUID 位

```shell
chmod u-s /bin/file
```

### 设置一个目录的 SGID 位

```shell
chmod g+s /home/public
```

类似 SUID ，不过这是针对目录的

### 禁用一个目录的 SGID 位

```shell
$ chmod g-s /home/public 
```

### 设置一个目录的 STIKY 位

```shell
$ chmod o+t /home/public 
```

只允许合法所有人删除文件

### 禁用一个目录的 STIKY 位

```shell
$ chmod o-t /home/public 
```

### 为所有者、所属组和其他用户添加执行的权限

```shell
$ chmod +x filePath
```

文件路径 filePath

### 文件路径 为所有者、所属组和其他用户删除执行的权限

```shell
$ chmod -x filePath
```

### 为所有者添加执行的权限

```shell
$ chmod u+x filePath
```

### 为所属组添加执行的权限

```shell
$ chmod g+x filePath
```

### 为其他用户添加执行的权限

```shell
$ chmod o+x filePath
```

### 为所有者、所属组添加执行的权限

```shell
$ chmod ug+x filePath
```

### 为所有者、所属组和其他用户添加写、执行的权限，取消读权限

```shell
$ chmod =wx filePath
```

### 为所有者、所属组添加写、执行的权限，取消读权限

```shell
$ chmod ug=wx filePath
```

文件路径 filePath

## 文件的特殊属性 ，使用 "+" 设置权限，使用 "-" 用于取消

### 只允许以追加方式读写文件 file

```shell
$ chattr +a file
```

### 允许这个文件 file 能被内核自动压缩/解压

```shell
$ chattr +c file
```

### 在进行文件系统备份时，dump 程序将忽略这个文件 file

```shell
$ chattr +d file
```

### 设置成不可变的文件 file，不能被删除、修改、重命名或者链接

```shell
$ chattr +i file
```

### 允许一个文件 file 被安全地删除

```shell
$ chattr +s file
```

### 一旦应用程序对这个文件 file 执行了写操作，使系统立刻把修改的结果写到磁盘

```shell
$ chattr +S file
```

### 若文件 file 被删除，系统会允许你在以后恢复这个被删除的文件 file

```shell
$ chattr +u file
```

### 显示特殊的属性

```shell
$ lsattr
```

## 打包和压缩文件

### 解压一个叫做 file1.bz2 的文件

```shell
$ bunzip2 file.bz2
```

### 压缩一个叫做 file 的文件

```shell
$ bzip2 file
```

### 解压一个叫做 file.gz 的文件

```shell
$ gunzip file.gz
```

### 压缩一个叫做 file 的文件

```shell
$ gzip file
```

### 最大程度压缩 file 文件

```shell
$ gzip -9 file
```

### 压缩 file 文件创建一个 file.rar 的包

```shell
sudo apt install rar
```

```shell
$ rar a file.rar file
```

### 同时压缩 file1, file2 以及目录 dir1 创建 file.rar 包

```shell
$ rar a file.rar file1 file2 dir1
```

### 解压 file.rar 包

```shell
$ rar x file.rar
```

### 解压 file.rar 包

```shell
$ unrar x file1.rar
```

### 创建一个非压缩的 tarball.tar

```shell
$ tar -cvf archive.tar file
```

### 创建一个包含了 file1, file2 以及 dir1 的档案文件 archive.tar

```shell
$ tar -cvf archive.tar file1 file2 dir1
```

### 显示包 archive.tar 的内容

```shell
$ tar -tf archive.tar
```

### 释放 archive.tar 包

```shell
$ tar -xvf archive.tar
```

### 将压缩包 archive.tar 释放到 /tmp 目录下

```shell
$ tar -xvf archive.tar -C /tmp
```

### 创建一个 bzip2 格式的压缩包 archive.tar.bz2

```shell
$ tar -cvfj archive.tar.bz2 dir
```

### 解压一个 bzip2 格式的压缩包 archive.tar.bz2

```shell
$ tar -xvfj archive.tar.bz2
```

### 创建一个 gzip 格式的压缩包 archive.tar.gz

```shell
$ tar -cvfz archive.tar.gz dir
```

### 解压一个 gzip 格式的压缩包 archive.tar.gz

```shell
$ tar -xvfz archive.tar.gz
```

### 创建一个 zip 格式的压缩包 file.zip

```shell
$ zip file.zip file
```

### 将几个文件和目录同时压缩成一个zip格式的压缩包 file.zip

```shell
$ zip -r file.zip file1 file2 dir1
```

### 解压一个 zip 格式压缩包 file.zip

```shell
$ unzip file.zip
```

### 解压含中文的文件和文件夹名的压缩包

```shell
unzip -O CP936  xxx.zip
```

可防止解压后含中文的文件和文件夹名是乱码

## RPM 包

### 安装一个 rpm 包 package.rpm

```shell
$ rpm -ivh package.rpm
```

### 安装一个 rpm 包而忽略依赖关系警告

```shell
$ rpm -ivh --nodeeps package.rpm
```

### 更新一个 rpm 包但不改变其配置文件

```shell
$ rpm -U package.rpm
```

### 更新一个确定已经安装的 rpm 包

```shell
$ rpm -F package.rpm
```

### 删除一个 rpm 包

```shell
$ rpm -e package.rpm
```

### 显示系统中所有已经安装的 rpm 包

```shell
$ rpm -qa
```

### 显示所有名称中包含 httpd 字样的 rpm 包

```shell
$ rpm -qa | grep httpd
```

### 获取一个已安装包 package 的特殊信息

```shell
$ rpm -qi package
```

### 显示一个组件的 rpm 包

```shell
$ rpm -qg "System Environment/Daemons"
```

### 显示一个已经安装的 rpm 包 package 提供的文件列表

```shell
$ rpm -ql package
```

### 显示一个已经安装的 rpm 包 package 提供的配置文件列表

```shell
$ rpm -qc package
```

### 显示与一个 rpm 包 package 存在依赖关系的列表

```shell
$ rpm -q package --whatrequires
```

### 显示一个 rpm 包 package 所占的体积

```shell
$ rpm -q package --whatprovides
```

### 显示在安装/删除期间所执行的脚本

```shell
$ rpm -q package --scripts
```

### 显示一个 rpm 包 package 的修改历史

```shell
$ rpm -q package --changelog
```

### 确认所给的文件由哪个 rpm 包所提供

```shell
$ rpm -qf /etc/httpd/conf/httpd.conf
```

### 显示由一个尚未安装的 rpm 包提供的文件列表

```shell
$ rpm -qp package.rpm -l
```

### 导入公钥数字证书

```shell
$ rpm --import /media/cdrom/RPM-GPG-KEY
```

### 确认一个 rpm 包的完整性

```shell
$ rpm --checksig package.rpm
```

### 确认已安装的所有 rpm 包的完整性

```shell
$ rpm -qa gpg-pubkey
```

### 检查文件 package 尺寸、 许可、类型、所有者、群组、MD5检查以及最后修改时间

```shell
$ rpm -V package
```

### 检查系统中所有已安装的 rpm 包

```shell
$ rpm -Va
```

小心使用

### 确认一个 rpm 包还未安装

```shell
$ rpm -Vp package.rpm
```

### 从一个 rpm 包运行可执行文件

```shell
$ rpm2cpio package.rpm | cpio --extract --make-directories *bin*
```

### 从一个 rpm 源码安装一个构建好的包

```shell
$ rpm -ivh /usr/src/redhat/RPMS/`arch`/package.rpm
```

### 从一个 rpm 源码构建一个 rpm 包

```shell
$ rpmbuild --rebuild package.src.rpm
```

## YUM 软件包升级器

### 下载并安装一个 rpm 包

```shell
$ yum install package
```

### 将安装一个 rpm 包，使用你自己的软件仓库为你解决所有依赖关系

```shell
$ yum localinstall package.rpm
```

### 更新当前系统中所有安装的 rpm 包

```shell
$ yum update package.rpm
```

### 更新一个 rpm 包

```shell
$ yum update package
```

### 删除一个 rpm 包

```shell
$ yum remove package
```

### 列出当前系统中安装的所有包

```shell
$ yum list
```

### 在 rpm 仓库中搜寻软件包

```shell
$ yum search package
```

### 清理 rpm 缓存删除下载的包

```shell
$ yum clean packages
```

### 删除所有头文件

```shell
$ yum clean headers
```

### 删除所有缓存的包和头文件

```shell
$ yum clean all
```

## deb 包

### 安装/更新一个 deb 包

```shell
$ dpkg -i package.deb
```

### 从系统删除一个 deb 包

```shell
$ dpkg -r package
```

### 显示系统中所有已经安装的 deb 包

```shell
$ dpkg -l
```

### 显示所有名称中包含 httpd 字样的 deb 包

```shell
$ dpkg -l | grep httpd
```

### 获得已经安装在系统中一个特殊包的信息

```shell
$ dpkg -s package
```

### 显示系统中已经安装的一个 deb 包所提供的文件列表

```shell
$ dpkg -L package 
```

### 显示尚未安装的一个包所提供的文件列表

```shell
$ dpkg --contents package.deb
```

### 确认所给的文件由哪个 deb 包提供

```shell
$ dpkg -S /bin/ping
```

### 软件工具

```shell
$ APT
```

Debian, Ubuntu 以及类似系统

### 安装/更新一个 deb 包

```shell
$ apt-get install package
```

### 从光盘安装/更新一个 deb 包

```shell
$ apt-cdrom install package
```

### 升级列表中的软件包

```shell
$ apt-get update
```

### 升级所有已安装的软件

```shell
$ apt-get upgrade
```

### 从系统删除一个deb包

```shell
$ apt-get remove package
```

### 确认依赖的软件仓库正确

```shell
$ apt-get check
```

### 从下载的软件包中清理缓存

```shell
$ apt-get clean
```

### 返回包含所要搜索字符串的软件包名称

```shell
$ apt-cache search searched-package
```

## 查看文件内容

### 从第一个字节开始正向查看文件的内容

```shell
$ cat file1
```

### 从最后一行开始反向查看一个文件的内容

```shell
$ tac file1
```

### 查看一个长文件的内容

```shell
$ more file1
```

### 类似于 'more' 命令，但是它允许在文件中和正向操作一样的反向操作

```shell
$ less file1
```

### 查看一个文件的前两行

```shell
$ head -2 file1
```

### 查看一个文件的最后两行

```shell
$ tail -2 file1
```

### 实时查看被添加到一个文件中的内容

```shell
$ tail -f /var/log/messages
```

## 文本处理

### 合并一个文件的详细说明文本，并将简介写入一个新文件中

```shell
$ cat file1 | command( sed, grep, awk, grep, etc...) > result.txt
```

### 合并一个文件的详细说明文本，并将简介写入一个已有的文件中

```shell
$ cat file1 | command( sed, grep, awk, grep, etc...) >> result.txt
```

### 在文件 '/var/log/messages'中查找关键词"Aug"

```shell
$ grep Aug /var/log/messages
```

### 在文件 '/var/log/messages'中查找以"Aug"开始的词汇

```shell
$ grep ^Aug /var/log/messages
```

### 选择 '/var/log/messages' 文件中所有包含数字的行

```shell
$ grep [0-9] /var/log/messages
```

### 在目录 '/var/log' 及随后的目录中搜索字符串"Aug"

```shell
$ grep Aug -R /var/log/*
```

### 将example.txt文件中的 "string1" 替换成 "string2"

```shell
$ sed 's/stringa1/stringa2/g' example.txt
```

### 从example.txt文件中删除所有空白行

```shell
$ sed '/^$/d' example.txt
```

### 合并上下单元格内容

```shell
$ echo 'esempio' | tr '[:lower:]' '[:upper:]'
```

### 从文件example.txt 中排除第一行

```shell
$ sed -e '1d' result.txt
```

### 查看只包含词汇 "string1"的行

```shell
$ sed -n '/stringa1/p'
```

### 删除每一行最后的空白字符

```shell
$ sed -e 's/ *$//' example.txt
```

### 从文档中只删除词汇 "string1" 并保留剩余全部

```shell
$ sed -e 's/stringa1//g' example.txt
```

### 查看从第一行到第5行内容

```shell
$ sed -n '1,5p;5q' example.txt
```

### 查看第5行

```shell
$ sed -n '5p;5q' example.txt
```

### 用单个零替换多个零

```shell
$ sed -e 's/00*/0/g' example.txt
```

### 标示文件的行数

```shell
$ cat -n file1
```

### 删除example.txt文件中的所有偶数行

```shell
$ cat example.txt | awk 'NR%2==1'
```

### 查看一行第一栏

```shell
$ echo a b c | awk '{print $1}'
```

### 查看一行的第一和第三栏

```shell
$ echo a b c | awk '{print $1,$3}'
```

### 合并两个文件或两栏的内容

```shell
$ paste file1 file2
```

### 合并两个文件或两栏的内容，中间用"+"区分

```shell
$ paste -d '+' file1 file2
```

### 排序两个文件的内容

```shell
$ sort file1 file2
```

### 取出两个文件的并集(重复的行只保留一份)

```shell
$ sort file1 file2 | uniq
```

### 删除交集，留下其他的行

```shell
$ sort file1 file2 | uniq -u
```

### 取出两个文件的交集(只留下同时存在于两个文件中的文件)

```shell
$ sort file1 file2 | uniq -d
```

### 比较两个文件的内容只删除 'file1' 所包含的内容

```shell
$ comm -1 file1 file2
```

### 比较两个文件的内容只删除 'file2' 所包含的内容

```shell
$ comm -2 file1 file2
```

### 比较两个文件的内容只删除两个文件共有的部分

```shell
$ comm -3 file1 file2
```

## 字符设置和文件格式转换

### 将一个文本文件的格式从MSDOS转换成UNIX

```shell
$ dos2unix filedos.txt fileunix.txt
```

### 将一个文本文件的格式从UNIX转换成MSDOS

```shell
$ unix2dos fileunix.txt filedos.txt
```

### 将一个文本文件转换成html

```shell
$ recode ..HTML < page.txt > page.html
```

### 显示所有允许的转换格式

```shell
$ recode -l | more
```

## 文件系统分析

### 检查磁盘hda1上的坏磁块

```shell
$ badblocks -v /dev/hda1
```

### 修复/检查hda1磁盘上linux文件系统的完整性

```shell
$ fsck /dev/hda1
```

### 修复/检查hda1磁盘上ext2文件系统的完整性

```shell
$ fsck.ext2 /dev/hda1
```

### 修复/检查hda1磁盘上ext2文件系统的完整性

```shell
$ e2fsck /dev/hda1
```

### 修复/检查hda1磁盘上ext3文件系统的完整性

```shell
$ e2fsck -j /dev/hda1
```

### 修复/检查hda1磁盘上ext3文件系统的完整性

```shell
$ fsck.ext3 /dev/hda1
```

### 修复/检查hda1磁盘上fat文件系统的完整性

```shell
$ fsck.vfat /dev/hda1
```

### 修复/检查hda1磁盘上dos文件系统的完整性

```shell
$ fsck.msdos /dev/hda1
```

### 修复/检查hda1磁盘上dos文件系统的完整性

```shell
$ dosfsck /dev/hda1
```

## 初始化一个文件系统

### 在hda1分区创建一个文件系统

```shell
$ mkfs /dev/hda1
```

### 在hda1分区创建一个linux ext2的文件系统

```shell
$ mke2fs /dev/hda1
```

### 在hda1分区创建一个linux ext3(日志型)的文件系统

```shell
$ mke2fs -j /dev/hda1
```

### 创建一个 FAT32 文件系统

```shell
$ mkfs -t vfat 32 -F /dev/hda1
```

### 格式化一个软盘

```shell
$ fdformat -n /dev/fd0
```

## SWAP文件系统

### 创建一个swap文件系统

```shell
$ mkswap /dev/hda3
```

### 启用一个新的swap文件系统

```shell
$ swapon /dev/hda3
```

### 启用两个swap分区

```shell
$ swapon /dev/hda2 /dev/hdb3
```

## 备份

### 制作一个 '/home' 目录的完整备份

```shell
$ dump -0aj -f /tmp/home0.bak /home
```

### 制作一个 '/home' 目录的交互式备份

```shell
$ dump -1aj -f /tmp/home0.bak /home
```

### 还原一个交互式备份

```shell
$ restore -if /tmp/home0.bak
```

### 同步两边的目录

```shell
$ rsync -rogpav --delete /home /tmp
```

### 通过SSH通道rsync

```shell
$ rsync -rogpav -e ssh --delete /home ip_address:/tmp
```

### 通过ssh和压缩将一个远程目录同步到本地目录

```shell
$ rsync -az -e ssh --delete ip_addr:/home/public /home/local
```

### 通过ssh和压缩将本地目录同步到远程目录

```shell
$ rsync -az -e ssh --delete /home/local ip_addr:/home/public
```

### 通过ssh在远程主机上执行一次备份本地磁盘的操作

```shell
$ dd bs=1M if=/dev/hda | gzip | ssh user@ip_addr 'dd of=hda.gz'
```

### 备份磁盘内容到一个文件

```shell
$ dd if=/dev/sda of=/tmp/file1
```

### 执行一次对 '/home/user' 目录的交互式备份操作

```shell
$ tar -Puf backup.tar /home/user
```

### 通过ssh在远程目录中复制一个目录内容

```shell
$ ( cd /tmp/local/ && tar c . ) | ssh -C user@ip_addr 'cd /home/share/ && tar x -p'
```

### 通过ssh在远程目录中复制一个本地目录

```shell
$ ( tar c /home ) | ssh -C user@ip_addr 'cd /home/backup-home && tar x -p'
```

### 本地将一个目录复制到另一个地方，保留原有权限及链接

```shell
$ tar cf - . | (cd /tmp/backup ; tar xf - )
```

### 从一个目录查找并复制所有以 '.txt' 结尾的文件到另一个目录

```shell
$ find /home/user1 -name '*.txt' | xargs cp -av --target-directory=/home/backup/ --parents
```

### 查找所有以 '.log' 结尾的文件并做成一个bzip包

```shell
$ find /var/log -name '*.log' | tar cv --files-from=- | bzip2 > log.tar.bz2
```

### 做一个将 MBR (Master Boot Record)内容复制到软盘的动作

```shell
$ dd if=/dev/hda of=/dev/fd0 bs=512 count=1
```

### 从已经保存到软盘的备份中恢复MBR内容

```shell
$ dd if=/dev/fd0 of=/dev/hda bs=512 count=1
```

## 光盘

### 清空一个可复写的光盘内容

```shell
$ cdrecord -v gracetime=2 dev=/dev/cdrom -eject blank=fast -force
```

### 在磁盘上创建一个光盘的iso镜像文件

```shell
$ mkisofs /dev/cdrom > cd.iso
```

### 在磁盘上创建一个压缩了的光盘iso镜像文件

```shell
$ mkisofs /dev/cdrom | gzip > cd_iso.gz
```

### 创建一个目录的iso镜像文件

```shell
$ mkisofs -J -allow-leading-dots -R -V "Label CD" -iso-level 4 -o ./cd.iso data_cd
```

### 刻录一个ISO镜像文件

```shell
$ cdrecord -v dev=/dev/cdrom cd.iso
```

### 刻录一个压缩了的ISO镜像文件

```shell
$ gzip -dc cd_iso.gz | cdrecord dev=/dev/cdrom -
```

### 挂载一个ISO镜像文件

```shell
$ mount -o loop cd.iso /mnt/iso
```

### 从一个CD光盘转录音轨到 wav 文件中

```shell
$ cd-paranoia -B
```

### 从一个CD光盘转录音轨到 wav 文件中（参数-3）

```shell
$ cd-paranoia -- "-3"
```

### 扫描总线以识别scsi通道

```shell
$ cdrecord --scanbus
```

### 校验一个设备的md5sum编码，例如一张 CD

```shell
$ dd if=/dev/hdc | md5sum
```

## 网络（以太网和WIFI无线）

### 显示一个以太网卡的配置

```shell
$ ifconfig eth0
```

### 启用一个 'eth0' 网络设备

```shell
$ ifup eth0
```

### 禁用一个 'eth0' 网络设备

```shell
$ ifdown eth0
```

### 控制IP地址

```shell
$ ifconfig eth0 192.168.1.1 netmask 255.255.255.0
```

### 设置 'eth0' 成混杂模式以嗅探数据包 (sniffing)

```shell
$ ifconfig eth0 promisc
```

### 以dhcp模式启用 'eth0'

```shell
$ dhclient eth0
```

```shell
route -n show routing table
route add -net 0/0 gw IP_Gateway configura default gateway
route add -net 192.168.0.0 netmask 255.255.0.0 gw 192.168.1.1 configure static route to reach network '192.168.0.0/16'
route del 0/0 gw IP_gateway remove static route
echo "1" > /proc/sys/net/ipv4/ip_forward activate ip routing
hostname show hostname of system
host www.example.com lookup hostname to resolve name to ip address and viceversa(1)
nslookup www.example.com lookup hostname to resolve name to ip address and viceversa(2)
ip link show show link status of all interfaces
mii-tool eth0 show link status of 'eth0'
ethtool eth0 show statistics of network card 'eth0'
netstat -tup show all active network connections and their PID
netstat -tupl show all network services listening on the system and their PID
tcpdump tcp port 80 show all HTTP traffic
iwlist scan show wireless networks
iwconfig eth1 show configuration of a wireless network card
hostname show hostname
host www.example.com lookup hostname to resolve name to ip address and viceversa
nslookup www.example.com lookup hostname to resolve name to ip address and viceversa
whois www.example.com lookup on Whois database
```

## 列出目录内容

### 显示所有文件(包括隐藏文件)

```shell
$ ls -a
```

Linux 中以.开头的文件是隐藏文件

### 显示详细信息

```shell
$ ls -l
```

### 递归显示子目录结构

```shell
$ ls -R
```

### 显示目录和链接信息

```shell
$ ls -ld
```

### 历史记录中所搜命令(输入命令中的任意一个字符)

```shell
$ ctrl+r
```

### 显示当前目录

```shell
$ pwd
```

## 查看文件的类型

### 查看文件的类型

```shell
$ file
```

## 复制文件目录

### cp

cp: 复制文件和目录

```shell
cp 源文件(文件夹) 目标文件(文件夹)
```

常用参数:

```shell
-r  递归复制整个目录树
-v  显示详细信息
```

复制文件夹时要在 ```cp``` 命令后面加一个 ```-r``` 参数

```shell
cp -r 源文件夹 目标文件夹
```

### touch

```shell
touch+文件名
```

当文件不存在的时候，创建相应的文件；当文件存在的时候，修改文件的创建时间。

功能：生成一个空文件或修改文件的存取/修改的时间记录值。

将当前下的文件时间修改为系统的当前时间

```shell
touch *
```

将 test 文件的日期改为 20040210

```shell
touch –d 20040210 test
```

若abc文件存在，则修改为系统的当前时间；若不存在，则生成一个为当前时间的空文件

```shell
touch abc　
```

### mv

```shell
mv 文件 目标目录
```

移动或重命名文件或目录(如果指定文件名，则可以重命名文件)。可以将文件及目录移到另一目录下，或更改文件及目录的名称。

格式为：

```shell
mv [参数]<源文件或目录> <目标文件或目录>
```

将 a.txt 文件移动上层目录

```shell
mva.txt ../
```

将 a.txt 改名为 b.txt

```shell
mv a.txt b.txt
```

将 dir 目录上移一层

```shell
mv dir ../
```

### rm

删除文件，常用参数：

```shell
-i  交互式   
-r  递归的删除包括目录中的所有内容
```

删除文件夹(只能删除空文件夹)

```shell
rmdir 文件夹名称：
```

删除文件夹(空文件夹和非空文件夹都可删除)

```shell
rm -r 文件夹名称
```

### mkdir

创建文件夹

```shell
mkdir 文件夹名称
```

7、mkdir -p dir1/dir2 ：在当前目录下创建dir1目录，并在dir1目录下创建dir2目录， 也就是连续创建两个目录（dir1/和dir1/dir2）

8、rmdir –p dir1/dir2：删除dir1下的dir2目录，若dir1目录为空也删除它

9、rm * ：删除当前目录下的所有文件

10、-f参数：强迫删除文件 rm –f  *.txt：强迫删除所有以后缀名为txt文件

11、-i参数：删除文件时询问

```shell
rm　–i  * ：删除当前目录下的所有文件会有如下提示：
rm:backup:is a directory　　　 遇到目录会略过
rm: remove ‘myfiles.txt’ ? Y
删除文件时会询问,可按Y或N键表示允许或拒绝删除文件　
```

12、-r参数：递归删除（连子目录一同删除，这是一个相当常用的参数）

```shell
rm  -r test ：删除test目录（含test目录下所有文件和子目录）
rm  -r  *：删除所有文件（含当前目录所有文件、所有子目录和子目录下的文件） 一般在删除目录时r和f一起用，避免麻烦
rm  -rf test ：强行删除、不加询问
```

13、grep：功能：在文件中搜索匹配的字符并进行输出

```shell
格式：grep[参数] <要找的字串> <要寻找字 串的源文件>
greplinux test.txt：搜索test.txt文件中字符串linux并输出
```

14、ln命令

功能：在文件和目录之间建立链接 格式：ln [参数] <源文件或目录> <目标文件或目录>
链接分“软链接”和“硬链接”

1.软链接:

```shell
ln–s /usr/share/do  doc ：创建一个链接文件doc,并指向目录/usr/share/do

```

2.硬链接:

```shell
ln  /usr/share/test  hard：创建一个硬链接文件hard，这时对于test文件对应 的存储区域来说，又多了一个文件指向它
```

## 系统常用命令

1、显示命令

```shell
date:查看或设置当前系统的时间：格式化显示时间：+%Y--%m--%d；
date -s:设置当前系统的时间
hwclock(clock)：显示硬件时钟时间(需要管理员权限)；
cal：查看日历
格式cal [参数] 月年
cal：显示当月的日历   cal4 2004 ：显示2004年4月的日历
cal- y 2003：显示2003年的日历
uptime：查看系统运行时间
```

2、输出查看命令

```shell
echo：显示输入的内容  追加文件echo "liuyazhuang" >> liuyazhuang.txt
cat：显示文件内容,也可以将数个文件合并成一个文件。
格式：格式：cat[参数]<文件名>
cat  test.txt：显示test.txt文件内容
cat  test.txt | more  ：逐页显示test.txt文件中的内容
cat  test.txt >> test1.txt ：将test.txt的内容附加到test1.txt文件之后
cat  test.txt test2.txt >readme.txt　: 将test.txt和test2.txt文件合并成readme.txt 文件
head:显示文件的头几行（默认10行） -n:指定显示的行数格式：head -n 文件名
tail：显示文件的末尾几行（默认10行）-n：指定显示的行数   -f：追踪显示文件更新 （一般用于查看日志，命令不会退出，而是持续显示新加入的内容）
格式：格式：tail[参数]<文件名>
tail-10 /etc/passwd ：显示/etc/passwd/文件的倒数10行内容
tail+10 /etc/passwd ：显示/etc/passwd/文件从第10行开始到末尾的内容
more：用于翻页显示文件内容（只能向下翻页）
more命令是一般用于要显示的内容会超过一个画面长度的情况。为了避免画  面显示时瞬间就闪过去，用户可以使用more命令，让画面在显示满一页时暂停，此时可按空格健继续显示下一个画面，或按Q键停止显示。
ls  -al  |more：以长格形式显示etc目录下的文件列表，显示满一个画面便暂停，可 按空格键继续显示下一画面，或按Q键跳离
less：翻页显示文件内容（带上下翻页）按下上键分页，按q退出、‘
less命令的用法与more命令类似，也可以用来浏览超过一页的文件。所不同  的是less 命令除了可以按空格键向下显示文件外，还可以利用上下键来卷动文件。当要结束浏览时，只要在less命令的提示符“：”下按Q键即可。
ls  -al | less：以长格形式列出/etc目录中所有的内容。用户可按上下键浏览或按Q键跳离
```

3、查看硬件信息

```shell
Ispci：查看PCI设备  -v：查看详细信息
Isusb：查看USB设备 -v：查看详细信息
Ismod：查看加载的模块(驱动)
```

4、关机、重启

```shell
shutdown关闭、重启计算机
shutdown[关机、重启]时间  -h关闭计算机   -r：重启计算机
如：立即关机：shutdown -h now
10分钟后关机：shutdown -h +10
23:30分关机：shutdown -h 23:30
立即重启：shutdown -r now
poweroff：立即关闭计算机
reboot：立即重启计算机
```

5、归档、压缩

```shell
zip:压缩文件  zip liuyazhuang.zip myfile  格式为：“zip 压缩后的zip文件文件名”
unzip：解压文件  unzip liuyazhuang.zip
gzip：压缩文件 gzip 文件名
tar：归档文件
tar -cvf out.tar liuyazhuang  打包一个归档（将文件"liuyazhuang"打包成一个归档）
tar -xvf liuyazhuang.tar     释放一个归档（释放liuyazhuang.tar归档）
tar -cvzf backup.tar.gz/etc  
-z参数将归档后的归档文件进行gzip压缩以减少大小。
-c：创建一个新tar文件
-v：显示运行过程的信息
-f：指定文件名
-z：调用gzip压缩命令进行压缩
-t：查看压缩文件的内容
-x：解开tar文件
tar  -cvf test.tar  *：将所有文件打包成test.tar,扩展名.tar需自行加上
tar  -zcvf test.tar.gz  *：将所有文件打包成test.tar,再用gzip命令压缩
tar -tf   test.tar ：查看test.tar文件中包括了哪些文件
tar -xvf test.tar       将test.tar解开
tar -zxvf foo.tar.gz   解压缩
gzip各gunzip命令
gziptest.txt ：压缩文件时，不需要任何参数
gizp–l test.txt.gz：显示压缩率
```

6、查找

locate：快速查找文件、文件夹：locate keyword 此命令需要预先建立数据库，数据库默认每天更新一次，可用updatedb命令手工建立、更新数据库。欢迎关注我们，公号终码一生。 find查找位置查找参数 如：

```shell
find . -name *liuyazhuang* 查找当前目录下名称中含有"liuyazhuang"的文件
find / -name *.conf  查找根目录下（整个硬盘）下后缀为.conf的文件
find / -perm 777 查找所有权限是777的文件
find / -type d 返回根目录下所有的目录
find . -name "a*"-exec ls -l {} \;
find功能：用来寻找文件或目录。
格式：find [<路径>] [匹配条件]
find / -name httpd.conf  搜索系统根目录下名为httpd.conf的文件
```

7、ctrl+c :终止当前的命令

8、who或w命令

功能：查看当前系统中有哪些用户登录 格式：who/w[参数]

9、dmesg命令

功能：显示系统诊断信息、操作系统版本号、物理内存的大小以及其它信息

10、df命令

功能：用于查看文件系统的各个分区的占用情况

11、du命令

功能：查看某个目录中各级子目录所使用的硬盘空间数 格式：du [参数] <目录名>

12、free命令

功能：用于查看系统内存，虚拟内存（交换空间）的大小占用情况

## VIM

VIM是一款功能强大的命令行文本编辑器，在Linux中通过vim命令可以启动vim编辑器。 一般使用vim + 目标文件路径 的形式使用vim

如果目标文件存在，则vim打开目标文件，如果目标文件不存在，则vim新建并打开该文件

```shell
:q：退出vim编辑器
```

VIM模式

vim拥有三种模式：

（1）命令模式（常规模式）

vim启动后，默认进入命令模式，任何模式都可以通过esc键回到命令模式（可以多按几次），命令模式下可以键入不同的命令完成选择、复制、粘贴、撤销等操作。 命名模式常用命令如下：

```shell
i : 在光标前插入文本；
o:在当前行的下面插入新行；
dd:删除整行；
yy：将当前行的内容放入缓冲区（复制当前行）
n+yy :将n行的内容放入缓冲区（复制n行）
p:将缓冲区中的文本放入光标后（粘贴）
u：撤销上一个操作
r:替换当前字符
/ 查找关键字
```

（2）插入模式

在命令模式下按 " i "键，即可进入插入模式，在插入模式可以输入编辑文本内容，使用esc键可以返回命令模式。

（3）ex模式

在命令模式中按" : "键可以进入ex模式，光标会移动到底部，在这里可以保存修改或退出vim. ext模式常用命令如下：

```shell
:w ：保存当前的修改
:q ：退出
:q! ：强制退出，保存修改
:x  :保存并退出，相当于:wq
:set number 显示行号
:! 系统命令  执行一个系统命令并显示结果
:sh ：切换到命令行，使用ctrl+d切换回vim
28. 软件包管理命令(RPM)
```

1、软件包的安装

使用RPM命令的安装模式可以将软件包内所有的组件放到系统中的正确路径，安装软件包的命令是:

```shell
rpm –ivh wu-ftpd-2.6.2-8.i386.rpm
i：作用rpm的安装模式 v: 校验文件信息h: 以＃号显示安装进度
```

2、软件包的删除

删除模式会将指定软件包的内容全部删除，但并不包括已更改过的配置文件，删除RPM软件包的命令如下：

```shell
rpm –e  wu-ftpd
```

注意：这里必须使用软件名“wu-ftpd”或”wu-ftpd-2.6.2-8而不是使用当初安装时的软件包名.wu-ftpd-2.6.2-8.i386.rpm

3、软件包升级

升级模式会安装用户所指定的更新版本，并删除已安装在系统中的相同软件包，升级软件包命令如下：

```shell
rpm –Uvh wu-ftpd-2.6.2-8.i386.rpm  –Uvh：升级参数
```

4、软件包更新

更新模式下，rpm命令会检查在命令行中所指定的软件包是否比系统中原有的软件
包更新。如果情况属实，rpm命令会自动更新指定的软件包；反之，若系统中并没有指定软件包的较旧版本，rpm命令并不会安装此软件包。而在升级模式下，不管系统中是否有较旧的版本，rpm命令都会安装指定的软件包。

```shell
rpm –Fvhwu-ftpd-2.6.2-8.i386.rpm   -Fvh：更新参数
```

5、软件包查询

若要获取RPM软件包的相关信息，可以使用查询模式。

使用-q参数可查询一个已 安装的软件包的内容

```shell
rpm  –q wu-ftpd
```

查询软件包所安装的位置：

```shell
rpm –ql package-name
rpm –ql xv (l参数：显示文件列表)
```

