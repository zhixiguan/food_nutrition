<script setup>
import { ElDivider } from 'element-plus'
</script>

<template>
  <div class="top-nav">
    <div class="nav-content">
      <h1 class="app-title">食物营养成分查询手册</h1>
    </div>
  </div>
</template>

<style scoped>
.top-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: #409EFF;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-content {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0.8rem 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.app-title {
  margin: 0;
  font-size: 1.25rem;
  color: white;
  font-weight: 600;
}
</style>