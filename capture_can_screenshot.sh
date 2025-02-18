#!/bin/bash

# Define the directory where screenshots will be saved
SAVE_DIR="$HOME/CAN-Bus-Spoofing-Attack"

# Create the directory if it doesn't exist
mkdir -p "$SAVE_DIR"

# Generate a timestamp for the screenshot filename
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Define the screenshot filename
FILENAME="can_screenshot_$TIMESTAMP.png"

# Capture the screenshot and save it in the specified directory
import -window root "$SAVE_DIR/$FILENAME"

# Print a success message
echo "Screenshot saved: $SAVE_DIR/$FILENAME"



# Navigate to the directory
cd "$SAVE_DIR"

# Add the screenshot to Git
git add "$FILENAME"

# Commit with a message
git commit -m "Added new CAN Bus screenshot: $FILENAME"

# Push to GitHub (Replace 'main' with your branch name if different)
git push origin main
