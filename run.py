from app import app
from app.forms import StudentForm
from flask import render_template, flash

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = StudentForm()
    if form.validate_on_submit():
        #DB code here
        flash("Create Successful ...!!!")
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug = True)
