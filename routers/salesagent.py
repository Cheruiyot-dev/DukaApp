from fastapi import APIRouter,  Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import CreateSalesAgentRequest, CreateSalesAgentResponse, User
from database import get_db
from models import SalesAgent
from sqlalchemy import or_
from utility import pwd_context

router = APIRouter(
    prefix='/salesAgent',
    tags=['SalesAgent'] 
)


@router.post("/register_sales_agent", response_model=CreateSalesAgentResponse)
async def register_sales_agent(sales_agent: CreateSalesAgentRequest,
                            db: Session = Depends(get_db)) -> \
                                CreateSalesAgentResponse:
    existing_sales_agent = db.query(SalesAgent).filter(or_(SalesAgent.email == sales_agent.email, SalesAgent.username == sales_agent.username)).first()
    if existing_sales_agent:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )

    # Hash password before storing it

    hashed_password = pwd_context.hash(sales_agent.password)

    new_sales_agent = SalesAgent(
        username=sales_agent.username,
        email=sales_agent.email,
        password=hashed_password
    )
    db.add(new_sales_agent)
    db.commit()
    db.refresh(new_sales_agent)

    # Response
    response = CreateSalesAgentResponse(
        id=new_sales_agent.id,
        username=new_sales_agent.username,
        email=new_sales_agent.email)

    return response


@router.get("/{sales_agent_id}", status_code=status.HTTP_200_OK,
            response_model=User)
def get_SalesAgent(sales_agent_id: int, db: Session = Depends(get_db)):
    sales_agent = db.query(SalesAgent).filter(SalesAgent.id == sales_agent_id).first()

    if not sales_agent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{sales_agent_id} does not exist")

    return sales_agent
