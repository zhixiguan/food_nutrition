<script setup>
import { ref } from 'vue'
import { ElInput, ElCard, ElRow, ElCol, ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

const router = useRouter()
const searchQuery = ref('')
const searchResults = ref([])
const loading = ref(false)

const handleSearch = async () => {
  if (!searchQuery.value.trim()) return
  loading.value = true
  try {
    const response = await fetch(`/api/search?keyword=${encodeURIComponent(searchQuery.value)}`)
    if (!response.ok) throw new Error('搜索失败')
    const data = await response.json()
    searchResults.value = data.map(food => ({
      id: food.id,
      name: food.name,
      category_name: food.category_name,
      father_category_name: food.father_category_name,
      icon: `/src/assets/f${food.father_id}.svg`,
      energy: food.energy,
      protein: food.protein,
      fat: food.fat
    }))
  } catch (error) {
    ElMessage.error(error.message)
    console.error('搜索错误:', error)
  } finally {
    loading.value = false
  }
}

const goToFoodDetail = (foodId) => {
  router.push(`/food/${foodId}`)
}
</script>

<template>
  <div class="search-page">
    <!--
    <div class="banner">
      <img src="../assets/banner.svg" alt="Banner" class="banner-image" />
      <h1 class="title">搜索食物</h1>
    </div>
    -->
    <div class="search-box">
      <el-input
        v-model="searchQuery"
        placeholder="食物名称关键词"
        clearable
        size="large"
        @keyup.enter="handleSearch"
      >
        <template #append>
          <el-button @click="handleSearch" :loading="loading">搜索</el-button>
        </template>
      </el-input>
    </div>

    <el-row :gutter="16" v-if="searchResults.length > 0">
      <el-col :xs="24" :sm="24" :md="24" :lg="24" v-for="food in searchResults" :key="food.id">
        <el-card class="food-card" shadow="hover" @click="goToFoodDetail(food.id)">
          <div class="food-content">
            <div style="display: flex; flex-direction: column; align-items: center;">
              <img :src="food.icon" class="food-icon" alt="食物图标" />
              <div class="unit-text">每100克</div>
            </div>
            <div class="text-content">
              <h3 class="food-name">{{ food.name }}</h3>
              <p class="category-name">{{ food.father_category_name }}、{{ food.category_name }}</p>
              <div class="nutrition-info">
                <div class="nutrition-item">
                  <img src="../assets/energy-icon.svg" alt="能量" class="nutrition-icon" />
                  <span>{{ food.energy }}</span>
                </div>
                <div class="nutrition-item">
                  <img src="../assets/protein-icon.svg" alt="蛋白质" class="nutrition-icon" />
                  <span>{{ food.protein }}</span>
                </div>
                <div class="nutrition-item">
                  <img src="../assets/fat-icon.svg" alt="脂肪" class="nutrition-icon" />
                  <span>{{ food.fat }}</span>
                </div>
              </div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>
.search-page {
  padding: 8px;
  max-width: 480px;
  overflow-x: hidden;
  margin-bottom: 50px;
}

.banner {
  position: relative;
  margin: -8px -8px 16px -8px;
}

.banner-image {
  width: 100%;
  height: auto;
  display: block;
}

.title {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  margin: 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  color: #2c3e50;
  font-size: clamp(20px, 5vw, 32px);
}

.search-box {
  margin: 24px auto;
  max-width: 800px;
  padding: 0 20px;
}

.food-card {
  margin-bottom: 12px;
  cursor: pointer;
  transition: transform 0.3s;
}

.food-card:hover {
  transform: translateY(-5px);
}

.food-content {
  display: flex;
  align-items: flex-start;
  text-align: left;
  padding: 12px;
}

.food-icon {
  width: clamp(48px, 12vw, 64px);
  height: clamp(48px, 12vw, 64px);
  margin-right: 16px;
  flex-shrink: 0;
}

.unit-text {
  font-size: 12px;
  color: #666;
  text-align: center;
  margin: 4px 16px 0 0;
  flex-shrink: 0;
  width: clamp(48px, 12vw, 64px);
}

.text-content {
  flex-grow: 1;
  min-width: 0;
  max-width: 198px;
}

.food-name {
  margin: 0 0 4px;
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.category-name {
  margin: 0 0 8px;
  font-size: 12px;
  color: #666;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.nutrition-info {
  display: flex;
  gap: 16px;
}

.nutrition-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #666;
}

.nutrition-icon {
  width: 16px;
  height: 16px;
}

:deep(.el-input) {
  --el-input-height: 56px;
  font-size: 18px;
}

:deep(.el-input__wrapper) {
  border-radius: 24px 0 0 24px;
}

:deep(.el-input-group__append) {
  border-radius: 0 24px 24px 0;
  padding: 0 32px;
  font-size: 18px;
}
</style>