from myapp import db


class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(50))
    lastname=db.Column(db.String(100))
    email=db.Column(db.String(120))


    def __repr__(self):
        return {
            'firstname':self.firstname,
            'lastname':self.lastname,
            'email':self.email

        }


