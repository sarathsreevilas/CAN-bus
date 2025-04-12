import can
import csv
from datetime import datetime

# Set up CAN interface (e.g., vcan0 for virtual or can0 for real device)
interface = 'socketcan'
channel = 'vcan0'  # change to 'can0' if using real hardware

log_file = 'can_log.csv'

# Open the CSV file to log messages
with open(log_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'CAN ID', 'Data'])

    print("📡 Listening to CAN traffic on", channel)
    try:
        bus = can.interface.Bus(channel=channel, bustype=interface)
        while True:
            msg = bus.recv()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            can_id = hex(msg.arbitration_id)
            data = ' '.join(f'{byte:02X}' for byte in msg.data)
            print(f"[{timestamp}] ID: {can_id} | Data: {data}")
            writer.writerow([timestamp, can_id, data])
    except KeyboardInterrupt:
        print("\n🛑 Logging stopped by user.")
