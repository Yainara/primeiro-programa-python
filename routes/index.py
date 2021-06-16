from flask import Blueprint
from flask import render_template
from flask import request
from services import index as service
from models.Pessoa import Pessoa

index_blueprint = Blueprint("index", __name__, static_folder="../static", template_folder="../templates", static_url_path="/static/index")

@index_blueprint.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@index_blueprint.route("/cadastrar", methods=['POST'])
def cadastrar():
    form = dict(request.form)
    pessoa = Pessoa(form["name"], form["email"], form["address"], form["city"], form["state"], form["cep"])
    response = service.cadastrar(pessoa)
    return response

@index_blueprint.route("/pesquisar", methods=['GET'])
def find():
    return render_template("find.html")

@index_blueprint.route("/busca", methods=['GET'])
def busca():
    name= request.args.get('name')
    pessoa = service.busca(name)

    if pessoa == None:
        return "Não encontrado", 404

    return render_template("info.html", pessoa = pessoa[0]), 200

@index_blueprint.route("/editar", methods=['GET'])
def editar():
    return render_template("edit.html")

@index_blueprint.route("/info", methods=['GET'])
def info():
    name= request.args.get('name')
    pessoa = service.busca(name)
    return render_template("infosedit.html", pessoa = pessoa[0])

@index_blueprint.route("/deletar", methods=['GET'])
def deletar():
    return render_template("exclui.html")

@index_blueprint.route("/infoedit", methods=['GET'])
def find_edit():
    name= request.args.get('name')
    pessoa = service.busca(name)
    return render_template("infosedit.html", pessoa = pessoa[0])

@index_blueprint.route("/edit", methods=['PUT'])
def edit():
    form = dict(request.form)
    pessoa = Pessoa(form["name"], form["email"], form["address"], form["city"], form["state"], form["cep"])

    response = service.edit(pessoa)
    return str(response)

@index_blueprint.route("/delete", methods=['GET'])
def delete():
    return render_template("delete.html")

@index_blueprint.route("/info_delete", methods=['GET'])
def info_delete():
    name= request.args.get('name')
    pessoa = service.busca(name)
    return render_template("info_delete.html", pessoa = pessoa[0])

@index_blueprint.route("/deletar", methods=['DELETE'])
def delete_final():
    form = dict(request.form)
    pessoa = Pessoa(form["name"], form["email"], form["address"], form["city"], form["state"], form["cep"])

    response = service.deletar(pessoa)
    return str(response)
