from fastapi import APIRouter, Depends, HTTPException, status 
from schemas import ProductRequest, ProductResponse, ProductUpdate
from database import get_db
from sqlalchemy.orm import Session
from models import Product
from typing import List

router = APIRouter()


@router.post("/products")
async def add_product(product: ProductRequest,
                    db: Session = Depends(get_db)) -> ProductRequest:
    existing_product = db.query(Product).filter(Product.name == product.name).first()
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product already exists"
        )
    new_product = Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return product


@router.get("/products", response_model=List[ProductResponse])
async def get_all_products(db: Session = Depends(get_db)):
    all_products = db.query(Product).all()
    if all_products is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products found"

        )
    return all_products


@router.get("/products/{product_id}", response_model=ProductResponse)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product does not exist")
    return product


# @router.put("/products/{product_id}")
# async def update_product(product_id: int, product_update: ProductUpdate,
#                           db: Session = Depends(get_db)) -> Dict[str, ProductUpdate]:
#     product_to_update = db.query(Product).filter(Product.id == product_id).first()
#     print(product_to_update)
#     if product_to_update is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Product does not exist")
#     # Update the product attributes
#     for field, value in product_update.model_dump().items():
#         setattr(product_to_update, field, value)

#     db.commit()
#     db.refresh(product_to_update)
#     return product_to_update

@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    # Retrieve the product from the database
    product_to_delete = db.query(Product).filter(Product.id == product_id).first()
    if product_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id=} not found"
        )

    # Delete the product from the database
    db.delete(product_to_delete)
    db.commit()

    return {"message": f"Product with id {product_id} deleted successfully"}
