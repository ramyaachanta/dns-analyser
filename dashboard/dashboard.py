import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import time

# DB connection
engine = create_engine("postgresql://postgres:Cse%4040668@localhost/dns_analyzer")

# Auto-refresh every 5 seconds
REFRESH_INTERVAL = 5  # seconds

# Title
st.set_page_config(page_title="DNS Spoof Detection", layout="wide")
st.title("🛡️ DNS Spoof Detection Dashboard")

# Auto-refresh checkbox
refresh = st.checkbox(f"Auto-refresh every {REFRESH_INTERVAL} seconds", value=True)

# Show data
df = pd.read_sql("SELECT * FROM spoofed_logs ORDER BY timestamp DESC", engine)

st.subheader("Recent Spoofed DNS Logs")
st.dataframe(df)

csv = df.to_csv(index=False)
st.download_button("📥 Download Logs", csv, "spoofed_logs.csv", "text/csv")

# TTL Distribution Chart
st.subheader("📊 TTL Distribution")
st.bar_chart(df["ttl"].value_counts().sort_index())

# Auto-refresh logic
if refresh:
    time.sleep(REFRESH_INTERVAL)
    st.rerun()