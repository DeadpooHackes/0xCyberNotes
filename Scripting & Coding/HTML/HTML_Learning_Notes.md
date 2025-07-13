# 📘 HTML फुल गाइड – हिंदी में (HTML Full Guide in Hindi)

यह गाइड HTML के सभी टैग्स, उनके प्रयोग और उदाहरणों को कवर करती है। इसमें पूरी Cheat Sheet, Dummy Login Page और प्रैक्टिस प्रोजेक्ट्स भी शामिल हैं।

---

## 🧾 HTML टैग्स – डिस्क्रिप्शन और उदाहरण सहित (Full Cheat Sheet)

### 🔹 `<!DOCTYPE>` – HTML डॉक्युमेंट का टाइप घोषित करता है

```html
<!DOCTYPE html>
```

### 🔹 `<html>` – HTML डॉक्युमेंट की शुरुआत और अंत करता है

```html
<html lang="en">
  ...
</html>
```

### 🔹 `<head>` – मेटाडेटा, टाइटल, CSS/JS लिंक आदि को रखता है

```html
<head>
  <title>मेरा पेज</title>
</head>
```

### 🔹 `<title>` – ब्राउज़र टैब का टाइटल सेट करता है

```html
<title>Welcome</title>
```

### 🔹 `<body>` – पेज का दृश्य हिस्सा जो दिखता है

```html
<body>
  <h1>हैलो!</h1>
</body>
```

### 🔹 `<h1>` to `<h6>` – हेडिंग्स

```html
<h1>सबसे बड़ी हेडिंग</h1>
<h6>सबसे छोटी हेडिंग</h6>
```

### 🔹 `<p>` – पैराग्राफ

```html
<p>यह एक पैराग्राफ है।</p>
```

### 🔹 `<br>` – लाइन ब्रेक

```html
यह पहला लाइन<br>यह दूसरी लाइन
```

### 🔹 `<hr>` – क्षैतिज लाइन

```html
<p>पहला</p>
<hr>
<p>दूसरा</p>
```

### 🔹 `<a>` – हाइपरलिंक

```html
<a href="https://example.com">क्लिक करें</a>
```

### 🔹 `<img>` – इमेज जोड़े

```html
<img src="img.jpg" alt="Image" width="200">
```

### 🔹 `<strong>`, `<em>`, `<u>` – टेक्स्ट फॉर्मेटिंग

```html
<strong>Bold</strong>
<em>Italic</em>
<u>Underline</u>
```

### 🔹 `<ul>`, `<ol>`, `<li>` – लिस्ट

```html
<ul><li>Item</li></ul>
<ol><li>Item</li></ol>
```

### 🔹 `<table>`, `<tr>`, `<td>`, `<th>` – टेबल

```html
<table border="1">
  <tr><th>नाम</th><th>कक्षा</th></tr>
  <tr><td>राम</td><td>10</td></tr>
</table>
```

### 🔹 `<form>`, `<input>`, `<textarea>`, `<button>` – फॉर्म एलिमेंट्स

```html
<form>
  <input type="text" placeholder="नाम">
  <textarea></textarea>
  <button>सबमिट</button>
</form>
```

### 🔹 `<audio>`, `<video>` – मीडिया

```html
<audio controls><source src="audio.mp3"></audio>
<video controls><source src="video.mp4"></video>
```

### 🔹 Semantic टैग्स – लेआउट के लिए

```html
<header>Header</header>
<nav>Menu</nav>
<main>Main Content</main>
<footer>Footer</footer>
```

### 🔹 अन्य टैग्स:

* `<span>` – inline text wrapper
* `<div>` – block container
* `<label>` – form label
* `<select>`, `<option>` – dropdown

---


## 📝 प्रैक्टिस प्रोजेक्ट शीट (Practice Projects)

### 🔸 Beginner Projects:

1. Basic Resume
2. Favorite Food List
3. School Timetable Table

### 🔸 Intermediate Projects:

1. Personal Portfolio
2. Contact Form Page
3. Image Gallery Grid

### 🔸 Dummy Login Page Practice

```html
<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <title>Fake Login Page</title>
  <style>
    body {
      background: #e0e0e0;
      font-family: Arial;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .login-box {
      background: white;
      padding: 20px;
      border-radius: 8px;
      width: 300px;
      box-shadow: 0 0 10px #aaa;
    }
    input {
      width: 93%;
      padding: 10px;
      margin: 10px 0;
    }
    button {
      background: blue;
      color: white;
      padding: 10px;
      border: none;
      width: 100%;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <h2>Login</h2>
    <input type="text" placeholder="Username">
    <input type="password" placeholder="Password">
    <button>Login</button>
  </div>
</body>
</html>
```
## 🧾 HTML Cheat Sheet (टेबल फॉर्मेट में)

