# secure_can_receiver.py

import can
import hmac
import hashlib
import datetime

channel = 'vcan0'
interface = 'socketcan'
shared_key = b'secret_key'

last_seq = -1  # Tracks last accepted sequence number

def get_mac(data):
    return hmac.new(shared_key, data, hashlib.sha256).digest()[:2]

print(" Secure CAN Receiver started...")

bus = can.Bus(channel=channel, interface=interface)

while True:
    msg = bus.recv()
    if msg.arbitration_id == 0x456:
        data = msg.data[:-2]
        received_mac = msg.data[-2:]
        expected_mac = get_mac(data)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        if received_mac != expected_mac:
            print(f"[{timestamp}]  INVALID MAC")
            continue

        payload_data = data[:-1]
        seq = data[-1]  # Extract 1-byte sequence number as int

        if seq <= last_seq:
            print(f"[{timestamp}]  REPLAY DETECTED: Seq = {seq}, Last Seq = {last_seq}")
            with open("replay_log.txt", "a") as f:
                f.write(f"{timestamp} - REPLAY DETECTED: Seq={seq}, Last Seq={last_seq}\n")
            continue

        last_seq = seq
        print(f"[{timestamp}]  VALID message from ID 0x{msg.arbitration_id:X} | Data = {data.hex()} | MAC OK")
