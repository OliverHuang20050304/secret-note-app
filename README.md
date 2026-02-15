# 閱後即焚秘密傳遞工具
## 專案概述
本專案的功能是讓使用者可以輸入一段訊息後，系統會產生一個連結，使用者可以將該連結分享給朋友，朋友打開後可以閱讀，此時訊息會被刪除。如果重載或是別人打開同樣的連結，會因為訊息已被刪除而無法讀取。

## 如何執行
### 創建虛擬環境
```bash
python3 -m venv venv
```
### 啟動虛擬環境
```bash
source venv/bin/activate
```
### 安裝相關套件
```bash
pip install -r requirements.txt
```
### 啟動伺服器
```bash
python app.py
```
啟動伺服器後打開http://127.0.0.1:5001 即可使用。