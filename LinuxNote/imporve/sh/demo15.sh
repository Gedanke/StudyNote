#!/bin/bash
trap '' 2
trap -p
for ((i = 0; i < 3; i++)); do
  sleep 1
  echo $i
done
trap '-' SIGINT
for ((i = 3; i < 10; i++)); do
  sleep 1
  echo $i
done
