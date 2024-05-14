from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, \
        Float, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


# connecting to the database
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    disabled = Column(Boolean, default=False)

    # Relationship with orders
    orders = relationship('Order', backref='customer')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    # Relationship with order items
    order_items = relationship('OrderItem', backref='product')


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_number = Column(Integer, autoincrement=True)
    order_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Relationship with Customer

    order_items = relationship('OrderItem', backref='order')


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_quantity = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
