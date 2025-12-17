from pydantic import BaseModel, ConfigDict


class UserRead(BaseModel):
	id: int
	name: str
	email: str

	model_config = ConfigDict(from_attributes=True) # pydantic v1 - class Config: orm_mode = True