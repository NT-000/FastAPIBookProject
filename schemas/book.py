from pydantic import BaseModel, ConfigDict

class BookRead(BaseModel):
	id: int
	user_id: int
	title : str
	author : str
	description : str
	price : int
	category : str
	rating : float

model_config = ConfigDict(from_attributes=True) # pydantic v1 - class Config: orm_mode = True

class BookCreate(BaseModel):
	title : str
	author : str
	description : str
	price : int
	category : str
	rating : float


class BookUpdate(BaseModel):
	title : str
	author : str
	description : str
	price : int
	category : str
	rating : float