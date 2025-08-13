
# 🐧 Linux फ़ाइल सिस्टम (Linux File System) – हिन्दी में पूर्ण विवरण

Linux फ़ाइल सिस्टम एक संरचना है जो यह निर्धारित करती है कि फ़ाइलें और डाइरेक्टरीज़ डिस्क पर कैसे संग्रहित और व्यवस्थित होती हैं।

---

## 🔰 रूट डायरेक्टरी – `/`
Linux में फ़ाइल सिस्टम `/` से शुरू होता है, जिसे रूट डायरेक्टरी कहते हैं। बाकी सारी फ़ोल्डरें और फ़ाइलें इसी के अंदर होती हैं।

---

## 📁 मुख्य डायरेक्टरीज़ और उनका उपयोग

| डायरेक्टरी | उपयोग |
|------------|--------|
| `/bin` | बेसिक कमांड्स जैसे `ls`, `cp`, `rm` |
| `/boot` | बूट लोडर फाइल्स, `vmlinuz`, `grub` |
| `/dev` | सभी डिवाइस फाइलें, जैसे `/dev/sda`, `/dev/null` |
| `/etc` | सिस्टम की सभी configuration फाइलें |
| `/home` | सभी users की personal डायरेक्टरी |
| `/lib`, `/lib64` | जरूरी सिस्टम libraries |
| `/media`, `/mnt` | USB, CD-ROM जैसे external devices के लिए |
| `/opt` | Third-party software installation के लिए |
| `/proc` | वर्चुअल फाइल सिस्टम, प्रोसेस और kernel जानकारी |
| `/root` | Root user की होम डायरेक्टरी |
| `/run` | Runtime सिस्टम डेटा |
| `/sbin` | System level commands जैसे `reboot`, `shutdown` |
| `/srv` | Server data (जैसे web server) |
| `/sys` | Kernel और hardware info |
| `/tmp` | Temporary files |
| `/usr` | User applications और प्रोग्राम्स |
| `/var` | Log files, spool, cache, आदि |

---

## 📂 डायरेक्टरी ट्री उदाहरण:

```
/
├── bin/
├── boot/
├── dev/
├── etc/
├── home/
│   ├── rootpapa/
│   └── guest/
├── lib/
├── media/
├── mnt/
├── opt/
├── proc/
├── root/
├── run/
├── sbin/
├── srv/
├── sys/
├── tmp/
├── usr/
│   ├── bin/
│   ├── lib/
│   └── local/
├── var/
```

---

## 🧠 "Everything is a File" (हर चीज़ एक फ़ाइल है)

Linux में hardware, process, device — सब फ़ाइल की तरह दिखता है:

| नाम | क्या है |
|------|---------|
| `/dev/sda` | हार्ड डिस्क |
| `/dev/null` | ब्लैक होल (डाटा फेंकने के लिए) |
| `/proc/cpuinfo` | CPU जानकारी |
| `/etc/passwd` | यूज़र अकाउंट्स |

---

## 🧾 अतिरिक्त डायरेक्टरी

| डायरेक्टरी | उपयोग |
|------------|--------|
| `/lost+found` | Crash के बाद बची हुई फ़ाइलें |
| `/snap` | Snap पैकेज के लिए (Ubuntu में) |
| `/swapfile` | RAM की कमी होने पर इस्तेमाल होती है |

---

## 📌 Extra Concepts (अतिरिक्त जानकारी)

### 🔸 फ़ाइल सिस्टम टाइप्स
- `ext4` – सबसे कॉमन और fast फाइल सिस्टम
- `ext3`, `ext2` – पुराने versions
- `Btrfs`, `XFS`, `ZFS` – Advanced विकल्प

### 🔸 Partitions Structure
- अलग-अलग partition करना अच्छा होता है:
  - `/` – रूट सिस्टम
  - `/home` – यूज़र डेटा
  - `/var` – logs और dynamic डेटा
  - `swap` – RAM backup

### 🔸 Mounting Commands
- `mount`, `umount` – फाइल सिस्टम माउंट/अनमाउंट करने के लिए
- `df -h` – डिस्क यूसेज देखना
- `lsblk` – block devices देखना

### 🔸 Permissions & Ownership
- `chmod`, `chown`, `umask` – फ़ाइल permission को मैनेज करने के लिए

### 🔸 Journaling File System
- Journaling से डेटा लॉस कम होता है; ext4 और btrfs में होता है।

---

## ✅ सारांश तालिका:

| डायरेक्टरी | कार्य |
|------------|------|
| `/` | रूट, सभी चीज़ों की जड़ |
| `/home` | यूज़र फोल्डर |
| `/etc` | सेटिंग्स और config |
| `/bin` | आवश्यक कमांड्स |
| `/dev` | डिवाइस फ़ाइलें |
| `/proc` | सिस्टम प्रोसेस जानकारी |
| `/var` | लॉग्स और चेंजिंग डेटा |
| `/tmp` | टेम्पररी फ़ाइल्स |
| `/usr` | सॉफ्टवेयर |
| `/boot` | बूट सिस्टम |

