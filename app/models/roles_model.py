from  app.models.base import BaseModel
from sqlalchemy.orm import  relationship
from sqlalchemy import Column,Integer,String,Boolean

class RoleModel(BaseModel):
    __tablename__='roles'
    
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(80))
    status=Column(Boolean ,default=True)

    users=relationship('UserModel',uselist=True,back_populates='role')



