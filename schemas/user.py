from pydantic import BaseModel, ConfigDict, Field, EmailStr


class UserRead(BaseModel):
	id: int
	name: str
	email: str

	model_config = ConfigDict(from_attributes=True) # pydantic v1 - class Config: orm_mode = True

class UserCreate(BaseModel):
	name: str = Field(..., min_length=6, max_length=50)
	email: EmailStr = Field(..., max_length=150)
	password: str = Field(..., min_length=8, max_length=64) # ... - required

	model_config = {
		"json_schema_extra" : {
			"example" : {
				"name": "John Doe",
				"email": "john_doe@gmail.com",
				"password": "12345678"
			}
		}
	}