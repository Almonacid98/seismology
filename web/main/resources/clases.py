from flask_restful import Resource
from flask import request
Verified_Seisms = {
    1: {'id' : '1' , 'datetime' : '25/08/2020' , 'magnitude' : '6.9'},
    2: {'id' : '2' , 'datetime' : '29/08/2020' , 'magnitude' : '8.1'}
}
Unverified_Seisms = {
    1: {'id' : '1' , 'datetime' : '15/08/2020' , 'magnitude' : '2.1'},
    2: {'id' : '2' , 'datetime' : '12/08/2020' , 'magnitude' : '3.5'},
    3: {'id' : '3' , 'datetime' : '28/08/2020' , 'magnitude' : '2.8'},
    4: {'id' : '4' , 'datetime' : '29/08/2020' , 'magnitude' : '1.5'}

}


class VerifiedSeisms(Resource):
    def get(self, id):
        if int(id) in Verified_Seisms:
            return Verified_Seisms[int(id)]
        return '', 404
class VerifiedSeisms1(Resource):
    def getreturn(self):
        return Verified_Seisms

class UnverifiedSeisms(Resource):
    def get(self, id):
        if int(id) in Unverified_Seisms:
            return Unverified_Seisms[int(id)]
        return '', 404
    def put(self, id):
        if int(id) in  Unverified_Seisms:
            USeisms = Unverified_Seisms[int(id)]
            data = request.get_json()
            USeisms.update(data)
            return USeisms, 201
        return '', 404
    def delete(self, id):
        if int(id) in Unverified_Seisms:
            del Unverified_Seisms[int(id)]
            return '', 204
        return '', 404
class Univerfiedseisms1(Resource):
    def getreturn(self):
        return Unverified_Seisms
