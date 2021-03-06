
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


# Assuming salaries.db is in your app root folder
e = create_engine('sqlite:///patients.db')  # loads db into memory

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)
cors = CORS(app)

class Patients(Resource):
	def get(self, patient_id):
            conn = e.connect()  # open connection to memory data
            print patient_id
            query = conn.execute("select PASSWORD from UserCredentials where ID = '%s'"%patient_id)  # query
            print query.cursor.fetchall()[0]
            #if len(query.cursor.fetchall()) == 0: #bad id
            #    return {'status':'user not found'}
        #    if query.cursor.fetchall()[0][0] != pwd_hash:
        #        return {'status':'wrong password'}
            #if query.cursor.fetchall()[0][0] == pwd_hash:
            info_query = conn.execute("select NAME, SEX, 'DATE OF BIRTH' from UserCredentials where ID = '%s'"%patient_id)
            status_query = conn.execute("select DATE, STATUS, STATE from UserDetails where ID = '%s' order by DATE "%patient_id)
            return {'patient info': info_query.cursor.fetchall()[0] , 'patient statuses': status_query.cursor.fetchall()}

	   def post(self):
	      conn = db_connect.connect()
	      print(request.json)
	      Name = request.json['Name']
	      BirthDate = request.json['BirthDate']
	      Sex = request.json['Sex']
	      patient_id = time.gmtime()
	      query = conn.execute("insert into UserCredentials values(null,'{0}','{1}','{2}','{3}')".format(patient_id, Name, BirthDate, Sex))
	      return {'status':'success','id':patient_id}


"""

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(LastName,FirstName,Title,
                             ReportsTo, BirthDate, HireDate, Address,
                             City, State, Country, PostalCode, Phone, Fax,
                             Email))
        return {'status':'success'}
"""

"""
class Status(Resource):
    def get(self, patient_id):  # param is pulled from url string
    	conn = e.connect()
    	query = conn.execute("select * from salaries where Department='%s'"%department_name.upper())
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
"""
class multiply(Resource):
    '''dummy function to test apis'''
    def get(self, number):  # param must match uri identifier
        return number * 2

# once we've defined our api functionalities, add them to the master API object
api.add_resource(Patients, '/patients/<string:patient_id>')

#api.add_resource(Departments_Meta, '/departments')  # bind url identifier to class
#api.add_resource(Departmental_Salary, '/dept/<string:department_name>')  # bind url identifier to class; also make it querable
api.add_resource(multiply, '/multiply/<int:number>')  # whatever the number is, multiply by 2

if __name__ == '__main__':
    app.run(debug=True)
