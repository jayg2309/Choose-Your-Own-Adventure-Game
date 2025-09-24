# flow 
# story name -> theme -> first option -> children [go left, go right] --> text + options
# sqlalchemy is an ORM 

from sqlalchemy  import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON 

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.db.database import Base

class Story(Base):
    #define fields to have in story
    __table__ == "stories"

    id = Column(Integer,primary_key=True,index=True)
