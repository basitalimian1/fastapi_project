from  sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):

    # What to call the table name in postgres?
    __tablename__ = "posts"

    # the are the columns of the databse
    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable  = False)
    content = Column (String, nullable = False)
    published = Column(Boolean,server_default = "TRUE", nullable = False)
    create_at = Column(TIMESTAMP(timezone=True),
                       nullable = False, 
                       server_default = text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id",
                                          ondelete="CASCADE"), 
                                          nullable = False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String, nullable  = False, unique = True)
    password = Column(String, nullable  = False)
    create_at = Column(TIMESTAMP(timezone=True),
                       nullable = False, 
                       server_default = text('now()'))
    phone_numer = Column(String)
    
class Vote(Base):
    __tablename__ = "Votes"
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), primary_key = True)
    post_id =Column(Integer, ForeignKey("posts.id",ondelete="CASCADE"), primary_key = True)
    