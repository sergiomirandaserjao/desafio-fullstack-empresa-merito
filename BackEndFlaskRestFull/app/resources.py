from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app import db
from app.models import Fundo, Movimentacao
from app.schemas import FundoSchema, MovimentacaoSchema
from app.auth import login_user

class FundoResource(Resource):
    @jwt_required()
    def get(self, fundo_id):
        fundo = Fundo.query.get_or_404(fundo_id)
        return FundoSchema().dump(fundo)

    @jwt_required()
    def put(self, fundo_id):
        fundo = Fundo.query.get_or_404(fundo_id)
        # Atualizar fundo
        db.session.commit()
        return FundoSchema().dump(fundo)

    @jwt_required()
    def delete(self, fundo_id):
        fundo = Fundo.query.get_or_404(fundo_id)
        db.session.delete(fundo)
        db.session.commit()
        return '', 204

class MovimentacaoResource(Resource):
    @jwt_required()
    def get(self, movimentacao_id):
        movimentacao = Movimentacao.query.get_or_404(movimentacao_id)
        return MovimentacaoSchema().dump(movimentacao)

    @jwt_required()
    def post(self):
        # Criar movimentacao
        db.session.commit()
        return MovimentacaoSchema().dump(movimentacao), 201

class LoginResource(Resource):
    def post(self):
        # Lógica de login
