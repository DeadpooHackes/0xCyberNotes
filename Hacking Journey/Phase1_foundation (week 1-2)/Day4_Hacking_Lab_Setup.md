---
marp: true
---

# 🔧 DVWA Lab Setup Guide – Hacking Practice

DVWA (Damn Vulnerable Web Application) is a deliberately vulnerable PHP/MySQL web app for learning and practicing web vulnerabilities such as XSS, SQLi, CSRF, etc.

---

## 💻 1. Requirements

* OS: Kali Linux, Ubuntu, or any Debian-based distro
* Apache2 (Web Server)
* MySQL/MariaDB (Database Server)
* PHP
* Git (for cloning DVWA repo)

---

## 🧰 2. Install Dependencies

```bash
sudo apt update && sudo apt install apache2 mariadb-server php php-mysqli git -y
```

Enable and start Apache & MySQL:

```bash
sudo systemctl enable apache2
sudo systemctl start apache2
sudo systemctl enable mariadb
sudo systemctl start mariadb
```

---

## 🐬 3. Setup MySQL

Login to MySQL:

```bash
sudo mysql
```

Then run:

```sql
CREATE DATABASE dvwa;
CREATE USER 'dvwauser'@'localhost' IDENTIFIED BY 'dvwapass';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwauser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

---

## 📦 4. Clone and Move DVWA Files

```bash
git clone https://github.com/digininja/DVWA.git
sudo mv DVWA /var/www/html/dvwa
```

Set permissions:

```bash
sudo chown -R www-data:www-data /var/www/html/dvwa
```

---

## 🛠️ 5. Configure DVWA

Edit the config file:

```bash
sudo cp /var/www/html/dvwa/config/config.inc.php.dist /var/www/html/dvwa/config/config.inc.php
sudo nano /var/www/html/dvwa/config/config.inc.php
```

Update MySQL settings:

```php
$_DVWA[ 'db_user' ] = 'dvwauser';
$_DVWA[ 'db_password' ] = 'dvwapass';
```

---

## ✅ 6. Enable PHP and Apache Modules

```bash
sudo phpenmod mysqli
sudo systemctl restart apache2
```

---

## 🌐 7. Access DVWA in Browser

Open:

```
http://127.0.0.1/dvwa
```

Click **Create / Reset Database** to initialize.

---

## 🔒 8. Set DVWA Security Level

DVWA Security Level:
Go to `DVWA > Security` in the menu
Set to:

* **Low** – For practicing basic vulnerabilities
* **Medium/High** – For realistic challenges

---

## 💡 Tips

* Always reset the database if configs break.
* Use Burp Suite with DVWA for intercepting HTTP requests.
* Practice:

  * XSS (Reflected/Stored)
  * SQL Injection
  * File Upload
  * CSRF
  * Command Injection

---

✅ DVWA is now ready for hacking practice!

Made by **Lucy – Your Hacking Trainer** 🐍
