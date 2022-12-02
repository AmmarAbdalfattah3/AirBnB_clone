#!/usr/bin/python3
"""module for the Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class implemention"""
    place_id = ""
    user_id = ""
    text = ""
