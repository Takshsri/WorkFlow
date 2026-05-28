from pydantic import BaseModel
from typing import Optional
class UserCreate(BaseModel):
    username:str
    email:str
    role:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str

class UserUpdate(BaseModel):
    username :Optional[str] = None
    email : Optional[str] = None
    role : Optional[str] = None
    password : Optional[str] = None
    


