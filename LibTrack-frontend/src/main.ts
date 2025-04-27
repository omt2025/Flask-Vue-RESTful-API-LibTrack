import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import App from './App.vue'
import router from './router'

const app = createApp(App)

// 安装插件
app.use(createPinia())
app.use(router)

// ✅ 安装 Element Plus，并配置语言（可选）
app.use(ElementPlus, {
  locale: zhCn,
})

app.mount('#app')
