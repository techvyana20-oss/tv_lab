# 🛡 TechVyana Cyber Lab Suite v4.0

TechVyana Cyber Lab Suite is a modular, defensive cybersecurity toolkit
built in Python.

It provides tools for: - File integrity verification - Secure password
generation - Cryptographic hashing - Role-based authentication -
Activity logging & analytics - Plugin-based architecture

This project is designed for educational and defensive cybersecurity
research purposes.

------------------------------------------------------------------------

## 🚀 Features

### 🔐 1. Integrity Plugin

-   Calculate SHA256 and MD5 for files
-   Verify file integrity against known hash
-   Detect potential file tampering

### 🔑 2. Password Plugin

-   Generate secure random passwords
-   Calculate password entropy
-   Evaluate password strength mathematically

### 🔒 3. Hash Plugin

-   Hash text or files
-   Supports SHA256, SHA1, and MD5
-   Outputs HEX and Base64 format

### 📊 4. Admin Analytics

-   Tracks tool usage
-   Logs activity to SQLite database
-   Displays usage statistics (admin only)

------------------------------------------------------------------------

## 🧠 Use Cases

### ✅ File Verification

Verify downloaded files against official checksums to ensure integrity.

### ✅ Cybersecurity Training

Learn how hashing works and understand entropy in password security.

### ✅ Digital Forensics Practice

Hash files and verify that evidence has not been altered.

### ✅ Secure Password Research

Generate strong passwords and study brute-force resistance.

------------------------------------------------------------------------

## 📦 Installation

Clone the repository:

git clone https://github.com/techvyana20-oss/tv_lab.git
git cd tv_lab

Install dependencies:

pip install cryptography

Run the application:

python main.py

------------------------------------------------------------------------

## 🏗 Architecture

-   Plugin-based tool system
-   SQLite backend
-   Role-based authentication
-   Activity logging
-   Modular core structure

------------------------------------------------------------------------

## 🛣 Roadmap

### Phase 1 -- Cryptography Enhancements

-   [ ] Directory-wide recursive integrity scanner
-   [ ] HMAC generation & verification
-   [ ] File comparison tool

### Phase 2 -- Secure Storage

-   [ ] Encrypted vault (AES-based)
-   [ ] Trusted hash baseline storage

### Phase 3 -- UI Improvements

-   [ ] Rich dashboard UI
-   [ ] Progress bars & visual stats
-   [ ] CLI argument support

### Phase 4 -- Lab Expansion

-   [ ] Entropy visualizer
-   [ ] File monitoring system
-   [ ] Plugin permission control

------------------------------------------------------------------------

## ⚠ Security Notice

This project is built strictly for: - Educational purposes - Defensive
cybersecurity research - Cryptography learning

It does NOT provide: - Offensive attack automation - Exploitation
tools - Network intrusion modules

------------------------------------------------------------------------

## 👨‍💻 Author

TechVyana2.0

------------------------------------------------------------------------

## 📜 License

MIT License
