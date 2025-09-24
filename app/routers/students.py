from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/students", tags=["Students"])

# -------------------- Dependency --------------------

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------- Create Student --------------------

@router.post("/", response_model=schemas.Student, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

# -------------------- Read All Students --------------------

@router.get("/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

# -------------------- Read Single Student --------------------

@router.get("/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# -------------------- Enroll Student in Course --------------------

@router.post("/{student_id}/enroll/{course_id}", response_model=schemas.Student)
def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = crud.enroll_student_in_course(db, student_id, course_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    return student
