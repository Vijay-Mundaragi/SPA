from app import db
from app.models import Student

import os

if not(os.path.exists('app.db')):
	db.create_all()
	db.session.commit()

	s = Student(fname="vijay", lname="M", email="saivijay010@gmail.com", gpa=9, phone_no=9449494494)
	print(s)

	db.session.add(s)
	db.session.commit()
