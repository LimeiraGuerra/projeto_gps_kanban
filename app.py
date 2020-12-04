from flask import Flask, render_template, request , Response, make_response
from model.task import Task
import os
#from routes.task_routes import task_blueprint
#from routes.lawyer_routes import lawyer_blueprint
from routes.simple_task_routes import simple_task_blueprint

dir_patch = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/projeto_gps_kanban'
app = Flask(__name__, template_folder=dir_patch + '/view', static_folder=dir_patch + '/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.register_blueprint(task_blueprint)
#app.register_blueprint(lawyer_blueprint)

app.register_blueprint(simple_task_blueprint)

@app.before_first_request
def create_database():
    bd.create_all()

@app.route('/', methods=['GET'])
def homepage():
    unfiltered = Task.query.all()
    tasks_a = []
    tasks_m = []
    tasks_f = []
    for task in unfiltered:
        if task.status == 'aberto':
            tasks_a.append(task)
        elif task.status == 'andamento':
            tasks_m.append(task)
        elif task.status == 'finalizado':
            tasks_f.append(task)
    return render_template("home.html", tasks_a=tasks_a, tasks_m=tasks_m, tasks_f=tasks_f)

if __name__ == '__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(port=8080, debug=True, use_reloader=True)