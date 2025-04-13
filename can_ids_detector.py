import can
from datetime import datetime

# List of known CAN IDs used by ICSim
KNOWN_IDS = {0x244, 0x245, 0x105, 0x112}  # Add more as you discover them

interface = 'socketcan'
channel = 'vcan0'

print(" IDS Started - Monitoring CAN traffic on", channel)

try:
    bus = can.Bus(channel=channel, interface=interface)
    while True:
        msg = bus.recv()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        can_id = msg.arbitration_id
        data = ' '.join(f'{byte:02X}' for byte in msg.data)

        if can_id not in KNOWN_IDS:
            print(f"[{timestamp}] ❗ ALERT: Suspicious CAN ID Detected: {hex(can_id)} | Data: {data}")
        else:
            print(f"[{timestamp}] OK: ID {hex(can_id)} | Data: {data}")

except KeyboardInterrupt:
    print("\n  IDS stopped by user.")
