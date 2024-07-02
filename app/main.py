from fastapi import FastAPI, APIRouter, HTTPException
from database.models import Product
from database.schemas import all_products, individual_product
from config import db_product_table
from utils import generate_description
from bson.objectid import ObjectId

app = FastAPI()
todo_router = APIRouter()
# app.include_router(todo_router, prefix="/api/v1/todos")

# The endpoint to get all products description


@app.get("/products")
async def get_all_products_description():
    return all_products(db_product_table.find())

# endpoint to get a single product description


@app.get("/products/{product_id}")
async def get_single_product_description(product_id: str):
    id = ObjectId(product_id)
    existing_product_description = db_product_table.find_one(
        {"_id": id})
    if not existing_product_description:
        return HTTPException(status_code=404, detail=f"Product does not exist")
    return individual_product(existing_product_description)


# an endpoint to generate the product description and store in the db
@app.post("/products")
async def generate_product_description(product: Product):
    description = generate_description(
        f"Product Name: {product.name}, Specs : {product.specs}")
    new_product = {"name": product.name, "description": description}
    try:
        res = db_product_table.insert_one(dict(new_product))
        return {"status_code": 200, "id": str(res.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error : {e}")
