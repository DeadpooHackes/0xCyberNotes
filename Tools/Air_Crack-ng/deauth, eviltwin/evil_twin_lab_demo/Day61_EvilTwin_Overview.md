
# Day 61 — Evil Twin (Rogue AP): सिद्धांत, MITM और फ़िशिंग — उदाहरण और कोड (सुरक्षा-केन्द्रित, non-actionable)

**ध्यान:** यह फ़ाइल अब उदाहरण और कोड शामिल करती है परन्तु किसी भी तरह के *हमला करने योग्य* निर्देश, स्क्रिप्ट या कॉन्फ़िगरेशन **नहीं** देती। सभी कोड रक्षात्मक (detect/educate/forensic) या शिक्षण‑उद्देश्य के लिए हैं। प्रयोग केवल कानूनी, नियंत्रित लैब‑नेटवर्क या वर्चुअल वातावरण में करें।

---

## A) अवधारणात्मक (pseudo‑code) फ्लो — केवल समझ के लिए
यह pseudo‑code केवल यह दिखाने के लिए है कि एक Evil‑Twin जैसा हमला *ख्याली तौर पर* किस तरह ट्रैफ़िक को प्रभावित कर सकता है — यह किसी भी वास्तविक कमांड या टूल का उपयोग नहीं बताता।

```text
# PSEUDO-FLOW (conceptual, non-executable)
Attacker:
  - Observe target SSID name and characteristics (do not interact with real users)
  - Create a wireless AP that *appears* similar (same SSID visible)
  - Wait for a victim device to prefer/associate with the rogue AP
  - If victim associates, attacker may be positioned to observe/forward traffic
  - Optionally show a captive-portal like page to the victim (for educational/demo only)
  - Record network-level metadata for analysis (timestamps, MACs, signal strength)
```

ऊपर का flow केवल शैक्षिक है — इसमें कोई executable कमांड नहीं है।  

---

## B) रक्षा/डिटेक्शन उदाहरण — Wi‑Fi scan लॉग का एनालिसिस (Python)
यह कोड **एक CSV** (या जैसा भी आपका स्कैन टूल एक्सपोर्ट करे) को पढ़कर यह पहचानता है कि किसी एक ही SSID के लिए कई अलग‑अलग BSSID दिख रहे हैं और signal_strength/last_seen के आधार पर असामान्य व्यवहार (potential rogue) flag करता है। यह रक्षात्मक और फ़ॉरेंसिक‑सहायता के लिए है।

**फ़ाइल का फॉर्मैट (example CSV columns):**
- timestamp (ISO format)
- interface
- ssid
- bssid
- signal_dbm (integer)
- channel

```python
# save as wifi_roguedetect.py
import csv
from collections import defaultdict
from datetime import datetime, timedelta
import statistics

CSV_PATH = "wifi_scans.csv"  # आपके स्कैन टूल से एक्सपोर्ट फाइल

def load_scans(path):
    scans = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # basic sanitation and types
            try:
                row['timestamp'] = datetime.fromisoformat(row['timestamp'])
            except Exception:
                continue
            row['signal_dbm'] = int(row.get('signal_dbm') or 0)
            scans.append(row)
    return scans

def analyze(scans, window_minutes=10):
    # group by SSID -> BSSID observations
    ssid_map = defaultdict(lambda: defaultdict(list))
    for r in scans:
        ssid = r['ssid'] or "<hidden>"
        bssid = r['bssid']
        ssid_map[ssid][bssid].append(r)

    alerts = []
    now = datetime.utcnow()
    cutoff = now - timedelta(minutes=window_minutes)
    for ssid, bmap in ssid_map.items():
        # if same SSID has more than 2 distinct BSSIDs in short window -> suspicious
        recent_bssids = []
        for bssid, records in bmap.items():
            if any(rec['timestamp'] >= cutoff for rec in records):
                # aggregate signal strengths
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
        print("कोई असामान्य गतिविधि नहीं मिली (given CSV).")
    else:
        print("संभावित Rogue/อ노मली Alerts:")
        for a in alerts:
            print(f"SSID: {a['ssid']}, BSSIDs: {a['count_bssids']}")
            for b in a['details']:
                print(f"  BSSID: {b[0]}, avg_signal: {b[1]}, samples: {b[2]}")
```

**कैसे उपयोग करें (सुरक्षा‑नोट):**
- यह स्क्रिप्ट किसी भी Wi‑Fi स्कैन टूल की output CSV पर चल सकती है — उदाहरण के लिए `nmcli -f SSID,BSSID,SIGNAL dev wifi` के परिणामों का structured export (आपके लैब‑टूल के हिसाब से बनाना होगा)।
- यह हमला करने के लिए नहीं है — यह anomalous behaviour की पहचान में मदद करेगा और नेटवर्क एडमिन को अलर्ट देगा।

