from fastapi import APIRouter, HTTPException
import sqlite3
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Food(BaseModel):
    id: int
    name: str
    category_name: str
    category_id: int
    father_id: int
    father_category_name: str
    alias_name: str | None
    english_name: str | None
    edible_part: str | None
    water: str | None
    energy: str | None
    protein: str | None
    fat: str | None
    cholesterol: str | None
    ash: str | None
    carbohydrate: str | None
    dietary_fiber: str | None
    carotene: str | None
    vitamin_a: str | None
    vitamin_e: str | None
    thiamin: str | None
    riboflavin: str | None
    niacin: str | None
    vitamin_c: str | None
    calcium: str | None
    phosphorus: str | None
    potassium: str | None
    sodium: str | None
    magnesium: str | None
    iron: str | None
    zinc: str | None
    selenium: str | None
    copper: str | None
    manganese: str | None
    iodine: str | None
    sfa: str | None
    mufa: str | None
    pufa: str | None
    fatty_acids_total: str | None


@router.get("/api/foods", response_model=List[Food])
async def get_foods(category_id: int):
    try:
        conn = sqlite3.connect("food_nutrition.db")
        cursor = conn.cursor()
        
        # 查询食物数据并关联分类表获取分类名称
        cursor.execute("""
            SELECT f.id, f.food_name as name, c.title as category_name, f.cate_id, c.father_id, d.title as father_category_name,
                f.alias_name, f.english_name, f.edible_part, f.water, f.energy, f.protein, f.fat, f.cholesterol, f.ash,
                f.carbohydrate, f.dietary_fiber, f.carotene, f.vitamin_a, f.vitamin_e, f.thiamin, f.riboflavin, f.niacin,
                f.vitamin_c, f.calcium, f.phosphorus, f.potassium, f.sodium, f.magnesium, f.iron, f.zinc, f.selenium,
                f.copper, f.manganese, f.iodine, f.sfa, f.mufa, f.pufa, f.fatty_acids_total
            FROM j_food_nutrition f
            LEFT JOIN j_food_categories c ON f.cate_id = c.cate_id
            LEFT JOIN j_food_categories d ON d.father_id = c.father_id and d.cate_id=0
            WHERE f.cate_id = ?
        """, (category_id,))
        
        foods = cursor.fetchall()
        conn.close()
        
        return [
            Food(
                id=food[0],
                name=food[1],
                category_name=food[2],
                category_id=food[3],
                father_id=food[4],
                father_category_name=food[5],
                alias_name=food[6],
                english_name=food[7],
                edible_part=food[8],
                water=food[9],
                energy=food[10],
                protein=food[11],
                fat=food[12],
                cholesterol=food[13],
                ash=food[14],
                carbohydrate=food[15],
                dietary_fiber=food[16],
                carotene=food[17],
                vitamin_a=food[18],
                vitamin_e=food[19],
                thiamin=food[20],
                riboflavin=food[21],
                niacin=food[22],
                vitamin_c=food[23],
                calcium=food[24],
                phosphorus=food[25],
                potassium=food[26],
                sodium=food[27],
                magnesium=food[28],
                iron=food[29],
                zinc=food[30],
                selenium=food[31],
                copper=food[32],
                manganese=food[33],
                iodine=food[34],
                sfa=food[35],
                mufa=food[36],
                pufa=food[37],
                fatty_acids_total=food[38]
                )
            for food in foods
        ]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")

