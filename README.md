# CAN-Bus Spoofing Attack

## Tools Needed
- **ICSim**: Simulates a car dashboard with CAN messages.
- **Wireshark**: Captures and analyzes CAN Bus traffic.
- **CAN-utils**: Allows sending, modifying, and spoofing CAN messages.

## Step-by-step Guide
1. Install ICSim on Kali Linux or Ubuntu.
2. Run ICSim to generate simulated CAN Bus traffic.
3. Use Wireshark to capture and analyze the CAN messages.
4. Use CAN-utils to inject false messages (e.g., changing the vehicle speed).

## Example Attack:
- Send a spoofed CAN message to trick the dashboard into showing false speed (e.g., 200 km/h instead of 60 km/h).
- Try CAN fuzzing – sending random data to see how the vehicle reacts.

## Tools Installation:
```bash
sudo apt install build-essential libtool libboost-all-dev libsdl2-dev
git clone https://github.com/ICSim/ICSim.git
cd ICSim
make

