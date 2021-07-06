#!/bin/bash
sum=0
i=1
while [ $i -le 100 ]; do
  if [ $(($i % 2)) -ne 0 ]; then
    let sum+=i
    let i++
  else
    let i++
  fi
done
echo "sum is $sum"
