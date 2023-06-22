from pydantic import BaseModel

class UserSchema(BaseModel):
    id : int | None
    name : str 
    phone : str