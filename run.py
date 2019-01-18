from app import app
from app.forms import StudentForm
from flask import render_template, flash, request
from app import DAL


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = StudentForm()
    if form.validate_on_submit():
        flash("Create Successful ...!!!")
    return render_template("index.html", form=form)


@app.route("/student_list", methods=["POST"])
def student_list():
    return render_template("get_response.html", data=request.get_json())


@app.route("/update", methods=["POST"])
def update_page():
    result = DAL.read_one(usn=request.get_json()["id"])    
    if result:
        form = StudentForm()
        form.usn.data = result.usn
        form.fname.data = result.fname
        form.lname.data = result.lname
        form.email.data = result.email
        form.gpa.data = result.gpa
        form.phone.data = result.phone_no
        return render_template("update.html", form=form)
    return "Error", 404        


@app.route("/delete", methods=["POST"])
def delete_page():
    result = DAL.read_one(usn=request.get_json()["id"])    
    if result:
        form = StudentForm()
        form.usn.data = result.usn
        return render_template("delete.html", form=form)
    return "Error", 404        


@app.route("/student/display")
def get_students():
    return render_template("get_response.html")


if __name__ == '__main__':
    app.run(debug = True)
