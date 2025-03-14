from flask import Blueprint, render_template

bp = Blueprint("todo", __name__, url_prefix="/todo")

@bp.route("/listar")
def list():
    return "Lista de tarefas"

@bp.route("/criar")
def create():
    return "Criar tarefa"