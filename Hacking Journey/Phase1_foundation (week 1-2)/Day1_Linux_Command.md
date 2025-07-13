---
marp: true
---

# 📘 Day 1: Linux Commands Basics

---

## 🔰 Linux क्या है?

Linux एक **ओपन-सोर्स ऑपरेटिंग सिस्टम** है जो मुख्य रूप से **हैकिंग, सर्वर, और नेटवर्क सिक्योरिटी** के लिए प्रयोग होता है।

---

## 🧠 Basic Linux Commands

| Command           | उपयोग                                                 |
|-------------------|--------------------------------------------------------|
| `pwd`             | Print Working Directory – आपका करंट फोल्डर दिखाता है      |
| `ls`              | फोल्डर के अंदर मौजूद फाइल्स और फोल्डर दिखाता है         |
| `cd <folder>`     | किसी फोल्डर में जाने के लिए                           |
| `cd ..`           | एक लेवल पीछे जाने के लिए                             |
| `mkdir <name>`    | नया फोल्डर बनाने के लिए                              |
| `touch <file>`    | खाली फाइल बनाने के लिए                               |
| `rm <file>`       | फाइल डिलीट करने के लिए                               |
| `rm -r <folder>`  | फोल्डर और अंदर की फाइलें डिलीट करने के लिए           |
| `cp <source> <dest>` | फाइल कॉपी करने के लिए                          |
| `mv <old> <new>`  | फाइल को मूव या नाम बदलने के लिए                      |
| `clear`           | टर्मिनल क्लियर करने के लिए                            |
| `history`         | अभी तक चले हुए commands की लिस्ट दिखाता है            |

---

## 🔐 Permissions Check

| Command         | उपयोग                                        |
|-----------------|-----------------------------------------------|
| `ls -l`         | फाइल्स की permission और details              |
| `chmod +x file` | फाइल को executable बनाता है                  |

---

## 📦 Package Management (Kali/Debian based)

| Command                    | उपयोग                                   |
|----------------------------|------------------------------------------|
| `sudo apt update`         | पैकेज लिस्ट अपडेट करता है              |
| `sudo apt install <name>` | नया पैकेज इंस्टॉल करता है              |
| `sudo apt remove <name>`  | पैकेज को हटाता है                      |

---

## 🧪 Practice

```bash
bash
mkdir hacking_lab
cd hacking_lab
touch notes.txt
echo "Hello Hacker" > notes.txt
cat notes.txt
