import can
import hmac
import hashlib
from datetime import datetime

channel = 'vcan0'
interface = 'socketcan'
shared_key = b'secret_key'  # Must match sender

print("🔐 Secure CAN Receiver started...")

bus = can.Bus(channel=channel, interface=interface)

try:
    while True:
        msg = bus.recv()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        payload = msg.data

        if len(payload) < 3:
            print(f"[{timestamp}] ⚠️ Skipping short message: {payload.hex()}")
            continue

        data = payload[:-2]  # all but last 2 bytes
        received_mac = payload[-2:]  # last 2 bytes

        # Recalculate HMAC
        expected_mac = hmac.new(shared_key, data, hashlib.sha256).digest()[:2]

        if expected_mac == received_mac:
            print(f"[{timestamp}] ✅ VALID message from ID {hex(msg.arbitration_id)} | Data = {data.hex()} | MAC OK")
        else:
            print(f"[{timestamp}] ❌ TAMPERED or SPOOFED message from ID {hex(msg.arbitration_id)} | Data = {data.hex()} | Expected MAC = {expected_mac.hex()} | Received = {received_mac.hex()}")

except KeyboardInterrupt:
    print("\n🛑 Receiver stopped.")
