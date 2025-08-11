#!/bin/bash

# Clear the screen for a clean output
clear

echo "================================="
echo "      System Information         "
echo "================================="
echo ""

# Use the 'whoami' command to get the current user
echo "Current User: $(whoami)"
echo ""

# Use the 'uptime -p' command for a "pretty" uptime format
echo "System Uptime: $(uptime -p)"
echo ""

# Use the 'date' command for the current date and time
echo "Date and Time: $(date)"
echo ""

echo "================================="


