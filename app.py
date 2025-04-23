from flask import Flask, request
from flask.views import MethodView
from extension import db, cors  # 引入扩展模块（数据库和跨域支持）
from models import Book  # 引入 Book 模型（表示数据库中的书籍表）

import os

app = Flask(__name__)  # 创建 Flask 应用实例
cors.init_app(app)  # 初始化跨域支持（CORS）

# 获取当前文件的绝对路径（项目根目录）
basedir = os.path.abspath(os.path.dirname(__file__))

# 配置数据库连接，使用 SQLite 并将数据文件保存在项目根目录下
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'books.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁用 SQLAlchemy 的事件系统（提升性能）

db.init_app(app)  # 初始化数据库对象


# 定义根路径路由，返回欢迎信息
@app.route('/')
def hello_world():
    return 'Welcome Books!'


# 自定义 Flask CLI 命令：create，用于初始化数据库
@app.cli.command()
def create():
    db.drop_all()  # 删除所有表（注意：生产环境慎用）
    db.create_all()  # 创建所有模型对应的表
    Book.init_db()  # 使用 Book 模型中定义的方法初始化测试数据（你需要在 models.py 中实现这个方法）


# 定义一个基于类的视图，用于处理 /books/ 路由
class BookApi(MethodView):
    def get(self, book_id=None):
        if book_id is None:
            # 查询所有书籍
            books: [Book] = Book.query.all()
            results = [
                {
                    'id': book.id,
                    'book_name': book.book_name,
                    'book_type': book.book_type,
                    'book_prize': book.book_prize,
                    'book_number': book.book_number,
                    'book_publisher': book.book_publisher,
                    'author': book.author,
                } for book in books
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }
        else:
            # 查询特定书籍
            book = Book.query.get(book_id)
            if not book:
                return {'status': 'error', 'message': '未找到该书籍'}, 404

            result = {
                'id': book.id,
                'book_name': book.book_name,
                'book_type': book.book_type,
                'book_prize': book.book_prize,
                'book_number': book.book_number,
                'book_publisher': book.book_publisher,
                'author': book.author,
            }
            return {
                'status': 'success',
                'message': '单本书籍查询成功',
                'result': result
            }

    def post(self):
        # 这里处理添加书籍的逻辑
        form = request.json
        book = Book()
        book.book_number = form.get('book_number')
        book.book_name = form.get('book_name')
        book.book_type = form.get('book_type')
        book.book_prize = form.get('book_prize')
        book.author = form.get('author')
        book.book_publisher = form.get('book_publisher')
        db.session.add(book)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据添加成功'
        }

    def delete(self, book_id):
        # 这里处理删除书籍的逻辑
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()

        return {
            'status': 'success',
            'message': '数据删除成功'
        }




# 将 BookApi 类视图注册到路由 /books/，只允许 GET 方法
book_view = BookApi.as_view('book_api')
app.add_url_rule('/books/',
                 view_func=book_view, methods=['GET', ])
app.add_url_rule('/books/',
                 view_func=book_view, methods=['POST', ])
app.add_url_rule('/books/<int:book_id>',
                 view_func=book_view, methods=['GET', 'PUT', 'DELETE'])

# 启动应用（开发模式下，自动重载，显示详细错误）
if __name__ == '__main__':
    app.run(debug=True)
