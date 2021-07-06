#!/bin/bash
for a in {1..9}; do
  for b in $(seq 1 $a); do
    let c=$a*$b
    echo -e "${a}x${b}=$c\t\c"
  done
  echo
done
