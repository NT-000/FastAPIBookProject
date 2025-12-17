from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base


class Book(Base):
	__tablename__ = 'books'
	id = Column(Integer, autoincrement=True, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	title = Column(String)
	author = Column(String)
	description = Column(String)
	price = Column(Integer)
	category = Column(String)
	rating = Column(Float)
