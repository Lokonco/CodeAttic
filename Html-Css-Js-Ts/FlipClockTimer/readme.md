# 🕐 Flip Clock Timer

A stylish countdown timer with a satisfying flip-clock animation, built with vanilla HTML, CSS, and JavaScript.

---

## 📸 Preview

> A retro-style flip clock that counts down hours, minutes, and seconds — complete with smooth 3D flip animations and a frosted-glass input panel.

---

## 🚀 Features

- **Flip animation** — smooth 3D card-flip effect on every digit change
- **Custom timer input** — set your own hours, minutes, and seconds
- **Preset buttons** — quickly jump to 5, 15, 25 minutes, or 1 hour
- **Start / Pause / Reset** controls
- **Glassmorphism UI** — modern frosted-glass styling over a background image

---

## 📁 Project Structure

```
FlipClockTimer/
├── index.html      # Markup — flip clock segments, input panel, controls
├── logic.js         # Logic — timer countdown, flip animations, user input
├── style.css       # Styling — flip card layout, animations, glassmorphism
└── Images/
    └── orangeBackGround.jpg
```

---

## 🛠️ How It Works

### `index.html`
Defines the structure of the flip clock. Each digit is broken into a **top half** and **bottom half**, plus an **overlay** that animates on top to create the flip illusion. There are three sections: Hours, Minutes, and Seconds.

### `logic.js`
Handles all the timer logic:
- Reads user input and calculates a `targetDate` using the current time + offset
- Uses `setInterval` to tick every second
- On each tick, calculates the remaining time and updates each digit
- Triggers the CSS flip animation only when a digit actually changes

### `style.css`
Styles the flip segments using `position: absolute` layering and CSS `@keyframes` for the 3D rotation effect:
- `flip-top` — rotates the top half away (0° → -90°)
- `flip-bottom` — rotates the bottom half into view (90° → 0°)

---

## ▶️ Getting Started

No dependencies or build tools needed — just open in a browser.

```bash
# Clone or download the project, then open:
index.html
```

Or drag `index.html` into any modern browser.

---

## 🎯 Usage

1. Enter your desired hours, minutes, and/or seconds — **or** click a preset
2. Hit **Start Timer**
3. Use **Pause** to freeze the countdown
4. Use **Reset** to clear everything back to `00:00:00`

---

## 🧰 Built With

- HTML5
- CSS3 (Keyframe Animations, Flexbox, Glassmorphism)
- Vanilla JavaScript (DOM manipulation, `setInterval`, `Date` API)
- [Fira Sans](https://fonts.google.com/specimen/Fira+Sans) via Google Fonts

---
