import sqlite3

# 连接数据库
conn = sqlite3.connect("books.sqlite")

# 获取游标
cursor = conn.cursor()

# 查询表列表
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("表名：", cursor.fetchall())

# 如果有某张表，比如 books，你可以查看它的内容
cursor.execute("SELECT * FROM books;")
for row in cursor.fetchall():
    print(row)

conn.close()
