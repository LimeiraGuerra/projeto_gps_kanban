from sql_alchemy import bd
from sqlalchemy.orm import relationship    
from model.lawyer import Lawyer

class Task(bd.Model):

    __tablename__ = 'task'

    id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(80))
    descricao = bd.Column(bd.String(80))
    status = bd.Column(bd.String(80))
    lawyers = bd.relationship('Lawyer', backref='task')

    def __init__(self, id, nome, descricao, status):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.status = status

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'status': self.status
        }

    
    def update(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        self.status = status
    
    def save(self):
        bd.session.add(self)
        bd.session.commit()

    def delete(self):
        bd.session.remove(self)
        bd.session.commit()