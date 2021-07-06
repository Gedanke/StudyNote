#!/bin/bash
if [ $# -eq 0 ]; then
  echo "Please input a arg(eg:$(basename $0) arg1)"
  exit 1
else
  while [ -n "$1" ]; do
    useradd $1 &>/dev/null
    shift
  done
fi
