#!/usr/bin/bash
awk '{print substr($4, 2, 11) " " $1}' access.log |
  sort | uniq |
  awk '{uv[$1]++;next}END{for (ip in uv) print ip, uv[ip]}'
