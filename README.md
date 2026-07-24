<div align="center">

# 🎨 GitHub Contribution Pattern Maker

### Paint your GitHub profile with stunning visual patterns using backdated commits!

[![GitHub Stars](https://img.shields.io/github/stars/Itz-Mridul/Krishna?style=for-the-badge&color=39d353&labelColor=0d1117)](https://github.com/Itz-Mridul/Krishna/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Itz-Mridul/Krishna?style=for-the-badge&color=39d353&labelColor=0d1117)](https://github.com/Itz-Mridul/Krishna/network)
[![GitHub Issues](https://img.shields.io/github/issues/Itz-Mridul/Krishna?style=for-the-badge&color=39d353&labelColor=0d1117)](https://github.com/Itz-Mridul/Krishna/issues)
[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-39d353?style=for-the-badge)](LICENSE)

<br/>

```
╔═════════════════════════════════════════════════════════════╗
║  ░░░ ░   ░ ░░░░ ░░░░ ░░░░ ░   ░░░░ ░░░░ ░  ░ ░░░░ ░  ░   ║
║  █ █ ██ ██ █  █  ██  ██   ██  ██   ██   █ ██ ██   █ █    ║
║  █ █ █ █ █ ████  ██  ████ █ █ ████ ████ ██ █ ████ ██      ║
║  █ █ █   █ █  █  ██  ██   █ █ ██   ██   █  █ ██   █ █    ║
║  ███ █   █ █  █ ████ ████ █   ████ ██   █  █ ████ █  ███  ║
╚═════════════════════════════════════════════════════════════╝
```

**[🔗 View on GitHub](https://github.com/Itz-Mridul/Krishna)** • **[👤 Author Profile](https://github.com/Itz-Mridul)** • **[⭐ Star this repo](https://github.com/Itz-Mridul/Krishna/stargazers)**

</div>

---

## ✨ What is this?

> **GitHub Contribution Pattern Maker** is a Python automation tool that creates **backdated commits** on specific dates to "paint" beautiful visual patterns onto your GitHub contribution graph — turning your activity heatmap into a work of art!

GitHub's contribution graph is a **52 × 7 grid** where each cell represents one day. The more commits on a day, the darker green the cell. This tool exploits that by generating commits with custom past dates to draw any shape or text you want!

---

## 🖼️ Available Patterns

| Pattern | Symbol | Preview |
|---------|--------|---------|
| `HEART` | ❤️ | Heart shape drawn across the graph |
| `STAR` | 🌟 | A glowing star with gradient shading |
| `ZIGZAG` | ⚡ | Sharp zigzag lightning waves |
| `DIAGONAL` | 📊 | Elegant diagonal stripes |
| `HI` | 👋 | Writes the word "HI" in pixels |
| `MRIDUL` | 🔤 | Writes "MRIDUL" in custom pixel font |
| `WAVE` | 🌊 | A smooth flowing sine wave |
| `MOUNTAIN` | 🏔️ | Majestic mountain peak silhouettes |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.6+** installed
- **Git** configured with your identity
- A **GitHub repository** to push to

### Installation & Usage

```bash
# 1. Clone this repository
git clone https://github.com/Itz-Mridul/Krishna.git
cd Krishna

# 2. Choose your pattern in contribute.py
#    Open the file and set PATTERN = HEART (or any other preset)

# 3. Run the script
python3 contribute.py

# 4. Follow the on-screen preview and confirm
#    (It shows a text preview of the pattern before making any changes)

# 5. Push your commits to GitHub
git push origin main

# 6. Check your GitHub profile! 🎉
#    Visit: https://github.com/Itz-Mridul
```

---

## ⚙️ Configuration

Open `contribute.py` and tweak these settings at the top:

```python
# 👇 SELECT YOUR PATTERN (change to any preset name)
PATTERN = HEART

# How many weeks ago should the pattern START?
# GitHub shows ~52 weeks. Higher = further left on the graph.
START_WEEKS_AGO = 40

# Commit counts per intensity level
COMMITS_PER_LEVEL = {
    '1': 2,   # 🟩 light green  (1-3 commits)
    '2': 5,   # 🟩 medium green (4-6 commits)
    '3': 8,   # 🟩 dark green   (7-9 commits)
    '4': 12,  # 🟩 darkest green (10+ commits)
}
```

---

## 🎨 Custom Pattern Guide

Draw your own pattern using this simple grid system:

```
'.' = empty cell  (no commits — stays grey)
'1' = light green  (1-3 commits)
'2' = medium green (4-6 commits)
'3' = dark green   (7-9 commits)
'4' = darkest green (10+ commits)
```

**Grid orientation:**
- Each **row** = day of week (`Sunday → Saturday`, top to bottom)
- Each **column** = one week (reads **left → right**)

**Example — Drawing a simple cross (+):**

```python
MY_PATTERN = [
    ". . . 3 . . .",
    ". . . 3 . . .",
    ". . . 3 . . .",
    "3 3 3 4 3 3 3",
    ". . . 3 . . .",
    ". . . 3 . . .",
    ". . . 3 . . .",
]

PATTERN = MY_PATTERN
```

---

## 🔬 How It Works

```
┌─────────────────────────────────────────────────────┐
│                GitHub Contribution Graph             │
│                                                      │
│  Sun  [░][░][▒][▓][█][▓][▒][░][ ][ ][ ][ ]        │
│  Mon  [░][▒][▓][█][█][▓][▒][░][ ][ ][ ][ ]        │
│  Tue  [ ][▒][▓][█][█][▓][▒][ ][ ][ ][ ][ ]        │
│  Wed  [ ][ ][▓][█][█][▓][ ][ ][ ][ ][ ][ ]        │
│  Thu  [ ][ ][ ][▓][▓][ ][ ][ ][ ][ ][ ][ ]        │
│  Fri  [ ][ ][ ][ ][▒][ ][ ][ ][ ][ ][ ][ ]        │
│  Sat  [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]        │
│                                                      │
│        ← 52 weeks wide                              │
└─────────────────────────────────────────────────────┘
```

1. **Script calculates** target dates based on `START_WEEKS_AGO` and pattern grid
2. **For each active cell**, it writes to `contributions.txt` and creates a backdated Git commit
3. **Git commit timestamps** are set using `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` env variables
4. **After pushing**, GitHub reads these timestamps and fills in the contribution graph accordingly

---

## 📁 Project Structure

```
Krishna/
├── 📄 contribute.py       # Main script — patterns + logic
├── 📄 contributions.txt   # Auto-generated file written by each commit
└── 📄 README.md           # You're reading this!
```

---

## ⚠️ Important Notes

> **Note**: This tool modifies your GitHub contribution graph using backdated commits. This is allowed by GitHub but use responsibly — it's meant for fun and personalization.

- ✅ Works on any public/private GitHub repository
- ✅ Pattern appears on your profile within a few minutes of pushing
- ⚠️ Make sure you're in the **correct repository** before running
- ⚠️ A large pattern may create **hundreds of commits** — this is expected

---

## 🔗 Links

| Resource | Link |
|----------|------|
| 🏠 **Repository** | [github.com/Itz-Mridul/Krishna](https://github.com/Itz-Mridul/Krishna) |
| 👤 **Author Profile** | [github.com/Itz-Mridul](https://github.com/Itz-Mridul) |
| 🐛 **Report a Bug** | [Open an Issue](https://github.com/Itz-Mridul/Krishna/issues/new) |
| ⭐ **Star this Project** | [Give it a Star!](https://github.com/Itz-Mridul/Krishna/stargazers) |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/new-pattern`
3. **Add** your pattern or feature
4. **Commit** your changes: `git commit -m "Add: cool new pattern"`
5. **Push** and open a **Pull Request**

---

<div align="center">

Made with ❤️ by **[Mridul](https://github.com/Itz-Mridul)**

*If you found this useful, give it a ⭐ — it means a lot!*

[![GitHub](https://img.shields.io/badge/GitHub-Itz--Mridul-181717?style=for-the-badge&logo=github)](https://github.com/Itz-Mridul)

</div>
