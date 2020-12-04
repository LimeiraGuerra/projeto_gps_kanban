from sql_alchemy import bd
#from sqlalchemy import UniqueConstraint

class Lawyer(bd.Model):

    __tablename__ = 'lawyer'

    lawyer_id = bd.Column(bd.Integer, primary_key=True)
    oab = bd.Column(bd.String(80))
    taskid = bd.Column(bd.Integer, bd.ForeignKey('task.task_id'), nullable=False)
    name = bd.Column(bd.String(80))

    def __init__(self, oab, name):
        self.oab = oab
        self.name = name

    def json(self):
        return {
            'lawyer_id': self.lawyer_id,
            'oab': self.oab,
            'taskid': self.taskid,
            'name': self.name
        }

    def find_lawyer(cls, lawyer_id):
        lawyer = cls.query.filter_by(lawyer_id=lawyer_id).first()
        if lawyer: return lawyer
        return None     

    #def update(self, name, oab, taskid):
    #    self.name = name
    #    self.oab = oab
    #    self.taskid = taskid
    #    bd.session.commit()

    def save(self):
        bd.session.add(self)
        bd.session.commit()

    def delete(self):
        bd.session.delete(self)
        bd.session.commit()