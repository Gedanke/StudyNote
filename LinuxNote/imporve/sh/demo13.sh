#!/bin/bash
read -p "Please input network (eg:192.168.0.0): " net
echo $net | egrep -o "\<(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\>"
[ $? -eq 0 ] || (
  echo "input error"
  exit 10
)
IP=$(echo $net | egrep -o "^([0-9]{1,3}\.){3}")
for i in {1..254}; do
  {
    ping -c 1 -w 1 $IP$i &>/dev/null &&
      echo "$IP$i is up"
  } &

done
wait
