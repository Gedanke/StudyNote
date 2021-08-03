#!/usr/bin/bash
readarray -t ips < iplist
for ip in ${ips[@]}
do
  ssh ./transfer_key.sh $ip
done
