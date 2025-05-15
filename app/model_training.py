import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def extract_ip_octet(ip):
    try:
        return int(ip.split(".")[0]) if "." in ip else 0  # fallback for IPv6
    except:
        return 0


# df = pd.read_csv("data/dns_live_capture.csv")
df = pd.read_csv("data/dns_dataset.csv")


df["domain_len"] = df["domain"].apply(len)
df["src_ip_octet"] = df["src_ip"].apply(extract_ip_octet)

X = df[["ttl", "length", "domain_len", "src_ip_octet"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

joblib.dump(clf, "models/model.pkl")
