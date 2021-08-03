#!/bin/bash
$ sudo useradd -m -d /home/user user
$ sudo passwd user
$ sudo usermod -G sudo user
$ sudo usermod --shell /bin/bash user
$ sudo cp ~/.bashrc /home/user/
$ sudo chown user.user /home/user/.bashrc
$ sduo sh -c 'echo "user ALL=(ALL) NOPASSWD:ALL">>/etc/sudoers'