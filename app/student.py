from datetime import datetime
from flask import make_response, abort, render_template, request
import json

from app.forms import StudentForm
from app.models import Student, StudentSchema
from app import DAL

pass_response = {"res": "Operation Successfully"}
err_response = {"res": "Failed"}

def helper(std):
    if std:
        student_schema = StudentSchema(many=True)
        data = student_schema.dump(std).data
        return data
    else:
        return {}

def create(student):
    DAL.add(student)
    return json.dumps(pass_response)

def read_all():
    std = DAL.read_all()
    return helper(std)
    # return {"students": helper(std) }

def read_one(usn=None): 
    std = DAL.read_one(usn)
    return helper(std)

def update(usn, student):
    DAL.update(student=student)
    return json.dumps(pass_response)    

def delete(usn=None):
    DAL.delete(usn=usn)
    return json.dumps(pass_response)