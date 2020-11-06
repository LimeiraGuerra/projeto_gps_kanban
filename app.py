from flask import Flask, render_template
import os

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

if __name__ == '__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(port=8080, debug=True, use_reloader=True)