#!/bin/bash

# Define the log file location
LOG_FILE="/var/log/custom_script.log"

echo "Starting the custom process monitoring script." >> $LOG_FILE

# Loop forever
while true; do
  # Append the current date and a message to the log file
  echo "Process is alive at: $(date)" >> $LOG_FILE
  # Wait for 5 seconds
  sleep 5
done
