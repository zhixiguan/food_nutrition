<script setup>
import { ref, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { House, Search, InfoFilled } from '@element-plus/icons-vue'

const router = useRouter()
const route = useRoute()
const activeTab = ref('/')

const handleTabClick = (tab) => {
  router.push(tab)
}

watch(() => route.path, (newPath) => {
  activeTab.value = newPath
}, { immediate: true })
</script>

<template>
  <div class="bottom-nav">
    <el-tabs v-model="activeTab" @tab-click="(tab) => handleTabClick(tab.props.name)" class="bottom-tabs">
      <el-tab-pane label="首页" name="/">
        <template #label>
          <div class="tab-item">
            <el-icon><House /></el-icon>
            <span>首页</span>
          </div>
        </template>
      </el-tab-pane>
      <el-tab-pane label="食物搜索" name="/search">
        <template #label>
          <div class="tab-item">
            <el-icon><Search /></el-icon>
            <span>食物搜索</span>
          </div>
        </template>
      </el-tab-pane>
      <el-tab-pane label="关于小册" name="/about">
        <template #label>
          <div class="tab-item">
            <el-icon><InfoFilled /></el-icon>
            <span>关于小册</span>
          </div>
        </template>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<style scoped>
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #fff;
  box-shadow: 0 -2px 12px rgba(0, 0, 0, 0.08);
  z-index: 100;
  padding: 0;
}

.bottom-tabs {
  width: 100%;
}

.bottom-tabs :deep(.el-tabs__nav-wrap),
.bottom-tabs :deep(.el-tabs__nav-scroll) {
  padding-bottom: 0;
  margin-bottom: 0;
}

.bottom-tabs :deep(.el-tabs__nav) {
  width: 100%;
  display: flex;
  justify-content: space-around;
  margin-bottom: 0;
}

.bottom-tabs :deep(.el-tabs__item) {
  flex: 1;
  text-align: center;
  padding: 8px 0;
  height: auto;
  transition: all 0.3s ease;
}
.bottom-tabs :deep(.el-tabs__header) {
    margin: 0;
 }


.bottom-tabs :deep(.el-tabs__item.is-active) {
  color: var(--el-color-primary);
  transform: translateY(-2px);
}

.tab-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.tab-item .el-icon {
  font-size: 20px;
}

.tab-item span {
  font-size: 12px;
  line-height: 1.2;
}
</style>