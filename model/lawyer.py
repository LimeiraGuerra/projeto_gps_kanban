from sql_alchemy import bd

class Lawyer(bd.Model):

    __tablename__ = 'lawyer'

    oab = bd.Column(bd.String(80), primary_key=True)
    task_id = bd.Column(bd.Integer, bd.ForeignKey('task.id'))
    nome = bd.Column(bd.String(80))

    def __init__(self, oab, task_id, nome):
        self.oab = oab
        self.task_id = task_id
        self.nome = nome

    def json(self):
        return {
            'oab': self.oab,
            'task_id': self.task_id,
            'nome': self.nome
        }

    def update(self, nome, task_id):
        self.nome = nome
        self.task_id = task_id

    def save(self):
            bd.session.add(self)
            bd.session.commit()

    def delete(self):
        bd.session.remove(self)
        bd.session.commit()