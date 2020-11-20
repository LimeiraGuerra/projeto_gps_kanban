from sql_alchemy import banco

class Lawyer(banco.Model):

    __tablename__ = 'lawyer'

    oab = banco.Column(banco.String(80))
    task_id = banco.Column(banco.task_id)
    nome = banco.Column(banco.String(80))

    def __init__(self, oab, task_id, nome):
        self.oab = oab
        self.task_id = task_id
        self.nome = nome

    def json(self):
        return {
            'oab': self.oab,
            'task_id': self.task_id
            'nome': self.nome
        }

    