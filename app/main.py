from fastapi import FastAPI
from .routers import students, courses
from .database import Base, engine

# -------------------- Database Setup --------------------

Base.metadata.create_all(bind=engine)

# -------------------- FastAPI App --------------------

app = FastAPI(
    title="Student Course CRUD API",
    description="A beginner-friendly FastAPI application for managing students, courses, and enrollments.",
    version="1.0.0"
)

# -------------------- Root Route --------------------

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Course CRUD API. Visit /docs for interactive documentation."}

# -------------------- Routers --------------------

app.include_router(students.router)
app.include_router(courses.router)
