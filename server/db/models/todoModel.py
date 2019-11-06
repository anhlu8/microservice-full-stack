from db.orm.SQLAlchemy import alchemist
import datetime

class TodoModel(alchemist.Model):  # This class is for SQLAlchemy alchemist
    __tablename__ = "todo"
    id = alchemist.Column(alchemist.Integer, primary_key=True)
    # date = alchemist.Column(alchemist.DateTime(timezone=True), nullable=False,
    #                         default=datetime.datetime.utcnow)
    # task = alchemist.Column(alchemist.String(
    #     20), nullable=False)
    # complete = alchemist.Column(alchemist.Boolean, nullable=False)
    first_name = alchemist.Column(alchemist.String(20), nullable=False)
    last_name = alchemist.Column(alchemist.String(20), nullable=False)
    def __repr__(self):
        return "('first_name': {})".format(self.first_name)