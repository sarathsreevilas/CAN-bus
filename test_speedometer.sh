#!/bin/bash

# 1. Load virtual CAN module
sudo modprobe vcan  

# 2. Create a virtual CAN interface (vcan0)
sudo ip link add dev vcan0 type vcan  
sudo ip link set up vcan0  

# 3. Start capturing CAN packets in the background
echo "Capturing CAN messages..."
candump vcan0 &

# Allow some time for candump to start
sleep 1

# 4. Inject CAN messages (simulating a speedometer)
echo "Sending CAN messages..."
cangen vcan0 -I 123 -L 8 -D 1122334455667788 -v -g 100

# Wait for a few seconds (or you can add more logic here to stop after a certain condition)
sleep 10

# 5. Stop capturing (optional, if you want to stop candump after a few seconds)
pkill candump

