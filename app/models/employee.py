from sqlalchemy import Column, Integer, String, Float, Date

from app.database.connection import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    position = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    department = Column(String, nullable=False)
    hire_date = Column(Date, nullable=False)
    phone = Column(String, nullable=True)