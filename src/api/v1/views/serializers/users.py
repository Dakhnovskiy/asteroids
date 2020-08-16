from typing import List

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    login: str = Field(max_length=256)


class UserCreate(UserBase):
    password: str


class UserInfo(UserBase):
    id: int


class UserFavourites(BaseModel):
    asteroid_name: str


class UserFavouritesInfo(BaseModel):
    user_id: int
    favourites: List[str]


