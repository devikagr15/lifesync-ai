from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class Task(BaseModel):
    title: str
    due_date: str | None = None