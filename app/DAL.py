from app import db
from app.models import Student

def add(student):
    std = Student(fname=student["fname"], lname=student["lname"], gpa=student["gpa"], email=student["email"], phone_no=student["pno"])
    db.session.add(std)
    db.session.commit()

def read_all():
    return Student.query.order_by(Student.lname).all()

def read_one(usn=None):
    if usn:
        result = Student.query.filter_by(usn=usn).first()
        if result:
            return result

def update(student=None):
    if student:
        usn=student["usn"]
        std = Student.query.filter_by(usn=usn).first()
        if(std):
            std.fname = student["fname"]
            std.lname = student["lname"]
            std.gpa = student["gpa"]
            std.email = student["email"]
            std.phone_no=student["pno"]
            db.session.commit()

def delete(usn=None):
    if usn:
        std = Student.query.filter_by(usn=usn).first()
        if std:
            db.session.delete(std)
            db.session.commit()



