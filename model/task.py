from sql_alchemy import bd
from sqlalchemy.orm import relationship    
from model.lawyer import Lawyer

class Task(bd.Model):

    __tablename__ = 'task'

    task_id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(80))
    descricao = bd.Column(bd.String(80))
    status = bd.Column(bd.String(80))
    lawyers = bd.relationship('Lawyer', backref='task', cascade="all, delete")

    def __init__(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        self.status = status

    def __str__(self):
        return str(self.task_id)

    def json(self):
        return {
            'task_id': self.task_id,
            'nome': self.nome,
            'descricao': self.descricao,
            'status': self.status,
            'lawyers': [lawyer.json() for lawyer in self.lawyers]
        }

    def find_task(cls, task_id):
        task = cls.query.filter_by(task_id=task_id).first()
        if task: return task
        return None

    def update(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        self.status = status
        bd.session.commit()

    def delete(self):
        bd.session.delete(self)
        bd.session.commit()
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()

    