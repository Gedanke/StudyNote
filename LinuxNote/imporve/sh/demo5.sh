#!/bin/bash
for ((i = 1, num = 0; i <= 100; i++)); do
  [ $((i % 2)) -eq 1 ] && let sum+=i
done
echo sum=$sum
