# test_db.py
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:%40%24Kinoti100%25@localhost:3306/student_course_db"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ Connected to MySQL successfully!")
except Exception as e:
        print("❌ Connection failed:", e)
