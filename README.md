
**Standard Applied**: ISO/SAE 21434 – Automotive Cybersecurity

 // ISO/SAE 21434 COMPLIANCE

This project aligns with core principles of ISO/SAE 21434 by simulating secure in-vehicle communication and threat mitigation strategies across the vehicle network lifecycle. It addresses the following key aspects of the standard:

- **Threat and Risk Assessment (TARA):** The spoofing and flooding detection scripts demonstrate analysis of threat scenarios involving CAN message tampering.
- **Secure Communication (SecOC):** Implementation of HMAC-based message authentication ensures message authenticity and integrity, directly relating to the Secure Onboard Communication (SecOC) concept.
- **Monitoring and Response:** Logging, real-time anomaly detection, and data capture for forensic analysis are in line with the continuous monitoring requirements of ISO/SAE 21434.
- **Cryptographic Measures:** Use of shared secret keys and hashing mechanisms simulates industry-accepted practices for protecting in-transit data in automotive ECUs.

By building this project, I gained hands-on experience in applying the technical concepts described in ISO/SAE 21434, including message-level security, intrusion detection, and response mechanisms for connected vehicle systems.





This project demonstrates a practical approach to securing in-vehicle communication using the Controller Area Network (CAN) protocol. It focuses on detecting spoofed or tampered CAN messages, implementing secure message transmission, and analyzing vehicle network data for anomalies.

Developed as part of my Postgraduate Diploma in Cybersecurity – Automobility, this project reflects hands-on skills in CAN-bus spoofing analysis, HMAC-based message authentication, and basic intrusion detection strategies.

## Project Objectives

- Analyze and log CAN traffic using candump and Python
- Detect spoofed messages or anomalies using custom IDS logic
- Secure CAN messages with HMAC to prevent tampering
- Visualize suspicious patterns in traffic and detect flood attacks
- Build an end-to-end simulation using virtual CAN (vcan0) on Linux

## Project Structure

| File / Folder              | Description |
|---------------------------|-------------|
| can_logger.py             | Logs live CAN traffic from vcan0 into a CSV file |
| can_ids_detector.py       | Basic IDS to detect spoofed messages using ID and data behavior |
| speed_jump_ids.py         | Detects sudden, unrealistic jumps in speed from CAN messages |
| speed_ids.py              | Flags abnormal speed patterns |
| secure_can_sender.py      | Sends secure CAN messages with HMAC appended |
| secure_can_receiver.py    | Verifies HMAC of received messages and checks for tampering |
| sppof.sh                  | Spoofing simulation script to send false messages |
| test_speedometer.sh       | Sends controlled speed messages to test detection logic |
| can_log.csv               | Logged CAN data for offline analysis |
| wireshrt.pcapng           | Wireshark-captured CAN traffic file |
| images/                   | Contains PNG charts showing detection results (optional)

## Tools Used

- Python 3 (with python-can, hmac, and hashlib libraries)
- CAN-utils: candump, cansend
- vCAN interface for virtual CAN testing
- Wireshark for network traffic capture and analysis
- Linux shell scripts for automation

## Secure Communication Workflow

1. The sender script (secure_can_sender.py) generates an HMAC using a shared secret key and appends it to the CAN data field.
2. The receiver script (secure_can_receiver.py) recomputes the HMAC and compares it with the received one.
3. If the values match, the message is considered valid. If not, it is flagged as spoofed or tampered.

## Intrusion Detection Logic

- ID-based Anomaly Detection: Identifies messages with abnormal IDs or unusual data frequency
- Speed-based Checks: Detects unrealistic increases in vehicle speed over short periods
- Flooding Detection: Analyzes packet frequency to identify potential DoS or fuzzing attacks
