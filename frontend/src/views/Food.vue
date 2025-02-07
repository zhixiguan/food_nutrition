<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { ElCard, ElDivider, ElSkeleton, ElMessage } from 'element-plus'

const route = useRoute()
const food = ref(null)
const loading = ref(false)

const fetchFoodDetail = async () => {
  loading.value = true
  try {
    const response = await fetch(`/api/food?id=${route.params.id}`)
    if (!response.ok) throw new Error('获取食物详情失败')
    const data = await response.json()
    food.value = {
      ...data,
      icon: `/src/assets/f${data.father_id}.svg`
    }
  } catch (error) {
    ElMessage.error(error.message)
    console.error('获取食物详情错误:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchFoodDetail()
})
</script>

<template>
  <div class="food-detail-page">
    <el-skeleton :loading="loading" animated>
      <template #template>
        <div class="skeleton-content">
          <el-skeleton-item variant="image" style="width: 240px; height: 240px" />
          <el-skeleton-item variant="h1" style="width: 50%" />
          <el-skeleton-item variant="text" style="width: 80%" />
          <el-skeleton-item variant="text" style="width: 60%" />
        </div>
      </template>
      
      <template #default>
        <el-card v-if="food" class="food-detail-card">
          <div class="food-header">
            <img :src="food.icon" class="food-icon" alt="食物图标" />
            <div class="food-title">
              <h1>{{ food.name }}</h1>
              <p class="category">{{ food.father_category_name }}、{{ food.category_name }}</p>
            </div>
          </div>

          <el-divider>
            <span class="divider-title">基本营养成分</span><br/><span style="color:#666; font-size:12px;">(每100g)</span>
          </el-divider>

          <!-- 能量与相关成分 -->
          <div class="nutrition-grid">
            <div class="nutrition-item">
              <img src="../assets/energy-icon.svg" alt="能量" />
              <div class="nutrition-info">
                <span class="label">能量 / Energy</span>
                <span class="value">{{ food.energy }}</span>
              </div>
            </div>
            <div class="nutrition-item">
              <img src="../assets/protein-icon.svg" alt="蛋白质" />
              <div class="nutrition-info">
                <span class="label">蛋白质 / Protein</span>
                <span class="value">{{ food.protein }}</span>
              </div>
            </div>
            <div class="nutrition-item">
              <img src="../assets/fat-icon.svg" alt="脂肪" />
              <div class="nutrition-info">
                <span class="label">脂肪 / Fat</span>
                <span class="value">{{ food.fat }}</span>
              </div>
            </div>
            <div class="nutrition-item">
              <img src="../assets/carbs-icon.svg" alt="碳水化合物" />
              <div class="nutrition-info">
                <span class="label">碳水化合物 / CHO</span>
                <span class="value">{{ food.carbohydrate }}</span>
              </div>
            </div>
          </div>

          <el-divider>
            <span class="divider-title">维生素</span>
          </el-divider>
          <div class="detailed-nutrition">
            <div class="nutrition-row">
              <span class="label">维生素A / Vitamin A</span>
              <span class="value">{{ food.vitamin_a }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">维生素C / Vitamin C</span>
              <span class="value">{{ food.vitamin_c }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">维生素E / Vitamin E</span>
              <span class="value">{{ food.vitamin_e }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">硫胺素 / Thiamin</span>
              <span class="value">{{ food.thiamin }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">核黄素 / Riboflavin</span>
              <span class="value">{{ food.riboflavin }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">烟酸 / Niacin</span>
              <span class="value">{{ food.niacin }}</span>
            </div>
          </div>

          <el-divider>
            <span class="divider-title">矿物质</span>
          </el-divider>
          <div class="detailed-nutrition">
            <div class="nutrition-row">
              <span class="label">钙 / Calcium</span>
              <span class="value">{{ food.calcium }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">铁 / Iron</span>
              <span class="value">{{ food.iron }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">锌 / Zinc</span>
              <span class="value">{{ food.zinc }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">磷 / Phosphorus</span>
              <span class="value">{{ food.phosphorus }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">钾 / Potassium</span>
              <span class="value">{{ food.potassium }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">钠 / Sodium</span>
              <span class="value">{{ food.sodium }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">镁 / Magnesium</span>
              <span class="value">{{ food.magnesium }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">硒 / Selenium</span>
              <span class="value">{{ food.selenium }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">铜 / Copper</span>
              <span class="value">{{ food.copper }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">锰 / Manganese</span>
              <span class="value">{{ food.manganese }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">碘 / Iodine</span>
              <span class="value">{{ food.iodine }}</span>
            </div>
          </div>

          <el-divider>
            <span class="divider-title">脂肪酸</span>
          </el-divider>
          <div class="detailed-nutrition">
            <div class="nutrition-row">
              <span class="label">饱和脂肪酸 / SFA</span>
              <span class="value">{{ food.sfa }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">单不饱和脂肪酸 / MUFA</span>
              <span class="value">{{ food.mufa }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">多不饱和脂肪酸 / PUFA</span>
              <span class="value">{{ food.pufa }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">脂肪酸合计 / Total</span>
              <span class="value">{{ food.fatty_acids_total }}</span>
            </div>
          </div>

          <el-divider>
            <span class="divider-title">详细营养信息</span>
          </el-divider>

          <div class="detailed-nutrition">
            <div class="nutrition-row">
              <span class="label">膳食纤维 / Dietary Fiber</span>
              <span class="value">{{ food.fiber }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">胆固醇 / Cholesterol</span>
              <span class="value">{{ food.cholesterol }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">钙 / Calcium</span>
              <span class="value">{{ food.calcium }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">铁 / Iron</span>
              <span class="value">{{ food.iron }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">锌 / Zinc</span>
              <span class="value">{{ food.zinc }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">维生素A / Vitamin A</span>
              <span class="value">{{ food.vitamin_a }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">维生素B1 / Vitamin B1</span>
              <span class="value">{{ food.vitamin_b1 }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">维生素B2 / Vitamin B2</span>
              <span class="value">{{ food.vitamin_b2 }}</span>
            </div>
            <div class="nutrition-row">
              <span class="label">维生素C / Vitamin C</span>
              <span class="value">{{ food.vitamin_c }}</span>
            </div>
          </div>

          <el-divider>
            <span class="divider-title">备注说明</span>
          </el-divider>

          <div class="notes-section">
            <div class="notes-content">
              <div class="notes-item">"—"：表示未检测</div>
              <div class="notes-item">"Tr"：表示未检出</div>
              <div class="notes-item">"un"：仅对维生素E和能量在计算时，表示不能得出结果</div>
              <div class="notes-item">"0"：表示测定后修约的0值，计算后的0值，理论上估计的0值</div>
            </div>
          </div>
        </el-card>
      </template>
    </el-skeleton>
  </div>
</template>

<style scoped>
.food-detail-page {
  max-width: 480px;
  margin: 0 auto;
  padding: 0;
  box-sizing: border-box;
  margin-bottom: 60px;
  margin-top: 50px;
}

.skeleton-content {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
  padding: 0px;
  margin: 0 auto;
  max-width: 100%;
}

.food-detail-card {
  background-color: #fff;
  border-radius: 8px;
  padding: 0px;
  width: 100%;
  margin: 0 auto;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.container {
  max-width: 100%;
  padding: 0 8px;
  margin: 0 auto;
}

.food-info {
  padding: 16px;
  margin: 0 -12px;
  background-color: #fff;
}

.food-header {
  margin-bottom: 24px;
}

.food-title {
  font-size: clamp(24px, 6vw, 32px);
  margin: 0 0 8px;
  color: #2c3e50;
}
.food-title h1 {
    font-size: 1.2em;
}
.food-title p.category {
    font-size: 0.6em;
}

.food-category {
  color: #666;
  font-size: clamp(14px, 3.5vw, 16px);
}

.nutrition-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 12px;
  margin: 16px 0;
}

.nutrition-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.nutrition-item img {
  width: 32px;
  height: 32px;
}

.nutrition-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  gap: 8px;
}
.nutrition-info .label {
  text-align: left;
  flex: 1;
}
.nutrition-info .value {
  text-align: right;
  min-width: 60px;
}

.detailed-nutrition .nutrition-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  background-color: #f8f9fa;
  border-radius: 6px;
}

.detailed-nutrition .value {
  min-width: 80px;
  text-align: right;
}

.notes-section {
  margin-top: 24px;
  padding: 16px;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.notes-title {
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 12px;
}

.notes-content {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
}

.notes-item {
  margin-bottom: 8px;
}
.label {
  color: #666;
  font-size: 14px;
}

.value {
  font-weight: 500;
  color: #2c3e50;
}
</style>