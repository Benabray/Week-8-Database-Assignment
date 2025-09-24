from pydantic import BaseModel
from typing import List, Optional

# -------------------- Course Schemas --------------------

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    credits: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode


# -------------------- Student Schemas --------------------

class StudentBase(BaseModel):
    name: str
    email: str
    age: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    courses: List[Course] = []

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode
