from typing import List, Optional, Dict 
from datetime import BaseModel
from pydantic import BaseModel 

class storyOptionsSchema(BaseModel):
    text:str
    node_id:Optional[int] = None

class storyNodeBase(BaseModel):
    content:str
    is_ending:bool=False
    is_winning_ending:bool=False

class CompleteStoryNodeResponse(storyNodeBase):
    id:int
    options:List[storyOptionsSchema]=[]

    class Config:
        from_attributes = True

class StoryBase(BaseModel):
    title:str
    session_id:str

class CreateStoryRequest(BaseModel):
    theme:str


class CompleteStoryResponse(StoryBase):
    id:int
    created_at:datetime
    root_node:CompleteStoryNodeResponse
    all_nodes: Dict[int,CompleteStoryNodeResponse]
    
    class Config:
        from_attributes = True 