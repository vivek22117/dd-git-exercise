#!/bin/bash

# A script to perform basic server setup for a new user.

# --- Step 1: Update Ubuntu Packages ---
# It's good practice to update the package lists and upgrade installed packages.
echo "Updating and upgrading system packages..."
sudo apt-get update && sudo apt-get upgrade -y
echo "Package update complete."

# --- Step3: Add new user ---
# Replace 'newuser' with the actual username.
sudo adduser newuser

# --- Step 2: Add SSH Key for a New User ---
# Replace 'newuser' with the actual username.
# Replace 'ssh-rsa AAAA...' with the user's actual public SSH key.

echo "Configuring SSH access for user: $USERNAME"

