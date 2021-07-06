#!/bin/bash
sum=0
for i in {1..100}; do
  [ $i -eq 51 ] && break
  [ $(($i % 2)) -eq 1 ] && {
    let sum+=i
    let i++
  }
done
echo sum=$sum
