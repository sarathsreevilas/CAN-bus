# secure_can_sender.py

import can
import hmac
import hashlib
import time

channel = 'vcan0'
interface = 'socketcan'
shared_key = b'secret_key'
seq_num = 0

def get_mac(data):
    return hmac.new(shared_key, data, hashlib.sha256).digest()[:2]

print("📤 Secure CAN Sender started...")

bus = can.Bus(channel=channel, interface=interface)

while True:
    data = bytearray([0x45, 0x67, 0x89])            # 3 bytes of sample data
    sequence = seq_num.to_bytes(1, 'big')           # 1 byte seq num
    payload = data + sequence                       # 4 bytes

    mac = get_mac(payload)                          # 2-byte HMAC
    final_payload = payload + mac                   # 6 bytes total

    msg = can.Message(arbitration_id=0x456, data=final_payload, is_extended_id=False)
    bus.send(msg)

    print(f"📤 Sent: Data = {data.hex()} | Seq = {seq_num} | MAC = {mac.hex()}")

    seq_num = (seq_num + 1) % 256                   # keep it in 1 byte
    time.sleep(1)

