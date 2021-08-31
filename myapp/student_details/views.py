from flask import Blueprint,jsonify,request
import json
from myapp import db
from myapp.student_details.models import Student

mod=Blueprint('student_details',__name__,url_prefix='/student')

@mod.route('/create_user', methods=['POST'])
def create_user():
    request_data=request.get_json()
    student=Student(
        firstname=request_data['firstname'],
        lastname=request_data['lastname'],
        email=request_data['email']
      )
    db.session.add(student)
    db.session.commit()
    return 'Student has been created'

@mod.route('/',methods=['GET'])
def get_student():
    students=Student.query.all() #select * from student
    # print(students[1].firstname)
    # print(students[1].lastname)
    # print(students[1].email)
    response=[student.__repr__() for student in students]
    # response=[x.__repr__() for x in students]
    return jsonify(response)

@mod.route('/get_student/<student_id>',methods=['GET'])
def get_student_id(student_id):
    students=Student.query.get(int(student_id))
    response=students.__repr__()
    response.pop('email')
    """
    #Execute query using raw sql query
    result=db.engine.execute('Select * from student where id={}'.format(int(student_id))')
    for x in result:
      response={
        'firstname':x['firstname'],
        'lastname':x['lastname'],
        'email':x['email']
        }
        
    """
    return jsonify(response)


@mod.route('/get_student', methods=['GET'])
def get_student_by_firstname():
    firstname=request.args.get('firstname')
    student = Student.query.filter(Student.firstname==firstname).first()
    #below is the statement for and ,or conditions
    #student=Student.query.filter((Student.firstname==firstname)|(Student.email==email)).first()
    response = student.__repr__()
    return jsonify(response)

@mod.route('/update_student/<student_id>', methods=['PUT'])
def update_student(student_id):
    request_data=request.get_json()
    student = Student.query.get(int(student_id))
    student.email=request_data['email']
    db.session.commit()
    return 'Student has been updated'

@mod.route('/delete_student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(int(student_id))
    db.session.delete(student)
    db.session.commit()
    return 'Student has been deleted'





