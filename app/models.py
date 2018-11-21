from app import db, app, ma


class Student(db.Model):
    __tablename__ = "person"
    usn = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(32))
    lname = db.Column(db.String(32))
    email = db.Column(db.String(128))
    gpa = db.Column(db.Float)
    phone_no = db.Column(db.Integer)


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
        sqla_session = db.session
