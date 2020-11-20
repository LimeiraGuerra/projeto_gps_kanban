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

@app.route('/salvatask', methods=['POST'])
def salvatask():
    #task = Task(request.json.get("id"), request.json.get("nome"), request.json.get("descricao"), request.json.get("status"))
    #task.save()
    #lawyer = Lawyer(0,0,"0")
    #lawyer.save()
    #lawyer1 = Lawyer(1,0,"1").save()
    #print(task.lawyers)
    return request.json

if __name__ == '__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(port=8080, debug=True, use_reloader=True)