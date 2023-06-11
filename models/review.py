#!/usr/bin/python3
from models.base_model import BaseModel as Base


class Review(Base):
    place_id = ""
    user_id = ''
    text = ""