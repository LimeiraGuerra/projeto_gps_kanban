from flask import Flask, render_template, request , Response, make_response
import os
from routes.task_routes import task_blueprint
from routes.lawyer_routes import lawyer_blueprint

dir_patch = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/projeto_gps_kanban'
app = Flask(__name__, template_folder=dir_patch + '/view', static_folder=dir_patch + '/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(task_blueprint )
app.register_blueprint(lawyer_blueprint)

@app.before_first_request
def create_database():
    bd.create_all()

@app.route('/', methods=['GET'])
def homepage():
    return render_template("home.html")

if __name__ == '__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(port=8080, debug=True, use_reloader=True)