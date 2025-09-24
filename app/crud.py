from sqlalchemy.orm import Session
from . import models, schemas

# -------------------- Student CRUD --------------------

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


# -------------------- Course CRUD --------------------

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session):
    return db.query(models.Course).all()

def get_course_by_id(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


# -------------------- Enrollment Logic --------------------

def enroll_student_in_course(db: Session, student_id: int, course_id: int):
    student = get_student_by_id(db, student_id)
    course = get_course_by_id(db, course_id)

    if not student or not course:
        return None  # You can raise HTTPException in the router

    # Avoid duplicate enrollment
    if course in student.courses:
        return student

    student.courses.append(course)
    db.commit()
    db.refresh(student)
    return student
