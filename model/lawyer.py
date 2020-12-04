from sql_alchemy import bd
from sqlalchemy import UniqueConstraint

class Lawyer(bd.Model):

    __tablename__ = 'lawyer'

    lawyer_id = bd.Column(bd.Integer, primary_key=True)
    oab = bd.Column(bd.String(80), unique =True)
    taskid = bd.Column(bd.Integer, bd.ForeignKey('task.task_id'), nullable=False)
    nome = bd.Column(bd.String(80))

    def __init__(self, oab, taskid, nome):
        self.oab = oab
        self.taskid = taskid
        self.nome = nome

    def json(self):
        return {
            'lawyer_id': self.lawyer_id,
            'oab': self.oab,
            'taskid': self.taskid,
            'nome': self.nome
        }

    def find_lawyer(cls, lawyer_id):
        lawyer = cls.query.filter_by(lawyer_id=lawyer_id).first()
        if lawyer: return lawyer
        return None     

    def update(self, nome, oab, taskid):
        self.nome = nome
        self.oab = oab
        self.taskid = taskid
        bd.session.commit()

    def save(self):
        bd.session.add(self)
        bd.session.commit()

    def delete(self):
        bd.session.delete(self)
        bd.session.commit()