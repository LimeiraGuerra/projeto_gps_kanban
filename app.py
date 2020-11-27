from flask import Flask, render_template, request, redirect
import os
from model.task import Task, Lawyer

dir_patch = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/projeto_gps_kanban'
app = Flask(__name__, template_folder=dir_patch + '/view', static_folder=dir_patch + '/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_database():
    bd.create_all()

@app.route('/', methods=['GET'])
def homepage():
    return render_template("home.html")

@app.route('/savetask', methods=['POST'])
def save_task():
    Task(request.json.get("id"), request.json.get("nome"), request.json.get("descricao"), request.json.get("status")).save()
    return "seila"

@app.route('/deletetask', methods=['POST'])
def delete_task():
    task = Task.find_task(Task, request.json.get("id"))
    task.delete()
    return "seila"

@app.route('/gettask', methods=['POST'])
def get_task():
    return Task.find_task(Task, request.json.get("id")).json()

@app.route('/updatetask', methods=['POST'])
def update_task():
    task = Task.find_task(Task, request.json.get("id"))
    task.update(request.json.get("nome"), request.json.get("descricao"), request.json.get("status"))
    return "seila"
    

if __name__ == '__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(port=8080, debug=True, use_reloader=True)