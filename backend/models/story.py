# flow 
# story name -> theme -> first option -> children [go left, go right] --> text + options
# sqlalchemy is an ORM 

from sqlalchemy  import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON 

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.db.database import Base

class Story(Base):
    #define fields to have in story
    __tablename__ = "stories"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    session_id = Column(String,index=True)
    created_at= Column(DateTime(timezone=True),server_default=func.now())
    #one to many relationship with story nodes
    nodes=relationship("StoryNode",back_populates="story")

class StoryNode(Base):
    __tablename__ = "story_nodes"

    id= Column(Integer,primary_key=True,index=True)
    story_id= Column(Integer,ForeignKey("stories.id"),index=True)
    content = Column(String)
    is_root = Column(Boolean,default=False)
    is_ending = Column(Boolean,default=False)
    is_winning_ending= Column(Boolean,default=False)
    options = Column(JSON,default=list) #list of options for next nodes

    story=relationship("Story",back_populates="nodes")