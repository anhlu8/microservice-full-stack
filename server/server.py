# imports from libraries
from flask import Flask, request
from flask_cors import CORS
import os
# imports from project
from db.orm.SQLAlchemy import get_postgres_url
from db.orm.SQLAlchemy import alchemist
from db.models.todoModel import TodoModel
from db.serializer.marshaller import OneTodoSchema, ManyTodoSchema

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = get_postgres_url() #Run this on local
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{pw}@{host}/{db}".format(user=os.environ['DBUSER'], pw=os.environ['POSTGRES_PASSWORD'], host=os.environ['DBHOST'], db=os.environ['POSTGRES_DB'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

alchemist.init_app(app)
alchemist.drop_all(app=app)
alchemist.create_all(app=app)

@app.route('/')
def hello_world():
    return 'Hello World 😘!!!'


@app.route('/name', methods=["POST"])
def hello_name():
    data = request.get_json()
    newData = TodoModel(first_name=data.get("first_name"), last_name=data.get("last_name"))
    alchemist.session.add(newData)
    alchemist.session.commit()
    return 'Hello there, {} 😜!'.format(data.get("first_name"))

@app.route('/all', methods=["GET"])
def getAllName():
    query_result = alchemist.session.query(TodoModel).all()
    output = ManyTodoSchema.dump(query_result)
    return {"names": output}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)