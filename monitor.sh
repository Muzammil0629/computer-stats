#!/bin/bash

echo "================================="
echo "SERVER HEALTH DASHBOARD"
echo "================================="

echo ""
echo "Hostname:"
hostname

echo ""
echo "Current Date & Time:"
date

echo ""
echo "System Uptime:"
uptime -p

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h /

echo ""
echo "CPU Information:"
top -bn1 | grep "Cpu"
