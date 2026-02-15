import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# 為了乾淨，我們先把舊的表格刪掉 (實務上要小心，但練習時沒關係)
cursor.execute('DROP TABLE IF EXISTS secrets')

# 建立新的 secrets 表格
# token 是唯一的 (UNIQUE)，不能重複
cursor.execute('''
    CREATE TABLE secrets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token TEXT UNIQUE NOT NULL,
        content TEXT NOT NULL
    )
''')

connection.commit()
connection.close()
print("新的秘密資料庫已建立！舊資料已銷毀。")