from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, database

router = APIRouter()

@router.post("/students/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db, student)

@router.get("/students/", response_model=list[schemas.StudentResponse])
def get_students(db: Session = Depends(database.get_db)):
    return crud.get_students(db)

@router.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(database.get_db)):
    student = crud.get_student_by_id(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
