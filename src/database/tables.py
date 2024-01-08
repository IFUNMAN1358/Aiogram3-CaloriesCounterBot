from sqlalchemy import Column, Integer, VARCHAR, Float, ForeignKey, DateTime, func, BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Consumption(Base):
    __tablename__ = 'consumption'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    day = Column(DateTime, nullable=False, default=func.current_timestamp())
    meal_name = Column(VARCHAR(100), nullable=False)
    product_list = Column(Text, nullable=False)
    weight = Column(Integer, nullable=False)
    calories_result = Column(Integer, nullable=False)
    proteins_result = Column(Integer, nullable=False)
    fats_result = Column(Integer, nullable=False)
    carbohydrates_result = Column(Integer, nullable=False)


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, unique=True, nullable=False)


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    product_name = Column(VARCHAR(255), nullable=False)
    calories = Column(Float, nullable=False)
    proteins = Column(Float, nullable=False)
    fats = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)