| टैग           | विवरण (Description)                   | उदाहरण (Code)                                     |
| ------------- | ------------------------------------- | ------------------------------------------------- |
| `<!DOCTYPE>`  | HTML डॉक्युमेंट का टाइप घोषित करता है | `<!DOCTYPE html>`                                 |
| `<html>`      | HTML डॉक्युमेंट की शुरुआत करता है     | `<html lang="en"> ... </html>`                    |
| `<head>`      | मेटाडेटा, टाइटल, CSS/JS लिंक          | `<head><title>पेज</title></head>`                 |
| `<title>`     | ब्राउज़र टैब का नाम                   | `<title>मेरा पेज</title>`                         |
| `<body>`      | पेज का दृश्य भाग                      | `<body>...</body>`                                |
| `<h1>`-`<h6>` | हेडिंग्स                              | `<h1>बड़ी हेडिंग</h1>`                            |
| `<p>`         | पैराग्राफ                             | `<p>यह एक पैराग्राफ है।</p>`                      |
| `<br>`        | लाइन ब्रेक                            | `यह पहला<br>दूसरा`                                |
| `<hr>`        | क्षैतिज रेखा                          | `<hr>`                                            |
| `<a>`         | लिंक बनाता है                         | `<a href="https://">क्लिक करें</a>`               |
| `<img>`       | इमेज जोड़ता है                        | `<img src="img.jpg" alt="image">`                 |
| `<strong>`    | बोल्ड टेक्स्ट                         | `<strong>महत्वपूर्ण</strong>`                     |
| `<em>`        | इटैलिक टेक्स्ट                        | `<em>ज़ोर</em>`                                   |
| `<u>`         | रेखांकित टेक्स्ट                      | `<u>रेखा</u>`                                     |
| `<ul>`        | unordered list                        | `<ul><li>आइटम</li></ul>`                          |
| `<ol>`        | ordered list                          | `<ol><li>आइटम</li></ol>`                          |
| `<li>`        | लिस्ट का आइटम                         | `<li>समान</li>`                                   |
| `<table>`     | टेबल बनाता है                         | `<table>...</table>`                              |
| `<tr>`        | टेबल रो                               | `<tr>...</tr>`                                    |
| `<td>`        | टेबल डेटा सेल                         | `<td>डेटा</td>`                                   |
| `<th>`        | टेबल हेडिंग                           | `<th>शीर्षक</th>`                                 |
| `<form>`      | फॉर्म शुरू करता है                    | `<form>...</form>`                                |
| `<input>`     | इनपुट फील्ड                           | `<input type="text">`                             |
| `<textarea>`  | मल्टीलाइन इनपुट                       | `<textarea></textarea>`                           |
| `<button>`    | बटन                                   | `<button>क्लिक</button>`                          |
| `<audio>`     | ऑडियो प्लेयर                          | `<audio controls><source src="file.mp3"></audio>` |
| `<video>`     | वीडियो प्लेयर                         | `<video controls><source src="file.mp4"></video>` |
| `<header>`    | पेज हेडर                              | `<header>...</header>`                            |
| `<nav>`       | नेविगेशन मेन्यू                       | `<nav>...</nav>`                                  |
| `<main>`      | मुख्य कंटेंट                          | `<main>...</main>`                                |
| `<footer>`    | पेज फुटर                              | `<footer>...</footer>`                            |
| `<span>`      | inline text wrapper                   | `<span>टेक्स्ट</span>`                            |
| `<div>`       | ब्लॉक कंटेनर                          | `<div>सेक्शन</div>`                               |
| `<label>`     | फॉर्म लेबल                            | `<label>नाम:</label>`                             |
| `<select>`    | ड्रॉपडाउन                             | `<select><option>1</option></select>`             |
| `<option>`    | विकल्प                                | `<option>विकल्प</option>`                         |

---

📌 यह एक dummy frontend login UI है। backend नहीं जोड़ा गया है।

---

## ✅ सुझाव:

* VS Code + Live Server Plugin यूज़ करें
* खुद से हर टैग के 5-5 उदाहरण बनाएं
* एक फाइल में सभी टैग्स की डेमो बनाएं

---

🎉 **रोज़ थोड़ा सीखो, रोज़ थोड़ा बनाओ – आप ज़रूर मास्टर बनोगे!**
