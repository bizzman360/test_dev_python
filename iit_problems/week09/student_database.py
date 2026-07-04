from flask import Flask, request
import pandas as pd
from pydantic import BaseModel

class Student(BaseModel):
    student_id: int
    student_name: str
    course_enrolled: str

app = Flask(__name__)

@app.route("/")
def main():
    student_id = request.args.get("student_id")
    student_name = request.args.get("student_name")