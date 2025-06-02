from typing import Optional
from bson import ObjectId

class User:
    def __init__(self, username: str, email: str, hashed_password: str, _id: Optional[ObjectId] = None):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.id = str(_id) if _id else None
