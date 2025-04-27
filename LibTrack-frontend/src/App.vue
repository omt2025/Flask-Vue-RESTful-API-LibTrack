<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 定义一个响应式变量，用于存储从后端获取的书籍数据
const books = ref([])

// 获取书籍的 API 请求
const fetchBooks = async () => {
  try {
    const response = await axios.get('http://localhost:5000/books/')  // 后端 API 地址
    books.value = response.data.results  // 假设返回的数据是 { results: [...] }
  } catch (error) {
    console.error('Error fetching books:', error)
  }
}

// 删除书籍的 API 请求
const handleDelete = async (bookId: number) => {
  try {
    await axios.delete(`http://localhost:5000/books/${bookId}`)
    fetchBooks()  // 删除成功后刷新书籍列表
  } catch (error) {
    console.error('Error deleting book:', error)
  }
}

// 编辑书籍的逻辑（目前只是一个占位函数，稍后可以添加编辑功能）
const handleEdit = (index: number, row: any) => {
  console.log('Editing book', row)
}

// 在组件加载时调用 fetchBooks 获取数据
onMounted(() => {
  fetchBooks()
})
</script>

<template>
  <div class="layout-container">
    <div class="layout-content">
      <h1 class="page-title">图书管理系统</h1>

      <!-- 添加图书按钮 -->
      <el-button type="primary" @click="add_dialog_visible = true" size="small">添加图书</el-button>

      <!-- 图书数据表格 -->
      <el-table :data="books" style="margin: 20px auto;">
        <el-table-column label="编号" prop="book_number"/>
        <el-table-column label="书名" prop="book_name"/>
        <el-table-column label="类型" prop="book_type"/>
        <el-table-column label="价格" prop="book_prize"/>
        <el-table-column label="作者" prop="author"/>
        <el-table-column label="出版社" prop="book_publisher"/>
        <el-table-column align="right" label="操作" width="200px">
          <template #default="scope">
            <el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<style>
/* 初始化样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* 确保 body 和 html 元素占满整个页面 */
html, body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
}

/* 确保 #app 元素没有多余的外边距和填充 */
#app {
  width: 100%;  /* 使 #app 占满整个页面 */
  height: 100%; /* 保证占满高度 */
  margin: 0;    /* 清除外边距 */
  padding: 0;   /* 清除填充 */
  display: flex; /* 如果有flex布局需求，可以加上这个 */
  justify-content: center;
  align-items: center;
}

/* 外层容器，撑满整个屏幕并居中 */
.layout-container {
  display: flex;
  justify-content: center;  /* 水平居中 */
  align-items: center;      /* 垂直居中 */
  min-height: 100vh;        /* 保证容器至少撑满屏幕 */
  padding: 20px;            /* 添加一点内边距 */
  width: 100%;              /* 确保父容器宽度为100% */
}

/* 内容容器，保持卡片效果 */
.layout-content {
  width: 100%;
  max-width: 1200px;        /* 最大宽度为1200px */
  background: #fff;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}

/* 页面标题 */
.page-title {
  text-align: center;
  font-size: 28px;
  margin-bottom: 30px;
}

/* 按钮区域 */
.action-bar {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .layout-content {
    padding: 20px;
    border-radius: 8px;
  }
}


</style>
