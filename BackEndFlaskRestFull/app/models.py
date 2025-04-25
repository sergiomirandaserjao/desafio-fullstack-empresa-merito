from datetime import datetime
from app import db

class Fundo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ticker = db.Column(db.String(10), unique=True, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    valor_cota = db.Column(db.Float, nullable=False)

class Movimentacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fundo_id = db.Column(db.Integer, db.ForeignKey('fundo.id'), nullable=False)
    data = db.Column(db.Date, default=datetime.utcnow)
    valor = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    cotas = db.Column(db.Float, nullable=False)
    fundo = db.relationship('Fundo', backref=db.backref('movimentacoes', lazy=True))
    
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://usuario:senha@localhost:1433/db_name?driver=ODBC+Driver+17+for+SQL+Server'

