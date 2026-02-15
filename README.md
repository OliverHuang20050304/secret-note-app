# 🤫 Secret Note App (Mission Impossible Style)

> "This message will self-destruct in 5 seconds..." well, actually, immediately after reading.

這是一個基於 Python Flask 開發的「閱後即焚」秘密便條服務。
使用者可以建立加密的訊息連結，接收者在讀取一次後，訊息就會從資料庫中**永久刪除**，確保隱私與安全性。

---

## 🚀 線上體驗 (Live Demo)

👉 **點擊這裡試用：[[這裡](https://oliver-secret-note.onrender.com)]**


---

## ✨ 功能特色 (Features)

* **🔒 閱後即焚 (Burn After Reading)**：
    * 採用「讀取即刪除」機制。當訊息被提取 (GET request) 後，後端會立即執行 `DELETE` 指令，確保資料無法被二次讀取。
* **🔑 唯一識別碼 (UUID)**：
    * 使用 Python `uuid` 模組產生不可預測的唯一亂碼連結，防止暴力破解。
* **📱 響應式設計 (Mobile Responsive)**：
    * 介面針對手機端優化，自動調整輸入框與按鈕大小，提供最佳的使用者體驗 (UX)。
* **🛠 自動初始化 (Auto-Init DB)**：
    * 系統啟動時自動檢查並建立 SQLite 資料庫，無需手動設定。
* **☁️ 雲端部署 (Cloud Ready)**：
    * 支援 Gunicorn WSGI Server，已優化並部署於 Render 平台。

---

## 🛠️ 使用技術 (Tech Stack)

* **Backend:** Python 3, Flask
* **Database:** SQLite (輕量化檔案型資料庫)
* **Frontend:** HTML5, CSS3 (RWD)
* **Deployment:** Render, Gunicorn
* **Version Control:** Git, GitHub

---

## 💻 如何在本地端執行 (Local Installation)

如果你想在自己的電腦上運行此專案，請按照以下步驟操作：

### 1. 複製專案 (Clone Repository)
```bash
git clone https://github.com/OliverHuang20050304/secret-note-app.git
cd secret-note-app
```
### 2. 建立虛擬環境 (Virtual Environment)

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
### Windows
```bash
python -m venv venv
venv\Scripts\activate
```
## 3. 安裝依賴套件 (Install Dependencies)
```bash
pip install -r requirements.txt
```
## 4. 啟動伺服器 (Run Server)
```bash
python app.py
```
現在打開瀏覽器前往 http://127.0.0.1:5001 即可使用！

