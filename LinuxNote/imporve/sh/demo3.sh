#!/bin/bash
read -p "Please input yes or no: " anw
case $anw in
[yY][eE][sS] | [yY])
  echo yes
  ;;
[nN][oO] | [nN])
  echo no
  ;;
*)
  echo false
  ;;
esac
