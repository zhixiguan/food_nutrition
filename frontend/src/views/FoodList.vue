<script setup>
import { ref, onMounted } from 'vue'
import { ElCard, ElRow, ElCol, ElMessage } from 'element-plus'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const foods = ref([])
const loading = ref(false)

const fetchFoods = async () => {
  loading.value = true
  try {
    const response = await fetch(`/api/foods?category_id=${route.params.id}`)
    if (!response.ok) throw new Error('获取食物数据失败')
    const data = await response.json()
    foods.value = data.map(food => ({
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
    console.error('获取食物数据错误:', error)
  } finally {
    loading.value = false
  }
}

const goToFoodDetail = (foodId) => {
  router.push(`/food/${foodId}`)
}

onMounted(() => {
  fetchFoods()
})
</script>

<template>
  <div class="food-list-page">
    <!--
    <div class="banner">
      <img src="../assets/banner.svg" alt="Banner" class="banner-image" />
      <h1 class="title">食物清单</h1>
    </div>
    -->
    <el-row :gutter="16">
      <el-col :xs="24" :sm="24" :md="24" :lg="24" v-for="food in foods" :key="food.id">
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
.food-list-page {
  padding: 8px;
  max-width: 480px;  /* 修改这行，设置为移动端的典型宽度 */
  overflow-x: hidden;
  margin-bottom: 50px;
  margin-top:50px;
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
}

.food-name {
  margin: 0 0 4px;
  font-size: clamp(16px, 4vw, 18px);
  color: #333;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width:200px
}

.category-name {
  color: #666;
  font-size: clamp(14px, 3.5vw, 16px);
  margin: 0 0 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nutrition-info {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.nutrition-item {
  display: flex;
  align-items: center;
  gap: 4px;
  background-color: #f5f7fa;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  color: #666;
}

.nutrition-icon {
  width: 16px;
  height: 16px;
}
</style>