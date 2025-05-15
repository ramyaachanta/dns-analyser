from scapy.all import sniff, DNS, DNSQR
import pandas as pd
from datetime import datetime

rows = []

def process_packet(pkt):
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        try:
            domain = pkt[DNSQR].qname.decode()
            src_ip = pkt[1].src
            ttl = 60  
            length = len(pkt)
            timestamp = datetime.now()
            label = 1 if ttl < 30 or any(domain.endswith(tld) for tld in [".xyz", ".info", ".tk", ".top", ".club"]) else 0

            # Append the packet as a new row in your dataset
            rows.append({
                "domain": domain,
                "src_ip": src_ip,
                "ttl": ttl,
                "length": length,
                "timestamp": timestamp,
                "label": label,
            })

        except Exception as e:
            print(f"Error: {e}")

print("📡 Capturing DNS packets for 2 minutes...")

# Start sniffing for 2 minutes
sniff(filter="udp port 53", prn=process_packet, timeout=120)

# Save the captured packets into a CSV
df = pd.DataFrame(rows)
df.to_csv("data/dns_live_capture.csv", index=False)

print("✅ DNS dataset saved to data/dns_live_capture.csv")

