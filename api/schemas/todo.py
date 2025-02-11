from pydantic import BaseModel, Field
from typing import Literal, Optional
from tortoise.contrib.pydantic import pydantic_model_creator

GetTodo = pydantic_model_creator(None, name='Todo')

class PostTodo(BaseModel):
    task: str = Field(..., max_length=100)
    done: bool
    
class GetTodo(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    done: Optional[bool]