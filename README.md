
# 🛡️ DNS Spoof Detection System

A real-time DNS packet analyzer and spoof detector built using Scapy, Python, and Machine Learning. It features live capture, model training, and a Streamlit dashboard to visualize and investigate DNS threats.

---

## 📂 Project Structure

```
DNS-ANALYSER/
│
├── app/
│   ├── collector.py           # Packet collector / live capture processor
│   ├── database.py            # PostgreSQL DB setup
│   ├── feature_extractor.py   # Feature generation for ML model
│   ├── model_training.py      # Script to train model on CSV
│   ├── models.py              # Model wrapper if needed
│   └── sniffer.py             # Live sniffing with prediction
│
├── dashboard/
│   └── dashboard.py           # Streamlit dashboard to show results
│
├── data/
│   ├── dns_dataset.csv        # Training dataset (labeled)
│   └── dns_live_capture.csv   # Output from live capture
│
├── models/
│   └── model.pkl              # Trained ML model
│
├── init_db.py                 # Optional script to initialize schema
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/dns-analyser.git
cd dns-analyser
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ Database Configuration

Ensure PostgreSQL is installed and running. Create a database:

```sql
CREATE DATABASE dns_analyzer;
```

Update the DB connection string inside `database.py` and `sniffer.py`:

```python
engine = create_engine("postgresql://postgres:YOUR_PASSWORD@localhost/dns_analyzer")
```

Schema for logging spoofed entries (auto-created):

```sql
spoofed_logs (
    domain TEXT,
    src_ip TEXT,
    ttl INTEGER,
    length INTEGER,
    timestamp TIMESTAMP
)
```

---

## 🚀 Run the DNS Sniffer (Live Monitoring)

> ⚠️ Requires root privileges to sniff packets

```bash
sudo python app/sniffer.py
```

What it does:
- Captures packets on UDP port 53
- Extracts domain, IP, TTL, length
- Applies ML model prediction
- Logs spoofed packets to DB and optionally CSV

---

## 🧠 Train Your ML Model

### 1. Prepare the training dataset

Edit `data/dns_dataset.csv` with entries like:

```csv
domain,src_ip,ttl,length,label
bad-domain.xyz,192.168.0.5,20,84,1
google.com,192.168.0.1,60,95,0
```

### 2. Train the model

```bash
python app/model_training.py
```

This:
- Loads the CSV
- Extracts features
- Trains a classifier (e.g., RandomForest)
- Saves the model as `models/model.pkl`

---

## 📊 Streamlit Dashboard

To visualize spoofed DNS logs:

```bash
streamlit run dashboard/dashboard.py
```

It connects to the PostgreSQL DB and displays:
- Spoofed entries
- Filters for domain/TLD/time
- Packet statistics

---

## 📋 Feature Set (Used by Model)

The `feature_extractor.py` extracts features such as:
- Domain length
- TTL value
- Packet length
- Suspicious TLD indicator (`.xyz`, `.info`, `.tk`, etc.)
- Digit count in domain
- Entropy (optional)

---

## 📝 Logging Format

Spoofed entries logged in DB and CSV contain:

| Field     | Description                  |
|-----------|------------------------------|
| domain    | Queried domain               |
| src_ip    | Source IP address            |
| ttl       | Time to live (static/simulated) |
| length    | Packet byte length           |
| timestamp | Time of detection            |

---

## 👤 Author

**Ramya Sri Achanta**  
_Masters in Computer Science | Network Security & Machine Learning Enthusiast_

---

## 📄 License

MIT License – Free to use and modify.

---

## ✅ Tips

- Test using `dig bad-domain.xyz` or simulate packets in Python
- Modify feature extractor to improve detection (e.g., entropy, substring patterns)
- Run sniffer in parallel with dashboard for a live monitoring experience
