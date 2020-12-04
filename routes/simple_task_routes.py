from flask import Flask, request, Blueprint, jsonify
import os
from model.task import Task
from model.lawyer import Lawyer

simple_task_blueprint = Blueprint('task', __name__, url_prefix="/task")


@simple_task_blueprint.route('/save', methods=['POST'])
def save_task():
    try:
        data = request.json
        task = Task(data["name"], data["desc"], 'aberto' )#request.json.get("status"))
        [task.lawyers.append(Lawyer(l["oab"], l["name"])) for l in data['lawyers']]
        task.save()
        return jsonify({
                'success': True,
                'error': False,
                'response': task.json()
            })
    except Exception as e:
        return jsonify({
                'success': False,
                'error': True,
                'response': str(e)
            })
        
@simple_task_blueprint.route('/delete', defaults={'id': None}, methods=['POST'])
@simple_task_blueprint.route('/delete/<id>', methods=['POST'])
def delete_task(id):
    try:
        #Task(request.json.get("id"), request.json.get("nome"), request.json.get("descricao"), request.json.get("status")).delete()
        if (id): Task.find_task(Task, id).delete()
        else: Task.find_task(Task, request.json.get("id")).delete()
        return jsonify({
                'success': True,
                'error': False,
                'response': 'success'
            })
    except Exception as e:
        print(e)
        return jsonify({
                'success': False,
                'error': True,
                'response': str(e)
            })

@simple_task_blueprint.route('/get', defaults={ 'id': None}, methods=['POST'])
@simple_task_blueprint.route('/get/<id>',  methods=['POST'])
def get_task(id):
    try:
        if (id): task = Task.find_task(Task, id).json()
        else : task = Task.find_task(Task, request.json.get("id")).json()
        return jsonify({
                'success': True,
                'error': False,
                'response': task
            })
    except Exception as e:
        return jsonify({
                'success': False,
                'error': True,
                'response': str(e)
            })

@simple_task_blueprint.route('/status', defaults={ 'id': None, 'type_status': None}, methods=['POST'])
@simple_task_blueprint.route('/status/<id>/<type_status>',  methods=['POST'])
def change_status(id, type_status):
    try:
        if (id): task = Task.find_task(Task, id)
        else : task = Task.find_task(Task, request.json.get("id"))
        if (type_status): 
            task.status = type_status
        else: 
            if request.json.get("status") is not None:
                task.status = request.json.get("status")
        task.update(task.name, task.desc, task.status)
        return jsonify({
                'success': True,
                'error': False,
                'response': task.json()
            })
    except Exception as e:
        return jsonify({
                'success': False,
                'error': True,
                'response': str(e)
            })

@simple_task_blueprint.route('/update', methods=['POST'])
def update_task():
    try:
        data = request.json
        task = Task.find_task(data.get("id"))
        task.update(data["name"], data["desc"], data['status'])
        return jsonify({
                'success': True,
                'error': False,
                'response': task.json()
            })
    except Exception as e:
        return jsonify({
                'success': False,
                'error': True,
                'response': str(e)
            })

@simple_task_blueprint.route('/getAll', methods=['POST'])
def getAll():
    tasks = Task.query.all()
    return jsonify({
                'success': True,
                'error': False,
                'response': [task.json() for task in tasks]
            })