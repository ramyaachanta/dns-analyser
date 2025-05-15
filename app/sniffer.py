from scapy.all import sniff, DNS, DNSQR
import joblib
import pandas as pd
from datetime import datetime
from app.feature_extractor import extract_features
from app.database import get_engine
from sqlalchemy import create_engine

clf = joblib.load("models/model.pkl")
engine = create_engine("postgresql://postgres:Cse%4040668@localhost/dns_analyzer")

def process_packet(pkt):
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        domain = pkt[DNSQR].qname.decode()
        src_ip = pkt[1].src
        ttl = 60  
        length = len(pkt)

        features = extract_features(domain, src_ip, ttl, length)
        prediction = clf.predict(features)
        print(f"Prediction for {domain}: {prediction[0]}")

        if prediction[0] == 1:
            print(f"[!] Spoofed DNS: {domain}")
            log = pd.DataFrame([{
                "domain": domain,
                "src_ip": src_ip,
                "ttl": ttl,
                "length": length,
                "timestamp": datetime.now()
            }])
            log.to_sql("spoofed_logs", engine, if_exists="append", index=False)

sniff(filter="udp port 53", prn=process_packet, store=0)
