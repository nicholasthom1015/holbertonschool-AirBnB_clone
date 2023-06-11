#!/usr/bin/python3
from models.base_model import BaseModel as Base


class User(Base):
    email = ""
    password = ""
    first_name = ""
    last_name = ""