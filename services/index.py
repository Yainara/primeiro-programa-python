from models import Pessoa
from repositories import pessoa as repo

def cadastrar(pessoa: Pessoa):
    try:
        repo.insert(pessoa)
        return "Cadastrado com sucesso"
    except Exception as e:
        print(e)
        return "Algo deu errado"

def busca(name: str):
    pessoa = repo.find(name)

    if (pessoa == []):
        return None

    pessoa = parse_pessoa(pessoa[0])

    return pessoa

def parse_pessoa(pessoa: list):
    return_list = []
    dict = {}

    dict["name"] = pessoa[1]
    dict["email"] = pessoa[2]
    dict["address"] = pessoa[3]
    dict["city"] = pessoa[4]
    dict["state"] = pessoa[5]
    dict["cep"] = pessoa[6]

    return_list.append(dict)

    return return_list

def edit(pessoa: Pessoa):
    repo.edit(pessoa)
    return 200

def deletar(pessoa: Pessoa):
    repo.deletar(pessoa)
    return 200
