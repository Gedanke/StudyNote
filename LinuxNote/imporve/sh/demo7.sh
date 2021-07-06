#!/bin/bash
until pgrep -u xiaoming &>/dev/null; do
  sleep 0.5
done
pkill -9 -u xiaoming
