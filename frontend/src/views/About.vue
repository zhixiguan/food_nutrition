<script setup>
import { ElCard, ElDivider } from 'element-plus'
</script>

<template>
  <div class="about-container">
    
    
    <el-card class="info-card">
      <template #header>
        <div class="card-header">
          <span>数据来源</span>
        </div>
      </template>
      <div class="card-content">
        聚合数据（<a href="https://www.juhe.cn/market/product/id/11087" target="_blank">JUHE.CN</a>）
      </div>
    </el-card>

    <el-card class="info-card">
      <template #header>
        <div class="card-header">
          <span>AI开发工具</span>
        </div>
      </template>
      <div class="card-content">
        TRAE（<a href="https://www.trae.ai/" target="_blank">TRAE.AI</a>）
      </div>
    </el-card>

    <el-card class="info-card">
      <template #header>
        <div class="card-header">
          <span>技术栈</span>
        </div>
      </template>
      <div class="card-content tech-stack">
        <div class="tech-item">
          <span class="tech-name">Vue 3</span>
          <span class="tech-desc">前端框架</span>
        </div>
        <el-divider></el-divider>
        <div class="tech-item">
          <span class="tech-name">Element Plus</span>
          <span class="tech-desc">UI组件库</span>
        </div>
        <el-divider></el-divider>
        <div class="tech-item">
          <span class="tech-name">Vite</span>
          <span class="tech-desc">构建工具</span>
        </div>
        <el-divider></el-divider>
        <div class="tech-item">
          <span class="tech-name">FastAPI</span>
          <span class="tech-desc">后端框架</span>
        </div>
        <el-divider></el-divider>
        <div class="tech-item">
          <span class="tech-name">SQLite</span>
          <span class="tech-desc">数据库</span>
        </div>
      </div>
    </el-card>
  </div>
</template>

<style scoped>
.about-container {
  width: 100%;
  max-width: 480px;
  min-width: 300px;
  padding: 8px;
  margin-bottom: 50px;
  margin-top: 50px;
}

.page-title {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
  font-size: 28px;
}

.info-card {
  margin-bottom: 16px;
  border-radius: 8px;
  width: 100%;
}

.card-header {
  display: flex;
  align-items: center;
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
}

.card-content {
  font-size: 16px;
  color: #606266;
  line-height: 1.6;
  padding: 16px 0;
}

.tech-stack {
  padding: 8px 0;
}

.tech-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
}

.tech-name {
  font-weight: 600;
  color: #2c3e50;
}

.tech-desc {
  color: #909399;
}
</style>