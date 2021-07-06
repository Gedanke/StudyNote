#!/bin/bash
trap 'echo press ctrl+c' 2
for ((i = 0; i < 10; i++)); do
  sleep 1
  echo $i
done
