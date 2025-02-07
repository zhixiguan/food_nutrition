from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from typing import List
from pydantic import BaseModel
from food_api import router as food_router

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class Category(BaseModel):
    id: int
    title: str
    cate_id: int
    father_id: int

# 注册食物API路由
app.include_router(food_router)

@app.get("/api/categoryinfo", response_model=List[Category])
async def get_categoryinfo(cate_id: int = 0):
    try:
        conn = sqlite3.connect("food_nutrition.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, cate_id, father_id FROM j_food_categories WHERE cate_id = 0 and father_id = ?",
                       (cate_id,)
        )
        categoryinfo = cursor.fetchall()
        conn.close()

        return [
            Category(id=cat[0], title=cat[1], cate_id=cat[2], father_id=cat[3])
            for cat in categoryinfo
        ]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")

@app.get("/api/categories", response_model=List[Category])
async def get_categories(cate_id: int = 0, father_id: int = None):
    try:
        # 连接数据库
        conn = sqlite3.connect("food_nutrition.db")
        cursor = conn.cursor()
        
        # 查询分类数据
        if father_id is not None:
            cursor.execute(
                "SELECT id, title, cate_id,father_id FROM j_food_categories WHERE cate_id<>0 and father_id = ?",
                (father_id,)
            )
        else:
            cursor.execute(
                "SELECT id, title, cate_id,father_id FROM j_food_categories WHERE cate_id = ?",
                (cate_id,)
            )
        categories = cursor.fetchall()
        
        # 关闭数据库连接
        conn.close()
        
        # 转换为响应格式
        return [
            Category(id=cat[0], title=cat[1], cate_id=cat[2], father_id=cat[3])
            for cat in categories
        ]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")