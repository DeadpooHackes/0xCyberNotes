import csv
from collections import defaultdict
from datetime import datetime, timedelta
import statistics

CSV_PATH = "wifi_scans.csv"

def load_scans(path):
    scans = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row['timestamp'] = datetime.fromisoformat(row['timestamp'])
            except Exception:
                continue
            row['signal_dbm'] = int(row.get('signal_dbm') or 0)
            scans.append(row)
    return scans

def analyze(scans, window_minutes=10):
    ssid_map = defaultdict(lambda: defaultdict(list))
    for r in scans:
        ssid = r['ssid'] or "<hidden>"
        bssid = r['bssid']
        ssid_map[ssid][bssid].append(r)

    alerts = []
    now = datetime.utcnow()
    cutoff = now - timedelta(minutes=window_minutes)
    for ssid, bmap in ssid_map.items():
        recent_bssids = []
        for bssid, records in bmap.items():
            if any(rec['timestamp'] >= cutoff for rec in records):
                svals = [rec['signal_dbm'] for rec in records if rec['timestamp'] >= cutoff]
                avg_sig = statistics.mean(svals) if svals else None
                recent_bssids.append((bssid, avg_sig, len(svals)))
        if len(recent_bssids) >= 2:
            alerts.append({
                "ssid": ssid,
                "count_bssids": len(recent_bssids),
                "details": recent_bssids
            })
    return alerts

if __name__ == "__main__":
    scans = load_scans(CSV_PATH)
    alerts = analyze(scans, window_minutes=15)
    if not alerts:
        print("No anomalies detected in given CSV.")
    else:
        print("Potential rogue/anomaly alerts:")
        for a in alerts:
            print(f"SSID: {a['ssid']}, BSSIDs: {a['count_bssids']}")
            for b in a['details']:
                print(f"  BSSID: {b[0]}, avg_signal: {b[1]}, samples: {b[2]}")
