from fastapi import APIRouter, Depends, HTTPException, status 
from schemas import MakeSaleRequest, SaleResponse, UpdateSaleRequest, UpdateSaleResponse
from models import Product, SalesAgent, Sale
from database import get_db
from sqlalchemy.orm import Session, joinedload
from oauth2 import get_current_user
from datetime import datetime
from typing import List, Dict

router = APIRouter(
    prefix="/sales",
    tags=['Sales']
)



"""
# sales routes

get_all_sales
get_sale_by_id
update_sale
delete_sale


"""


@router.post("/sale", response_model=SaleResponse)
async def make_sale(sale_request: MakeSaleRequest, db: Session = Depends(get_db),
                    current_user=Depends(get_current_user)
                    ) -> MakeSaleRequest:
    #  Fetch product by name
    product = db.query(Product).filter(Product.name == sale_request.product_name).first()
    # print(product)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Check if there is enough quantity
    if product.quantity < sale_request.quantity_bought:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough quantity available"
        )
    
    # Calculate the total price
    total_price = product.quantity * sale_request.quantity_bought

    new_sale = Sale(
        pid=product.id,
        quantity_bought=sale_request.quantity_bought,
        created_at=datetime.utcnow(),
        SalesAgent_id=current_user.id,
        buyer_first_name=sale_request.buyer_first_name,
        buyer_last_name=sale_request.buyer_last_name,
        seller=current_user.username,
        total_price=total_price

    )

    db.add(new_sale)
    # Update product quantity
    product.quantity -= sale_request.quantity_bought
    db.commit()
    db.refresh(new_sale)

    # the response

    sale_response = SaleResponse(
        sale_id=new_sale.id,
        pid=new_sale.pid,
        buyer_first_name=new_sale.buyer_first_name,
        buyer_last_name=new_sale.buyer_last_name,
        product_name=sale_request.product_name,
        seller_name=current_user.username,
        quantity_bought=new_sale.quantity_bought,
        created_at=new_sale.created_at,
        total_price=new_sale.total_price
    )

    return sale_response


@router.get("sale/{sale_id}", response_model=SaleResponse)
async def get_sale_by_id(sale_id: int, db: Session = Depends(get_db), 
                         current_user=Depends(get_current_user)):
    sale = db.query(Sale).options(joinedload(Sale.product)).filter(Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found"
        )
    
    # pname = sale.product.name
    # print(pname)


    sale_response = SaleResponse(
        sale_id=sale.id,
        pid=sale.pid,
        buyer_first_name=sale.buyer_first_name,
        buyer_last_name=sale.buyer_last_name,
        product_name=sale.product.name,
        seller_name=sale.seller,
        quantity_bought=sale.quantity_bought,
        created_at=sale.created_at,
        total_price=sale.total_price
    )
    return sale_response


@router.get("sales/", response_model=List[SaleResponse])
async def get_all_sales(db: Session = Depends(get_db), 
                         current_user=Depends(get_current_user)):
    sales = db.query(Sale).options(joinedload(Sale.product)).all()
    sales_responses = []
    for sale in sales:
        sale_response = SaleResponse(
                sale_id=sale.id,
                pid=sale.pid,
                buyer_first_name=sale.buyer_first_name,
                buyer_last_name=sale.buyer_last_name,
                product_name=sale.product.name,
                seller_name=sale.seller,
                quantity_bought=sale.quantity_bought,
                created_at=sale.created_at,
                total_price=sale.total_price
        )
        sales_responses.append(sale_response)

    return sales_responses


@router.put("sale/{sale_id}", response_model=SaleResponse)
async def update_sale(sale_id: int, update_request: UpdateSaleRequest, db: Session = Depends(get_db), 
                        current_user=Depends(get_current_user)):
    sale = db.query(Sale).options(joinedload(Sale.product)).filter(Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale not found"
        )
    
    if update_request.quantity_bought is not None:
        #  Ensure there is enough quantity available in the product
        if sale.product.quantity < update_request.quantity_bought:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Not enough quantity available"
            ) 
        
        # update product quantity bought
        sale.product.quantity += sale.quantity_bought - update_request.quantity_bought
        sale.quantity_bought = update_request.quantity_bought

    if update_request.buyer_first_name is not None:
        sale.buyer_first_name = update_request.buyer_first_name

    if update_request.buyer_last_name is not None:
        sale.buyer_last_name = update_request.buyer_last_name

    if update_request.seller is not None:
        sale.seller = update_request.seller

    if update_request.total_price is not None:
        product_price = sale.product.price
        sale.total_price = product_price * update_request.quantity_bought

    db.commit()
    db.refresh(sale)


    sale_response = SaleResponse(
        sale_id=sale.id,
        pid=sale.pid,
        buyer_first_name=sale.buyer_first_name,
        buyer_last_name=sale.buyer_last_name,
        product_name=sale.product.name,  # Access the product name
        seller_name=current_user.username,
        quantity_bought=sale.quantity_bought,
        created_at=sale.created_at,
        total_price=sale.total_price
    )
    
    return sale_response


@router.delete("/sale/{sale_id}")
async def delete_sale_by_id(sale_id: int, db: Session = Depends(get_db), 
                            current_user=Depends(get_current_user)):
    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    
    # Delete the sale
    db.delete(sale)
    db.commit()

    return {"message": f"Sale with id {sale_id} has been deleted"}