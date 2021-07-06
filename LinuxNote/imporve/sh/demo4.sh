#!/bin/bash
sum=0
read -p "Please input a positive integer: " num
if [[ $num =~ [^0-9] ]]; then
  echo "input error"
elif [[ $num -eq 0 ]]; then
  echo "input error"
else
  for i in $(seq 1 $num); do
    sum=$(($sum + $i))
  done
  echo $sum
fi
unset zhi
