# secure_can_sender.py

import can
import hmac
import hashlib
import time
import struct

channel = 'vcan0'
interface = 'socketcan'
shared_key = b'secret_key'

def get_mac(data):
    return hmac.new(shared_key, data, hashlib.sha256).digest()[:2]  # 2-byte HMAC

print(" Secure CAN Sender with Timestamp started...")

bus = can.Bus(channel=channel, interface=interface)

while True:
    data = bytearray([0x45, 0x67])  # 2-byte payload
    timestamp = int(time.time())   # current UNIX timestamp (4 bytes)
    ts_bytes = timestamp.to_bytes(4, 'big')  # 4 bytes

    payload = data + ts_bytes                   # 6 bytes
    mac = get_mac(payload)                      # 2 bytes
    final_payload = payload + mac               # 8 bytes total

    msg = can.Message(arbitration_id=0x456, data=final_payload, is_extended_id=False)
    bus.send(msg)

    print(f" Sent: Data = {data.hex()} | Timestamp = {timestamp} | MAC = {mac.hex()}")

    time.sleep(1)
