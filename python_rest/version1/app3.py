
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_cors import CORS, cross_origin
import time


# Assuming salaries.db is in your app root folder
e = create_engine('sqlite:///Random')  # loads db into memory

app = Flask(__name__)
cors=CORS(app)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)

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
            status_query = conn.execute("select DATE, TIMESTAMP, STATUS, STATE from UserDetails where ID = '%s' "%patient_id)

            #rank :
#            print [i[2] for i in status_query.cursor.fetchall()]
            status_query_copy = list(status_query.cursor.fetchall())
            cur_status = [i[2] for i in status_query_copy][2]
            rank_query = conn.execute("select count(*) from UserDetails where STATUS = (select STATUS from UserDetails where ID = '%s' and STATE = 'pending') and TIMESTAMP < (select TIMESTAMP from UserDetails where ID = '%s' and STATE = 'pending') "%(patient_id, patient_id))
            rank_query_copy = list(rank_query.cursor.fetchall())
            print rank_query_copy
            return {'patient info': info_query.cursor.fetchall()[0] , 'patient statuses':  status_query_copy, 'rank': rank_query_copy}

    def post(self, patient_id):
            conn = e.connect()
            print(request.json)
            Name = request.json['Name']
            BirthDate = request.json['BirthDate']
            Sex = request.json['Sex']
            patient_id = time.gmtime()
            query = conn.execute("insert into UserCredentials values(null,'{0}','{1}','{2}','{3}')".format(patient_id, Name, BirthDate, Sex))
            return {'status':'success','id':patient_id}



class Status(Resource):
    def get(self, patient_id):  # param is pulled from url string
    	conn = e.connect()
    	query = conn.execute("select * from salaries where Department='%s'"%department_name.upper())
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result


    def post(self, patient_id):
        conn = e.connect()
        print(request.json)
        status_id = time.gmtime
        patient_id = request.json['id']
        timestamp = time.gmtime
        Status = request.json['Status']
        State = 'pending'
        query = conn.execute("insert into UserCredentials values(null,'{0}','{1}','{2}','{3}','{4}')".format(status_id, patient_id, timestamp, Status, State))
        return {'status':'success'}

class multiply(Resource):
    '''dummy function to test apis'''
    def get(self, number):  # param must match uri identifier
        return number * 2

# once we've defined our api functionalities, add them to the master API object
api.add_resource(Patients, '/patients/<string:patient_id>')
api.add_resource(Status, '/patients/<string:patient_id>')

#api.add_resource(Departments_Meta, '/departments')  # bind url identifier to class
#api.add_resource(Departmental_Salary, '/dept/<string:department_name>')  # bind url identifier to class; also make it querable
api.add_resource(multiply, '/multiply/<int:number>')  # whatever the number is, multiply by 2

if __name__ == '__main__':
    app.run(debug=True)
