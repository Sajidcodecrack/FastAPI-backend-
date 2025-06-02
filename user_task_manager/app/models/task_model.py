from typing import Optional
from bson import ObjectId


class Task:
    def __init__(
        self,
        user_id: str,
        title: str,
        description: str,
        status: str,
        due_date: str,
        created_at: str,
        _id: Optional[ObjectId] = None,
    ):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.created_at = created_at
        self.id = str(_id) if _id else None
