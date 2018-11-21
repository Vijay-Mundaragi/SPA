from datetime import datetime
from flask import make_response, abort, render_template, request
import json

from app import db
from app.forms import StudentForm

Students = {
    "Mundaragi": {
    	"usn":1,
        "fname": "Vijay",
        "lname": "Mundaragi",
        "gpa":9,
        "email":"abc@gmail.com",
        "phone":9449494494
    },
    "Mundaragi_1": {
    	"usn":2,
        "fname": "Vijay",
        "lname": "Mundaragi",
        "gpa":9,
        "email":"abc@gmail.com",
        "phone":9449494494
    }
}

response = {"res": "Successfully created"}

def create(student):
    print(request.form)
    print(student)
    print(student["lname"])
    print(student["fname"])
    
    # if True:
    #     sdt = Student(fname=student.fname, lanme=student.fname, gpa=student.gpa, email=student.email, phone_no=student.phone)
    #     db.session.add(std)
    #     db.session.commit()
    # return json.loads(response)

    return response

def read_all():

    # return render_template("get_response.html", data=Students)
    return [Students[key] for key in Students.keys()]

def read_one(lname):
    pass

def update(lname, student):
    pass

def delete(lname):
    pass