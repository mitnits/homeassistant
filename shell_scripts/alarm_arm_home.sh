#!/bin/bash
rc=999
max_retries=5
while [ ${rc} -ne 0 -a ${max_retries} -gt 0 ]; do
    python3 /home/homeassistant/.homeassistant/shell_scripts/alarm_arm_home.py
    rc=$?
    max_retries=$(($max_retries-1))
done
