import csv
from datetime import datetime, timedelta
import random

OUT="wifi_scans.csv"
now = datetime.utcnow()
ssids = ["CorpWiFi","GuestNet","CafeFree"]
bssids = {
    "CorpWiFi": ["00:11:22:33:44:55","66:77:88:99:AA:BB"],
    "GuestNet": ["AA:BB:CC:DD:EE:01"],
    "CafeFree": ["12:34:56:78:9A:BC","12:34:56:78:9A:BD","12:34:56:78:9A:BE"]
}

rows=[]
for ssid in ssids:
    for b in bssids[ssid]:
        for i in range(random.randint(2,6)):
            t = now - timedelta(minutes=random.randint(0,19), seconds=random.randint(0,59))
            rows.append({
                "timestamp": t.isoformat(),
                "interface": "wlan0",
                "ssid": ssid,
                "bssid": b,
                "signal_dbm": random.randint(-90,-30),
                "channel": random.choice([1,6,11])
            })

rows.append({
    "timestamp": (now - timedelta(minutes=1)).isoformat(),
    "interface": "wlan0",
    "ssid": "CorpWiFi",
    "bssid": "CC:DD:EE:FF:00:11",
    "signal_dbm": -35,
    "channel": 6
})

with open(OUT,"w",newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["timestamp","interface","ssid","bssid","signal_dbm","channel"])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

print("Wrote sample scans to", OUT)
