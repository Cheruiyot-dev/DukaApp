from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, \
        Float, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Connecting to the database
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class SalesAgent(Base):
    __tablename__ = "salesagents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
 
    sales = relationship('Sale', back_populates='sales_agent')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    # sale_id = Column(Integer, ForeignKey('sales.id'), nullable=False)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)


    # Define the relationship with Product
    sales = relationship("Sale", back_populates="product")


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    pid = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity_bought = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    sales_agent_id = Column(Integer, ForeignKey('salesagents.id'), nullable=False)
    buyer_first_name = Column(String(100), nullable=False)
    buyer_last_name = Column(String(100), nullable=False)
    seller = Column(String(100), nullable=False)
    total_price = Column(Float, nullable=False)

    sales_agent = relationship('SalesAgent', back_populates='sales')
    product = relationship("Product", back_populates="sales")


# Create all tables
Base.metadata.create_all(engine)