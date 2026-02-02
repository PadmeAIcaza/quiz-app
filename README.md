# Quizzzzler (Tkinter Trivia Quiz)

A simple **True/False trivia quiz** desktop app built with **Python + Tkinter**.  
It pulls questions from the **Open Trivia DB API**, shows them one by one, and updates your score with instant feedback (green/red background).

---

## Features
- ✅ True/False questions (10 by default)
- ✅ Score tracking
- ✅ Instant visual feedback after each answer
- ✅ Questions are HTML-unescaped (so stuff like `&quot;` renders properly)

---

## Tech Stack
- **Python**
- **Tkinter** (GUI)
- **requests** (API calls)

---

## Project Structure
```markdown
project/
├─ src/
│ ├─ main.py
│ ├─ data.py
│ ├─ question_model.py
│ └─ ui.py
└─ images/
├─ T.png
└─ F.png
```

> ⚠️ `images/` is required because the UI loads:
> - `../images/T.png`
> - `../images/F.png`

So the `images` folder must be **next to** `src`, not inside it.

---

## Setup

### 1) Install dependencies
```bash
pip install requests
