import sqlite3
import uuid  # [新朋友] 用來產生亂碼 ID
from flask import Flask, render_template, request, g, url_for
import os # 記得在最上面 import os

app = Flask(__name__)
DATABASE = 'data.db'

# --- [新增] 自動初始化資料庫的函式 ---
def init_db_command():
    # 如果資料庫檔案不存在，才執行初始化
    if not os.path.exists(DATABASE):
        print("檢測到無資料庫，開始建立...")
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS secrets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT UNIQUE NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        db.commit()
        db.close()
        print("資料庫建立完成！")

# 讓 Flask 一啟動就先跑一次上面的檢查
with app.app_context():
    init_db_command()
# -----------------------------------

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- 1. 首頁：讓人輸入秘密 ---
@app.route("/", methods=['GET', 'POST']) # 預設下網頁只接受get 所以如果有post要顯式寫出來
def create_secret():
    if request.method == 'POST':
        secret_content = request.form.get('secret')
        
        # 產生一個唯一的亂碼 token (例如：a8098c1a-f86e-11da-bd1a-00112444be1e)
        token = str(uuid.uuid4())
        
        # 存入資料庫
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO secrets (token, content) VALUES (?, ?)', (token, secret_content))
        db.commit()
        
        # 產生給別人的網址
        # url_for('read_secret', token=token) 會幫你產生 /secret/亂碼
        # _external=True 代表產生「完整的網址」 (包含 http://...)
        secret_link = url_for('read_secret', token=token, _external=True)
        
        return render_template("result.html", link=secret_link)

    return render_template("index.html")

# --- 2. 讀取秘密 (閱後即焚！) ---
@app.route("/secret/<token>")
def read_secret(token):
    db = get_db()
    cursor = db.cursor()
    
    # 步驟 A：先試著要把秘密找出來
    cursor.execute('SELECT content FROM secrets WHERE token = ?', (token,))
    row = cursor.fetchone()
    
    if row:
        # 如果找得到秘密：
        secret_message = row[0]
        
        # 步驟 B：殘忍的時刻到了，馬上刪除！
        cursor.execute('DELETE FROM secrets WHERE token = ?', (token,))
        db.commit()
        
        # 步驟 C：顯示秘密給你看
        return render_template("secret.html", content=secret_message)
    else:
        # 如果找不到 (代表已經被看過銷毀了，或者是亂猜的)
        return "<h1>💥 錯誤！</h1><p>這則訊息已經自毀，或者根本不存在。</p>"

# 只有在我這個程式被直接run時我才會跑 如果只是被import不會跑
if __name__ == "__main__":
    # 改回 5001 避開 AirPlay
    app.run(debug=True, port=5001)