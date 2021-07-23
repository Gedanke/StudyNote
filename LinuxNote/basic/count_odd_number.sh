#!/usr/bin/env bash
# 用于计算数组中奇数的和
# @author liyangyang
# @time 2019/09/17
sum=0
for num in 1 2 3 4; do
  re=${num}%2
  if ((${re} == 1)); then
    sum=$((${sum} + ${num}))
  fi
done
echo ${sum}
