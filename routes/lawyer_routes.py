from flask import Flask, request , Blueprint
import os
from model.lawyer import Lawyer

lawyer_blueprint = Blueprint('lawyer', __name__, url_prefix="/lawyer")


@lawyer_blueprint.route('/save', methods=['POST'])
def save_lawyer():
    try:
        print(request.json)
        Lawyer(request.json.get("id"), request.json.get("oab"), request.json.get("task_id"), request.json.get("nome")).save()
        return {
                'sucess': True,
                'erro': False,
                'msg': 'sucess'
            }
    except Exception as e:
        return {
                'sucess': False,
                'erro': True,
                'msg': str(e)
            }
        
@lawyer_blueprint.route('/delete', defaults={'id': None}, methods=['POST'])
@lawyer_blueprint.route('/delete/<id>', methods=['POST'])
def delete_lawyer(id):
    try:
        #Lawyer(request.json.get("id"), request.json.get("nome"), request.json.get("descricao"), request.json.get("status")).delete()
        lawyer = Lawyer.find_lawyer(Lawyer, request.json.get("id"))
        lawyer.delete()
        return {
                'sucess': True,
                'erro': False,
                'msg': 'sucess'
            }
    except Exception as e:
        return {
                'sucess': False,
                'erro': True,
                'msg': str(e)
            }

@lawyer_blueprint.route('/get', defaults={ 'id': None}, methods=['POST'])
@lawyer_blueprint.route('/get/<id>',  methods=['POST'])
def get_lawyer():
    try:
        lawyer = Lawyer.find_lawyer(Lawyer, request.json.get("id")).json()
        return {
                'sucess': True,
                'erro': False,
                'msg': lawyer
            }
    except Exception as e:
        return {
                'sucess': False,
                'erro': True,
                'msg': str(e)
            }

@lawyer_blueprint.route('/update', methods=['POST'])
def update_lawyer():
    try:
        lawyer = Lawyer.find_lawyer(Lawyer, request.json.get("id"))
        lawyer.update(request.json.get("nome"), request.json.get("oab"), request.json.get("task_id"))
        return {
                'sucess': True,
                'erro': False,
                'msg': lawyer.json()
            }
    except Exception as e:
        return {
                'sucess': False,
                'erro': True,
                'msg': str(e)
            }