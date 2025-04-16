import can
import hmac
import hashlib

channel = 'vcan0'
interface = 'socketcan'
shared_key = b'secret_key'  # Must match receiver

# Data payload (max 6 bytes, leaving room for MAC)
data = bytearray([0x45, 0x67, 0x89])

# Compute HMAC (truncate to 2 bytes to fit CAN)
mac = hmac.new(shared_key, data, hashlib.sha256).digest()[:2]
payload = data + mac

try:
    bus = can.Bus(channel=channel, interface=interface)
    msg = can.Message(arbitration_id=0x456, data=payload, is_extended_id=False)
    bus.send(msg)
    print(f"  Sent secure CAN message: Data = {data.hex()} | HMAC = {mac.hex()}")
finally:
    bus.shutdown()
