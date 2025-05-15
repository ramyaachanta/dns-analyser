import pandas as pd

def extract_features(domain, src_ip, ttl, length):
    domain_len = len(domain)
    try:
        src_ip_octet = int(src_ip.split(".")[0]) if "." in src_ip else 0  # fallback for IPv6
    except:
        src_ip_octet = 0
    return pd.DataFrame([{
        "ttl": ttl,
        "length": length,
        "domain_len": domain_len,
        "src_ip_octet": src_ip_octet
    }])
