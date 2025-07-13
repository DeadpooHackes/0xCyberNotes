# 🎨 CSS की सम्पूर्ण गाइड (हिंदी में) – वेब डेवेलपर्स और एथिकल हैकर्स के लिए

---

## 📘 अध्याय 1: CSS क्या है?

**CSS** (Cascading Style Sheets) एक डिज़ाइन भाषा है जो HTML वेबपेज को सुंदर बनाने के लिए उपयोग होती है।

👉 इससे आप कंट्रोल कर सकते हैं:

- टेक्स्ट का रंग, आकार और फ़ॉन्ट
- पृष्ठभूमि रंग और चित्र
- बॉर्डर, मार्जिन, पेडिंग
- लेआउट और रेस्पॉन्सिव डिज़ाइन

---

## 🧩 अध्याय 2: CSS कैसे काम करता है?

### 🔹 3 तरीके CSS लगाने के:

| तरीका | उदाहरण |
|-------|---------|
| Inline | `<h1 style="color: red;">Hello</h1>` |
| Internal | `<style>h1 { color: red; }</style>` |
| External | `<link rel="stylesheet" href="style.css">` |

✅ **External CSS** सबसे अच्छा तरीका है।

---

## 🧠 अध्याय 3: CSS Syntax

```css
selector {
  property: value;
}
```

उदाहरण:
```css
h1 {
  color: blue;
  font-size: 24px;
}
```

---

## 🎯 अध्याय 4: CSS Selectors

| Selector | उदाहरण | काम |
|----------|--------|-----|
| * | `* {}` | सभी एलिमेंट्स को चुनता है |
| टैग | `p {}` | सभी `<p>` टैग |
| क्लास | `.box {}` | class="box" वाले |
| ID | `#main {}` | id="main" वाले |
| ग्रुप | `h1, p {}` | दोनों को चुनें |

---

## 🎨 अध्याय 5: सामान्य CSS Properties

| Property | काम |
|----------|-----|
| `color` | टेक्स्ट का रंग |
| `background-color` | बैकग्राउंड का रंग |
| `font-size` | टेक्स्ट का आकार |
| `text-align` | टेक्स्ट को Center/Left |
| `border` | बॉर्डर देना |
| `margin` | बाहर की जगह |
| `padding` | अंदर की जगह |
| `width`, `height` | आकार देना |

---

## 🧱 अध्याय 6: Box Model

HTML एलिमेंट 4 स्तरों से घिरा होता है:

```
| Margin |
| Border |
| Padding |
| Content |
```

---

## 📦 अध्याय 7: Layout Systems

### 🔹 Flexbox:
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### 🔸 Grid:
```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
```

---

## 📱 अध्याय 8: Responsive Design (Media Query)

```css
@media (max-width: 600px) {
  body {
    background-color: lightblue;
  }
}
```

---

## 🧪 अध्याय 9: Dummy Login Page Design (Practice)

### 📄 HTML (index.html)

```html
<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <title>Login Page</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="login-box">
    <h2>लॉग इन करें</h2>
    <form>
      <input type="text" placeholder="यूज़रनेम">
      <input type="password" placeholder="पासवर्ड">
      <button>Login</button>
    </form>
    <p><a href="#">पासवर्ड भूल गए?</a></p>
  </div>
</body>
</html>
```

---

### 🎨 CSS (style.css)

```css
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background: #f0f2f5;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-box {
  background: white;
  padding: 40px;
  border-radius: 10px;
  width: 300px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  text-align: center;
}

.login-box h2 {
  color: #333;
  margin-bottom: 20px;
}

.login-box input {
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.login-box button {
  width: 100%;
  padding: 12px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-box button:hover {
  background-color: #45a049;
}

.login-box a {
  text-decoration: none;
  color: #007BFF;
}
```

---

## 🧠 अध्याय 10: उपयोगी Tips

- HTML और CSS फ़ाइलों को एक ही फ़ोल्डर में रखें
- मोबाइल व्यू के लिए Media Query ज़रूर जोड़ें
- Ethical Hacking अभ्यास के लिए dummy pages का उपयोग करें (केवल ऑफलाइन)

---

## 📘 Extra Learning (Coming Next)

| टॉपिक | विवरण |
|-------|--------|
| Animation | CSS से स्लो/फेड इफेक्ट्स |
| Hover Effects | बटन पर माउस आने पर |
| Pseudo Classes | `:hover`, `:nth-child` |
| CSS Variables | Reusable वैल्यू |

---

## 📘 Extra Learning (एडवांस टॉपिक्स)

### 🎞️ 1. Animation – CSS से स्लो/फेड इफेक्ट

CSS में आप किसी भी एलिमेंट को Move, Fade, Rotate आदि कर सकते हैं।

🔹 उदाहरण:

```css
.box {
  width: 100px;
  height: 100px;
  background: red;
  animation: fadein 2s ease-in-out forwards;
}

@keyframes fadein {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

👉 इसे HTML में ऐसे लागू करें:

```html
<div class="box"></div>
```

---

### 🖱️ 2. Hover Effects – बटन पर माउस आने पर

जब माउस किसी बटन या डिव पर आता है, तब स्टाइल चेंज करना हो तो `:hover` उपयोग होता है।

🔹 उदाहरण:

```css
button {
  background-color: green;
  color: white;
  padding: 10px;
  border: none;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: darkgreen;
}
```

---

### 🧙‍♂️ 3. Pseudo Classes – विशेष selectors

CSS में कुछ विशेष selectors होते हैं, जिन्हें **Pseudo-classes** कहा जाता है।

| Pseudo Class | उपयोग |
|--------------|--------|
| `:hover` | माउस आने पर |
| `:first-child` | पहला child |
| `:last-child` | अंतिम child |
| `:nth-child(n)` | nth number पर |

🔹 उदाहरण:

```css
ul li:first-child {
  color: red;
}

ul li:nth-child(2) {
  font-weight: bold;
}
```

---

### 🧮 4. CSS Variables – Reusable वैल्यू

Variables से आप एक ही वैल्यू को बार-बार उपयोग कर सकते हैं।

🔹 डिफाइन करना:

```css
:root {
  --main-color: #4CAF50;
  --padding: 12px;
}
```

🔹 उपयोग करना:

```css
button {
  background-color: var(--main-color);
  padding: var(--padding);
}
```

📝 नोट: `:root` का मतलब HTML का root (global scope) है।

---


---

## 🧾 निष्कर्ष

✅ अब आप:

- CSS लिखना और जोड़ना सीख गए
- Selectors, Properties और Box Model समझ गए
- Dummy login डिज़ाइन बनाना सीखा

---

## 📦 फोल्डर स्ट्रक्चर

```
project-folder/
│
├── index.html
└── style.css
```

---


👨‍💻 बनाए रखा: Lucy (AI Hacking & Coding Teacher)

