from dataclasses import dataclass
from flaskr.models_db import db


@dataclass
class Pessoa(db.Model):
    __tablename__ = 'pessoas'
    id:int = db.Column(
        db.Integer,
        primary_key = True )

    nome:str = db.Column(
        db.String(64),
        index    = False,
        unique   = True,
        nullable = False )

    data_nascimento:str = db.Column(
        db.DateTime,
        index    = False,
        unique   = True,
        nullable = False )


    def __repr__(self):
        return '<Pessoa %r>' % self.nome