---

## C) फ़ॉरेंसिक‑लेवल रिकॉर्डिंग (लॉगिंग) — सरल JSON लॉगर (Python)
नेटवर्क‑इवेंट की संरचित लॉगिंग महत्वपूर्ण है। नीचे एक छोटा Logger दिखाया गया है जो CSV/JSON के रूप में AP‑observations को स्टोर करेगा — यह नेटवर्क‑फोरेंसिक के लिए उपयोगी है।

```python
# ap_logger.py
import json
from datetime import datetime

LOGFILE = "ap_observations.jsonl"

def log_observation(ssid, bssid, channel, signal_dbm, iface):
    rec = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ssid": ssid,
        "bssid": bssid,
        "channel": channel,
        "signal_dbm": signal_dbm,
        "interface": iface
    }
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

# Example usage:
if __name__ == "__main__":
    # इन उदाहरणों को अपने वास्तविक टूल से replace करें — यहाँ केवल संरचना दिखाई गई है
    log_observation("CorpWiFi", "00:11:22:33:44:55", 6, -42, "wlan0")
    log_observation("CorpWiFi", "66:77:88:99:AA:BB", 6, -80, "wlan0")
    print("logged sample observations")
```

---

## D) शैक्षिक 'Mock captive portal' — harmless HTML (ब्लॉग‑स्टाइल)
यह एक **शिक्षण‑उद्देश्य** का HTML पेज है जो उपयोगकर्ता को बताता है कि यह एक डेमो है और क्रेडेंशियल नहीं मांगा जाता। सुरक्षा‑टेस्ट के दौरान वास्तविक क्रेडेंशियल कलेक्ट न करें — यह अवैध और अनैतिक है।

```html
<!-- save as mock_captive_demo.html -->
<!doctype html>
<html lang="hi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>शिक्षण‑डेमो — Captive Portal (Non‑collecting)</title>
  <style>
    body { font-family: Arial, Helvetica, sans-serif; background:#f4f6fb; color:#111; padding:24px; }
    .card { background:white; padding:18px; border-radius:8px; max-width:720px; margin:auto; box-shadow:0 6px 20px rgba(0,0,0,0.08); }
    .alert { color:#8a1; font-weight:700; }
    input[disabled] { opacity:0.6; }
  </style>
</head>
<body>
  <div class="card">
    <h2>शिक्षण‑डेमो: Captive Portal (Non‑Collecting)</h2>
    <p class="alert">यह केवल एक शिक्षण पृष्ठ है — कृपया अपना कोई भी वास्तविक पासवर्ड यहाँ न डालें।</p>
    <p>उद्देश्य: यह दिखाना कि कैप्टिव‑पोर्टल उपयोगकर्ता को कैसे redirect कर सकता है। इस पेज पर कोई भी इनपुट सर्वर पर स्टोर नहीं होता।</p>

    <form onsubmit="alert('यह केवल डेमो है — कोई डेटा स्टोर नहीं किया गया'); return false;">
      <label>ईमेल / उपयोगकर्ता नाम (डेमो):</label><br>
      <input type="text" value="demo@example.com" disabled><br><br>
      <label>किसी भी कार्य के लिए नीचे 'Continue' दबाएँ (डेमो):</label><br>
      <button type="submit">Continue (Demo)</button>
    </form>

    <hr>
    <h4>शिक्षण‑नोट्स</h4>
    <ul>
      <li>यदि आप captive portals का अध्ययन कर रहे हैं, तो केवल नियंत्रित लैब में अभ्यास करें।</li>
      <li>ब्राउज़र certificate warnings को कभी bypass न करें — वे असुरक्षा का स्पष्ट संकेत हैं।</li>
    </ul>
  </div>
</body>
</html>
```

---

## E) लैब‑सेटअप‑सुझाव (सुरक्षित)
- अपने लैब के लिए अलग VLAN/इंटरनेट‑सॉल्टिव (No Internet) रूट बनायें।  
- उपयोग करें: Virtual machines, isolated Wi‑Fi AP (या वर्चुअल AP) और केवल स्वयं के उपकरण‑SSID पर टेस्ट करें।  
- हमेशा लिखित अनुमति लें यदि किसी अन्य व्यक्ति या संस्था का सिस्टम शामिल हो।  

---

## F) क्या मैं यह Markdown फ़ाइल अपडेट कर दूँ?
मैं इन उदाहरणों को आपकी Markdown फ़ाइल में जोड़ सकता/सकती हूँ और फ़ाइल को अपडेट कर के डाउनलोड लिंक दे दूँगा/दूंगी। क्या मैं यही करूँ? (हाँ → मैं अपडेट कर दूँगा/दूंगी और फ़ाइल का डाउनलोड लिंक दे दूँगा/दूंगी)  
