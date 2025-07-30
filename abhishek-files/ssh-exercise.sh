#!/bin/bash

# A script to perform basic server setup for a new user.

# --- Step 1: Update Ubuntu Packages ---
# It's good practice to update the package lists and upgrade installed packages.
echo "Updating and upgrading system packages..."
sudo apt-get update && sudo apt-get upgrade -y
echo "Package update complete."

# --- Step 2: Add SSH Key for a New User ---
# Replace 'newuser' with the actual username.
# Replace 'ssh-rsa AAAA...' with the user's actual public SSH key.

echo "Configuring SSH access for user: $USERNAME"

# Create the .ssh directory if it doesn't exist
sudo mkdir -p /home/newuser/.ssh

# Add the public key to the authorized_keys file
echo "ssh-rsa AAAA... your-email@example.com" > /home/newuser/.ssh/authorized_keys


# Set the correct permissions for security
sudo chown -R newuser:newuser $SSH_DIR
sudo chmod 700 /home/newuser/.ssh
sudo chmod 600 /home/newuser/.ssh/authorized_keys

echo "SSH key added and permissions set for $USERNAME."
echo "Setup complete!"