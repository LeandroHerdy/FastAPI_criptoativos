from pydantic import BaseModel
from typing import List


class UserCreateInput(BaseModel):
    name: str


class UserFavoriteAddInput(BaseModel):
    user_id: int
    symbol: str


class StandardOutput(BaseModel):
    message: str


class AlternativeOutput(StandardOutput):
    detail: str


class ErrorOutput(BaseModel):
    detail: str        


class Favorite(BaseModel):
    id: int
    symbol: str
    user_id: int

    class Config:
        orm_mode = True
    

class UserListOutput(BaseModel):
    id: int
    name: str
    favorite: List[Favorite]

    class Config:
        orm_mode = True

class DaySummaryOutput(BaseModel):
    highest: float
    lowest: float
    symbol: str
           