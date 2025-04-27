import sqlite3


def view_all_tables(db_path):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 查询所有表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("❗ 数据库中没有表。")
        return

    print(f"📚 数据库中共有 {len(tables)} 张表：")
    for name_tuple in tables:
        table_name = name_tuple[0]
        print(f"\n🔸 表名: {table_name}")

        # 打印每张表的所有内容
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print("   ", row)
        else:
            print("   （空表）")

    conn.close()


if __name__ == "__main__":
    view_all_tables("books.sqlite")  # 如果你的文件路径不同，请修改这里
