from fastapi import FastAPI, HTTPException, Depends
# from pydantic import BaseModel
from schemas.bases_schema import QuestionBase, ChoiceBase
from typing import List, Annotated
from models.bases import Base,Questions, Choices
from config.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/questions/")
async def create_questions(question: QuestionBase, db : db_dependency):
    db_question = Questions(question_text = question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = Choices(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choice)
    db.commit()

@app.get("/questions/{question_id}")
async def read_question(question_id : int, db : db_dependency):
    result = db.query(Questions).filter(Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Question is not found")
    return result

@app.get("/choices/{question_id}")
async def read_choices(question_id : int, db : db_dependency):
    result = db.query(Choices).filter(Choices.question_id == question_id).all()
    if not result:
        raise HTTPException(status_code=404, detail="Question is not found")
    return result

# @app.delete("/questions/{question_id}")
    


# from models.user_connection import UserConnection
# from schemas.user_schema import UserSchema

# app = FastAPI()
# conn = UserConnection()

# @app.get("/")
# async def index():
#     conn
#     return "Hola Fast API"

# @app.post("/api/insert")
# async def insert(user_data : UserSchema):
#     data = user_data.dict()
#     data.pop("id")
#     conn.write(data)