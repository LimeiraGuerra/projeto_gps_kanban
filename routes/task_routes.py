from flask import Flask, request , Blueprint
import os
from model.task import Task

task_blueprint = Blueprint('task', __name__, url_prefix="/task")


@task_blueprint.route('/save', methods=['POST'])
def save_task():
    try:
        Task(request.json.get("nome"), request.json.get("descricao"), request.json.get("status")).save()
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
        
@task_blueprint.route('/delete', defaults={'id': None}, methods=['POST'])
@task_blueprint.route('/delete/<id>', methods=['POST'])
def delete_task(id):
    try:
        #Task(request.json.get("id"), request.json.get("nome"), request.json.get("descricao"), request.json.get("status")).delete()
        #if (id): Task.find_task(Task, id).delete()
        #else: Task.find_task(Task, request.json.get("id")).delete()
        task = Task.find_task(Task, request.json.get("id"))
        print(task.lawyers)
        task.delete()
        return {
                'sucess': True,
                'erro': False,
                'msg': 'sucess'
            }
    except Exception as e:
        print(e)
        return {
                'sucess': False,
                'erro': True,
                'msg': str(e)
            }

@task_blueprint.route('/get', defaults={ 'id': None}, methods=['POST'])
@task_blueprint.route('/get/<id>',  methods=['POST'])
def get_task(id):
    try:
        if (id): task = Task.find_task(Task, id).json()
        else : task = Task.find_task(Task, request.json.get("id")).json()
        return {
                'sucess': True,
                'erro': False,
                'msg': task
            }
    except Exception as e:
        return {
                'sucess': False,
                'erro': True,
                'msg': str(e)
            }

@task_blueprint.route('/update', methods=['POST'])
def update_task():
    try:
        task = Task.find_task(Task, request.json.get("id"))
        task.update(request.json.get("nome"), request.json.get("descricao"), request.json.get("status"))
        return {
                'sucess': True,
                'erro': False,
                'msg': task.json()
            }
    except Exception as e:
        return {
                'sucess': False,
                'erro': True,
                'msg': str(e)
            }