from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class BookRead(BaseModel):
	id: int
	user_id: int
	title : str
	author : str
	description : str
	price : int
	category : str
	rating : Optional[float] = None

	model_config = ConfigDict(from_attributes=True) # pydantic v1 - class Config: orm_mode = True

class BookCreate(BaseModel):
	title : str = Field(min_length=3, max_length=100)
	author : str = Field(min_length=10, max_length=100)
	description : str = Field(min_length=20, max_length=300)
	price : int = Field(ge=1, le=1000)
	category : str = Field(min_length=2, max_length=100)

	model_config = {
		"json_schema_extra": {
			"example": {
				"title": "Thieves of the Feygate",
				"author": "Nina Calder",
				"description": "This is a placeholder description.",
				"price": 459,
				"category": "fantasy",
			}
		}
	}


class BookUpdate(BaseModel):
	title : Optional[str] = None
	author : Optional[str] = None
	description : Optional[str] = None
	price : Optional[int] = None
	category : Optional[str] = None
	rating : Optional[float] = None

	model_config = {
		"json_schema_extra": {
			"example": {
					"title": "Update",
					"category": "crime",
					"description": "A late-night code review uncovers a pattern of crimes hidden inside a popular app's telemetry logs.",
					"price": 222,
					"rating": 4.1
			}
		}
	}