from flask import Flask
from extension import db
from models import Book
import os

app = Flask(__name__)

# 获取当前文件所在的目录（也就是项目根目录）
basedir = os.path.abspath(os.path.dirname(__file__))

# 将数据库保存到项目根目录下，而不是 Flask 默认的 instance 目录
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'books.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止 SQLAlchemy 进行追踪

db.init_app(app)

@app.route('/')
def hello_world():
    return 'Welcome Books!'

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()

if __name__ == '__main__':
    app.run(debug=True)
