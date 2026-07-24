<div align="center">

# 👻 Ghost Courier

### Covert Messaging · Three-Layer Security Protocol

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Visit_Site-00ffe7?style=for-the-badge&labelColor=050810)](https://itz-mridul.github.io/ghost-courier/)
[![GitHub Stars](https://img.shields.io/github/stars/Itz-Mridul/ghost-courier?style=for-the-badge&color=00ffe7&labelColor=050810)](https://github.com/Itz-Mridul/ghost-courier/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Itz-Mridul/ghost-courier?style=for-the-badge&color=a259ff&labelColor=050810)](https://github.com/Itz-Mridul/ghost-courier/network)
[![HTML](https://img.shields.io/badge/HTML-100%25-ff6b35?style=for-the-badge&logo=html5&logoColor=white&labelColor=050810)](https://github.com/Itz-Mridul/ghost-courier)
[![License](https://img.shields.io/badge/License-MIT-00ffe7?style=for-the-badge&labelColor=050810)](LICENSE)

<br/>

```
                                         ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
                                        ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
                                        ██║  ███╗███████║██║   ██║███████╗   ██║   
                                        ██║   ██║██╔══██║██║   ██║╚════██║   ██║   
                                        ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
                                         ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝  
                                    ██████╗ ██████╗ ██╗   ██╗██████╗ ██╗███████╗██████╗
                                  ██╔════╝██╔═══██╗██║   ██║██╔══██╗██║██╔════╝██╔══██╗
                                  ██║     ██║   ██║██║   ██║██████╔╝██║█████╗  ██████╔╝
                                  ██║     ██║   ██║██║   ██║██╔══██╗██║██╔══╝  ██╔══██╗
                                  ╚██████╗╚██████╔╝╚██████╔╝██║  ██║██║███████╗██║  ██║
                                   ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
```

**[🌐 Live Website](https://itz-mridul.github.io/ghost-courier/)** &nbsp;•&nbsp; **[👤 Author](https://github.com/Itz-Mridul)** &nbsp;•&nbsp; **[⭐ Star this Repo](https://github.com/Itz-Mridul/ghost-courier/stargazers)**

</div>

---

## 🕵️ What is Ghost Courier?

> **Ghost Courier** is a sleek, browser-based covert messaging tool that lets you **encrypt**, **decrypt**, and **hide secret messages inside images** — all without any server, all in real-time.

Built with a cyberpunk dark-mode UI, Ghost Courier combines **three security layers** into one seamless experience:

| Layer | Technology | Purpose |
|-------|-----------|---------|
| 🔐 **Confidentiality** | Caesar Cipher | Encrypts your message text |
| 🔗 **Integrity** | SHA-256 Hash | Verifies message hasn't been tampered |
| 🖼️ **Obfuscation** | LSB Steganography | Hides the encrypted message inside an image |

---

## ✨ Features

- **🔐 Text Encryption** — Caesar Cipher with a configurable shift key (1–25), generates a bundled package containing ciphertext + SHA-256 hash
- **🔓 Text Decryption** — Paste the package back, enter the key, and verify message integrity in one click
- **🖼️ Hide in Image** — Embed an encrypted message invisibly into any PNG/JPG/WEBP using LSB steganography
- **🔍 Reveal from Image** — Extract and decrypt a hidden message from a stego image
- **📋 Copy Package** — One-click copy of the encrypted payload
- **⬇️ Download Stego Image** — Save your image with the hidden message embedded
- **🌑 Cyberpunk Dark UI** — Animated scanlines, glowing accents, and a stunning Orbitron + Share Tech Mono typeface
- **📱 Fully Responsive** — Works beautifully on mobile and desktop

---

## 🌐 Live Demo

> Try it right now — no installation needed!

**👉 [https://itz-mridul.github.io/ghost-courier/](https://itz-mridul.github.io/ghost-courier/)**

---

## 🚀 How to Use

### 🔐 Encrypting a Message

1. Click the **ENCRYPT** tab
2. Type your secret message in the plaintext field
3. Set a **Shift Key** (default: 13 — like ROT13)
4. Click **⚡ ENCRYPT**
5. Copy the generated **Package** (ciphertext + SHA-256 hash) and share it

### 🔓 Decrypting a Message

1. Click the **DECRYPT** tab
2. Paste the encrypted **Package** you received
3. Enter the same **Shift Key** used during encryption
4. Click **🔓 DECRYPT**
5. The original message appears, with **integrity verification** (✅ PASS / ❌ FAIL)

### 🖼️ Hiding a Message in an Image

1. Click the **HIDE** tab
2. Upload a carrier image (PNG/JPG/WEBP)
3. Type your secret message and set a shift key
4. Click **🕵️ HIDE**
5. **Download** the stego image — it looks identical to the original!

### 🔍 Revealing a Hidden Message

1. Click the **REVEAL** tab
2. Upload the stego image you received
3. Enter the shift key
4. Click **🔍 REVEAL** — the hidden message is extracted and decrypted

---

## 🔬 How It Works

```
┌──────────────────────────────────────────────────────────┐
│                   GHOST COURIER PIPELINE                 │
│                                                          │
│  Plaintext ──► Caesar Cipher ──► Ciphertext              │
│                    │                  │                  │
│                    │            SHA-256 Hash             │
│                    │                  │                  │
│                    └──────────────────┘                  │
│                           │                              │
│                    Encrypted Package                     │
│                    (ciphertext||hash)                    │
│                           │                              │
│                    LSB Steganography                     │
│                           │                              │
│                    Carrier PNG Image                     │
│                           │                              │
│                  👻 Stego Image Output                   │
└──────────────────────────────────────────────────────────┘
```

### Caesar Cipher
Each letter is shifted by `N` positions in the alphabet. For example, with shift 3: `A → D`, `B → E`, etc. Non-alphabetic characters pass through unchanged.

### SHA-256 Integrity
After encryption, a SHA-256 hash of the **ciphertext** is computed using the Web Crypto API and appended to the package. On decryption, the hash is recomputed and compared — any tampering is instantly detected.

### LSB Steganography
The message bits are embedded into the **Least Significant Bit** of each pixel's color channels (R, G, B). This change is imperceptible to the human eye, making the image visually identical to the original.

---

## 🛠️ Tech Stack

| Technology | Usage |
|-----------|-------|
| `HTML5` | Structure and layout |
| `Vanilla CSS` | Cyberpunk dark-mode design with animations |
| `Vanilla JavaScript` | All crypto logic, UI interactions |
| `Web Crypto API` | SHA-256 hashing (native browser API) |
| `Canvas API` | LSB pixel manipulation for steganography |
| `Google Fonts` | Orbitron · Share Tech Mono · Exo 2 |

> ✅ **Zero dependencies. Zero servers. Zero data collection.** Everything runs locally in your browser.

---

## 📁 Project Structure

```
ghost-courier/
└── 📄 index.html    # Complete single-file app (HTML + CSS + JS)
```

---

## ⚠️ Security Notice

> [!NOTE]
> Ghost Courier is a **demonstration tool** for educational purposes. Caesar Cipher is a classical cipher and **not cryptographically secure** for real-world sensitive data. For production-level security, use AES-256 or RSA encryption.

---

## 🤝 Contributing

Pull requests are welcome! Ideas for improvements:

- 🔑 Add AES-256 encryption support
- 🎨 Multiple UI themes
- 📁 Support for more image formats
- 🧪 Add unit tests for crypto functions

```bash
# Fork and clone the repo
git clone https://github.com/Itz-Mridul/ghost-courier.git

# Open in browser (no build step needed!)
open index.html
```

---

## 🔗 Links

| Resource | URL |
|----------|-----|
| 🌐 **Live Website** | [itz-mridul.github.io/ghost-courier](https://itz-mridul.github.io/ghost-courier/) |
| 📦 **Repository** | [github.com/Itz-Mridul/ghost-courier](https://github.com/Itz-Mridul/ghost-courier) |
| 👤 **Author Profile** | [github.com/Itz-Mridul](https://github.com/Itz-Mridul) |
| 🐛 **Report a Bug** | [Open an Issue](https://github.com/Itz-Mridul/ghost-courier/issues/new) |

---

<div align="center">

Made with 🔐 by **[Mridul](https://github.com/Itz-Mridul)**

*If Ghost Courier was useful, drop a ⭐ — it means a lot!*

[![GitHub](https://img.shields.io/badge/GitHub-Itz--Mridul-181717?style=for-the-badge&logo=github)](https://github.com/Itz-Mridul)

</div>
