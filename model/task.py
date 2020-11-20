from sql_alchemy import bd
#from sql_alchemy.orm import relationship    
from model.lawyer import Lawyer

class Task(bd.Model):

    __tablename__ = 'task'

    task_id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(80))
    descricao = bd.Column(bd.String(80))
    status = bd.Column(bd.String(80))
    #lawyers = bd.relationship('Lawyer', backref='task')

    def __init__(self, task_id, nome, descricao, status):
        self.task_id = task_id
        self.nome = nome
        self.descricao = descricao
        self.status = status

    def json(self):
        return {
            'task_id': self.task_id,
            'nome': self.nome,
            'descricao': self.descricao,
            'status': self.status
        }

    @classmethod
    def find_task(self, task_id):
        task = cls.query.filter_by(task_id=task_id).first()
        if task: return task
        return None