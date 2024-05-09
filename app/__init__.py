from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from config import environment

app = Flask(__name__)
app.config.from_object(environment[getenv('ENVIRONMENT')])




authorizations={
    'Bearer':{
        'type':'apiKey',
        'in':'header',
        'name':'Authorization'
    }
}

api=Api(
    app,
    title= 'Bordeplait Version',
    version='0.1',
    description='Repaso la documentacion',
    authorizations=authorizations,
    doc='/swagger-ui'

)



db = SQLAlchemy(app)


migrate= Migrate(app,db)


jwt =JWTManager(app)

mail = Mail(app)
