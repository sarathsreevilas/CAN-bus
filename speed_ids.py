import can
import time
from datetime import datetime

# CAN ID for speed messages (from ICSim it's usually 0x244)
SPEED_CAN_ID = 0x244
LAST_SPEED = None
THRESHOLD_JUMP = 50  # Maximum allowed sudden jump in speed (km/h)

def extract_speed(data):
    # ICSim encodes speed in one byte (example: data[7])
    try:
        return data[7]  # Change this index based on your setup
    except IndexError:
        return None

print("🚦 Speed Jump IDS Started - Monitoring CAN ID 0x244")

try:
    bus = can.Bus(channel='vcan0', interface='socketcan')
    while True:
        msg = bus.recv()
        if msg.arbitration_id == SPEED_CAN_ID:
            current_speed = extract_speed(msg.data)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

            if current_speed is None:
                continue

            if LAST_SPEED is not None:
                jump = abs(current_speed - LAST_SPEED)
                if jump >= THRESHOLD_JUMP:
                    print(f"[{timestamp}] ❗ ALERT: Speed jump from {LAST_SPEED} → {current_speed} km/h")
                else:
                    print(f"[{timestamp}] OK: Speed = {current_speed} km/h")

            LAST_SPEED = current_speed
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\n  Speed IDS stopped by user.")
