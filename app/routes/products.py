from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductResponse
from typing import List

router = APIRouter()

@router.get("/products", response_model = List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    products_list = db.query(Product).all()
    return products_list