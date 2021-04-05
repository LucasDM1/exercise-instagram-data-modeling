import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class MyEnum(enum.Enum):
    VIDEO="mp4"
    IMAGE="jpg"

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250),nullable=False)
    firstname = Column(String(250),nullable=False)
    lastname = Column(String(250),nullable=False)
    email = Column(String(250),nullable=False)

    def serialize(self):
        return {
            "id": self.id
        }

class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

class Media(Base): 
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MyEnum)) 
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

class Like(Base):
    __tablename__='likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

class Follower(Base):
    __tablename__='followers'
    user_from_id=Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_to_id=Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship(User)

    def to_dict(self):#covertir row en un dictionary de python
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')