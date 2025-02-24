from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import socket
import struct
import os  # Import os for random data generation

# Encryption key (must be 16 bytes for AES-128)
key = b'Sixteen byte key'

# Generate random data (e.g., 8 bytes)
data = os.urandom(8)  # Generates 8 random bytes

# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC)
encrypted_data = cipher.encrypt(pad(data, AES.block_size))

# Display encrypted data for verification
print(f"Original Data: {data.hex()}")
print(f"Encrypted Data: {encrypted_data[:8].hex()}")

# CAN ID and frame setup
can_id = 0x123
can_dlc = 8  # Data length (max 8 bytes for standard CAN)

# Pack CAN frame (ID + length + first 8 bytes of encrypted data)
can_frame = struct.pack("=IB3x8s", can_id, can_dlc, encrypted_data[:8])

# Send over virtual CAN interface
sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
sock.bind(('vcan0',))
sock.send(can_frame)

print("Encrypted CAN frame sent successfully.")
