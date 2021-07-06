#!/bin/bash
read -p "Please input your score: " score
if [[ $score =~ [^0-9] ]]; then
  echo "please input a int"
  exit 10
elif [ $score -gt 100 ]; then
  echo "Your score is wrong"
  exit 20
elif [ $score -ge 85 ]; then
  echo "Your score is very good"
elif [ $score -ge 60 ]; then
  echo "Your score is soso"
else
  echo "You are loser"
fi
