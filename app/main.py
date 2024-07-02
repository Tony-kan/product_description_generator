from fastapi import FastAPI, APIRouter, HTTPException
from database.models import Product
from database.schemas import all_products, individual_product
from config import db_product_table
from utils import generate_description

app = FastAPI()
todo_router = APIRouter()
# app.include_router(todo_router, prefix="/api/v1/todos")


@app.get("/products")
async def get_all_products_description():
    return all_products(db_product_table.find())


@app.post("/products")
async def generate_product_description(product: Product):
    description = generate_description(
        f"Product Name: {product.name}, Notes : {product.notes}")
    new_product = {"name": product.name, "description": description}
    try:
        res = db_product_table.insert_one(dict(new_product))
        return {"status_code": 200, "id": str(res.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error : {e}")
