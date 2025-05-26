# snort_runner.py
# Part of CAN-bus IDPS project
# This script runs Snort on a given PCAP file and prints alerts

import subprocess

def run_snort(pcap_path):
    print(f"\n  Running Snort on: {pcap_path}\n")
    cmd = [
        "sudo", "snort", "-A", "console", "-q",
        "-c", "/etc/snort/snort.conf",
        "-r", pcap_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    # Example usage — replace with your actual pcap file
    run_snort("spoof_packet.pcap")