@router.get("/api/food", response_model=Food)
async def get_food(id: int):
    try:
        conn = sqlite3.connect("food_nutrition.db")
        cursor = conn.cursor()
        
        # 查询食物数据并关联分类表获取分类名称
        cursor.execute("""
            SELECT f.id, f.food_name as name, c.title as category_name, f.cate_id, c.father_id, d.title as father_category_name,
                f.alias_name, f.english_name, f.edible_part, f.water, f.energy, f.protein, f.fat, f.cholesterol, f.ash,
                f.carbohydrate, f.dietary_fiber, f.carotene, f.vitamin_a, f.vitamin_e, f.thiamin, f.riboflavin, f.niacin,
                f.vitamin_c, f.calcium, f.phosphorus, f.potassium, f.sodium, f.magnesium, f.iron, f.zinc, f.selenium,
                f.copper, f.manganese, f.iodine, f.sfa, f.mufa, f.pufa, f.fatty_acids_total
            FROM j_food_nutrition f
            LEFT JOIN j_food_categories c ON f.cate_id = c.cate_id
            LEFT JOIN j_food_categories d ON d.father_id = c.father_id and d.cate_id=0
            WHERE f.id = ?
        """, (id,))
        
        food = cursor.fetchone()
        conn.close()

        if food is None:
            raise HTTPException(status_code=404, detail="未找到该食物")
        
        return Food(
            id=food[0],
            name=food[1],
            category_name=food[2],
            category_id=food[3],
            father_id=food[4],
            father_category_name=food[5],
            alias_name=food[6],
            english_name=food[7],
            edible_part=food[8],
            water=food[9],
            energy=food[10],
            protein=food[11],
            fat=food[12],
            cholesterol=food[13],
            ash=food[14],
            carbohydrate=food[15],
            dietary_fiber=food[16],
            carotene=food[17],
            vitamin_a=food[18],
            vitamin_e=food[19],
            thiamin=food[20],
            riboflavin=food[21],
            niacin=food[22],
            vitamin_c=food[23],
            calcium=food[24],
            phosphorus=food[25],
            potassium=food[26],
            sodium=food[27],
            magnesium=food[28],
            iron=food[29],
            zinc=food[30],
            selenium=food[31],
            copper=food[32],
            manganese=food[33],
            iodine=food[34],
            sfa=food[35],
            mufa=food[36],
            pufa=food[37],
            fatty_acids_total=food[38]
            )
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")

@router.get("/api/search", response_model=List[Food])
async def get_foods(keyword: str):
    try:
        conn = sqlite3.connect("food_nutrition.db")
        cursor = conn.cursor()
        
        # 查询食物数据并关联分类表获取分类名称
        cursor.execute("""
            SELECT f.id, f.food_name as name, c.title as category_name, f.cate_id, c.father_id, d.title as father_category_name,
                f.alias_name, f.english_name, f.edible_part, f.water, f.energy, f.protein, f.fat, f.cholesterol, f.ash,
                f.carbohydrate, f.dietary_fiber, f.carotene, f.vitamin_a, f.vitamin_e, f.thiamin, f.riboflavin, f.niacin,
                f.vitamin_c, f.calcium, f.phosphorus, f.potassium, f.sodium, f.magnesium, f.iron, f.zinc, f.selenium,
                f.copper, f.manganese, f.iodine, f.sfa, f.mufa, f.pufa, f.fatty_acids_total
            FROM j_food_nutrition f
            LEFT JOIN j_food_categories c ON f.cate_id = c.cate_id
            LEFT JOIN j_food_categories d ON d.father_id = c.father_id and d.cate_id=0
            WHERE f.food_name like ?
        """, (f'%{keyword}%',))
        
        foods = cursor.fetchall()
        conn.close()
        
        return [
            Food(
                id=food[0],
                name=food[1],
                category_name=food[2],
                category_id=food[3],
                father_id=food[4],
                father_category_name=food[5],
                alias_name=food[6],
                english_name=food[7],
                edible_part=food[8],
                water=food[9],
                energy=food[10],
                protein=food[11],
                fat=food[12],
                cholesterol=food[13],
                ash=food[14],
                carbohydrate=food[15],
                dietary_fiber=food[16],
                carotene=food[17],
                vitamin_a=food[18],
                vitamin_e=food[19],
                thiamin=food[20],
                riboflavin=food[21],
                niacin=food[22],
                vitamin_c=food[23],
                calcium=food[24],
                phosphorus=food[25],
                potassium=food[26],
                sodium=food[27],
                magnesium=food[28],
                iron=food[29],
                zinc=food[30],
                selenium=food[31],
                copper=food[32],
                manganese=food[33],
                iodine=food[34],
                sfa=food[35],
                mufa=food[36],
                pufa=food[37],
                fatty_acids_total=food[38]
                )
            for food in foods
        ]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")