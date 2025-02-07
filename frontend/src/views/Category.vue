<script setup>
import { ref, onMounted } from 'vue'
import { ElCard, ElRow, ElCol, ElMessage } from 'element-plus'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const categories = ref([])
const loading = ref(false)
const parentCategory = ref('')

const fetchParentCategory = async () => {
    try {
      const response = await fetch(`/api/categoryinfo?cate_id=${route.params.id}`)
      if (!response.ok) throw new Error('获取父级分类数据失败')
      const data = await response.json()
      if (data && data.length > 0) {
        parentCategory.value = data[0].title
      }
    } catch (error) {
      ElMessage.error(error.message)
      console.error('获取父级分类数据错误:', error)
    }
  }

const fetchCategories = async () => {
  loading.value = true
  try {
    const response = await fetch(`/api/categories?father_id=${route.params.id}`)
    if (!response.ok) throw new Error('获取分类数据失败')
    const data = await response.json()
    categories.value = data.map(category => ({
      id: category.id,
      name: category.title,
      cate_id: category.cate_id,
      father_id: category.father_id,
      icon: `/src/assets/f${category.father_id}.svg`
    }))
  } catch (error) {
    ElMessage.error(error.message)
    console.error('获取分类数据错误:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchCategories()
  fetchParentCategory()
})
</script>

<template>
  <div class="home">
    <!--
    <div class="banner">
      <img src="../assets/banner.svg" alt="Banner" class="banner-image" />
      <h1 class="title">{{ parentCategory }}</h1>
    </div>
    -->
    <el-row :gutter="16" justify="start">
      <el-col :xs="12" :sm="12" :md="12" :lg="12" v-for="category in categories" :key="category.id">
        <el-card class="category-card" shadow="hover" @click="router.push(`/foods/${category.cate_id}`)">
          <div class="category-content">
            <img :src="category.icon" class="category-icon" alt="分类图标" />
            <span class="category-name">{{ category.name }}</span>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>
.home {
  padding: 8px;
  max-width: 480px;
  margin: 50px auto;
  overflow-x: hidden;
}
.el-row {
  width: 100%;
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
  margin-bottom: 24px;
  font-size: clamp(20px, 5vw, 32px);
}

.category-card {
  margin-bottom: 8px;
  cursor: pointer;
  transition: transform 0.3s;
  height: 140px;
}

.category-card:hover {
  transform: translateY(-5px);
}

.category-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 12px;
  width: 100%;
  box-sizing: border-box;
}

.category-icon {
  width: clamp(48px, 12vw, 64px);
  height: clamp(48px, 12vw, 64px);
  margin-bottom: 12px;
  flex-shrink: 0;
  display: block;
}

.category-name {
  font-size: clamp(12px, 3vw, 14px);
  color: #2c3e50;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  padding: 0 4px;
  display: block;
  margin: 0;
}
</style>