---
marp: false
---


# 🔍 Nmap Commands Table in Hindi (with Examples)

| Command                        | Description (विवरण)                       | Example (उदाहरण)                        |
|-------------------------------|--------------------------------------------|------------------------------------------|
| `nmap <IP>`                   | बेसिक पोर्ट स्कैन                         | `nmap 192.168.1.1`                        |
| `nmap -p- <IP>`               | सभी 65535 पोर्ट स्कैन करें                | `nmap -p- 192.168.1.1`                    |
| `nmap -sS <IP>`               | SYN (Stealth) स्कैन                       | `nmap -sS 192.168.1.1`                    |
| `nmap -sT <IP>`               | TCP Connect स्कैन (कम सुरक्षित)          | `nmap -sT 192.168.1.1`                    |
| `nmap -sU <IP>`               | UDP पोर्ट स्कैन                          | `nmap -sU 192.168.1.1`                    |
| `nmap -sV <IP>`               | सर्विस वर्जन डिटेक्शन                     | `nmap -sV 192.168.1.1`                    |
| `nmap -O <IP>`                | OS (Operating System) डिटेक्शन            | `nmap -O 192.168.1.1`                     |
| `nmap -A <IP>`                | Advance स्कैन: OS, वर्जन, स्क्रिप्ट       | `nmap -A 192.168.1.1`                     |
| `nmap -v <IP>`                | Verbose Mode (अधिक जानकारी)              | `nmap -v 192.168.1.1`                     |
| `nmap -Pn <IP>`               | Ping स्किप करके स्कैन                    | `nmap -Pn 192.168.1.1`                    |
| `nmap -F <IP>`                | Fast Scan (100 पोर्ट्स)                  | `nmap -F 192.168.1.1`                     |
| `nmap -sC <IP>`               | Default NSE Scripts                       | `nmap -sC 192.168.1.1`                    |
| `nmap --script <script>`      | Specific Nmap Script चलाना               | `nmap --script http-enum 192.168.1.1`    |
| `nmap -iL targets.txt`        | Multiple Targets from File               | `nmap -iL targets.txt`                    |
| `nmap -oN output.txt`         | Result को Normal Text में सेव करें       | `nmap -oN result.txt 192.168.1.1`         |
| `nmap -oX output.xml`         | XML format में Output                    | `nmap -oX result.xml 192.168.1.1`         |
| `nmap --top-ports 100 <IP>`   | टॉप 100 पोर्ट स्कैन करें                 | `nmap --top-ports 100 192.168.1.1`        |
| `nmap -p 22,80,443 <IP>`      | Selected Ports स्कैन करें                | `nmap -p 22,80,443 192.168.1.1`           |
| `nmap -sN <IP>`               | NULL Scan (Advanced)                     | `nmap -sN 192.168.1.1`                    |
| `nmap -sX <IP>`               | Xmas Scan (Firewall Bypass)              | `nmap -sX 192.168.1.1`                    |

---

## 📝 Extra Tips:
- सभी कमांड्स Kali Linux या Parrot OS जैसे OS में टर्मिनल से चलाएं।  
- `sudo` का प्रयोग करें अगर permission denied error आए।  
- स्कैनिंग केवल अपनी नेटवर्क पर करें या जहाँ आपको परमिशन हो।  
