import can
import time
from datetime import datetime
from collections import defaultdict

# Flooding threshold — change based on your system speed
FLOOD_THRESHOLD = 10  # messages per second
TIME_WINDOW = 1  # in seconds

# CAN channel
channel = 'vcan0'
interface = 'socketcan'

# Track message counts
msg_counts = defaultdict(list)

print("🚨 Flooding Detection IDS started on", channel)

try:
    bus = can.Bus(channel=channel, interface=interface)

    while True:
        msg = bus.recv()
        timestamp = time.time()
        can_id = msg.arbitration_id

        # Record timestamp of this CAN ID
        msg_counts[can_id].append(timestamp)

        # Remove old timestamps outside the time window
        msg_counts[can_id] = [t for t in msg_counts[can_id] if t >= timestamp - TIME_WINDOW]

        # Count how many messages came from this ID in the last second
        count = len(msg_counts[can_id])
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        if count > FLOOD_THRESHOLD:
            print(f"[{dt}] ❗ ALERT: Flooding detected from CAN ID {hex(can_id)} – {count} msgs/sec")
        else:
            print(f"[{dt}] OK: {hex(can_id)} - {count} msg(s)/sec")

except KeyboardInterrupt:
    print("\n🛑 Flooding IDS stopped by user.")
