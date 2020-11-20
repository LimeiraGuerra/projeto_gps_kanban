from sql_alchemy import banco

class Task(banco.Model):

    __tablename__ = 'task'

    task_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    descricao = banco.Column(banco.String(80))
    status = banco.Column(banco.String(80))

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

    