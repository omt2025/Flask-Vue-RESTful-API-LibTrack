# 📚 LibTrack: Book Information Management System

**LibTrack** 是一个完整的书籍管理应用，采用 **Flask** 构建后端，**Vue 3** 构建前端，**Element Plus** 作为 UI 组件库，展示了清晰的前后端分离架构，使用 **Axios** 进行 HTTP 请求。

这个项目让用户能够管理书籍记录，具备书籍的增加、编辑、删除、查看等功能，并支持强大的搜索和过滤功能。

---

## 🚀 Features

- 📖 **增加**、**编辑**、**删除**、**查看** 书籍记录。
- 🔍 **搜索与过滤** 功能，支持根据书籍的属性（如书名、作者、出版社）查找书籍。
- 🛠️ **RESTful API** 用于处理前端和后端之间的交互请求。
- 💾 **SQLite 数据库** 集成，提供轻量级、易于使用的存储方式。
- 🎨 使用 **Vue 3** 和 **Element Plus** 打造的 **响应式用户界面**，确保在任何设备上都能流畅体验。
- 🔗 **前后端分离**，使用 **Axios** 进行数据请求，保持架构清晰和易于维护。

---

## 🧰 Tech Stack

| 层级        | 技术                    |
|-------------|-------------------------|
| 后端        | Flask, Flask-SQLAlchemy |
| 前端        | Vue 3, Element Plus     |
| API 客户端  | Axios                   |
| 数据库      | SQLite                  |
| 开发工具    | PyCharm, VSCode, Git    |

---

## 📂 Project Structure

```bash
LibTrack/
├── app.py                # Flask 应用入口文件，包含路由处理和 API 配置
├── models.py             # 数据库模型（如 Book 模型）及其 Schema 定义
├── extension.py          # 数据库扩展和配置，初始化 Flask-SQLAlchemy
├── instance/books.sqlite # 存储所有书籍记录的 SQLite 数据库文件
├── view_db.py            # 用于检查或可视化数据库内容的工具脚本
├── frontend/             # Vue.js 前端项目文件夹，包含前端代码
│   ├── src/              # Vue 组件、状态管理、路由配置
│   └── ...
└── README.md             # 项目文档

📝 更新记录 (04/23)
使用 npm create vue@latest 初始化 Vue 3 项目

项目配置选择：

✅ TypeScript

✅ Vue Router（路由）

✅ Pinia（状态管理）

✅ ESLint + Prettier（代码规范）

分析并注释了 main.ts 的项目启动流程

替换 JavaScript 写法为 TypeScript 等效写法

安装并引入 Element Plus 组件库及样式

配置 Element Plus 中文语言包（zh-cn）

验证应用正常挂载，并支持路由与状态管理
