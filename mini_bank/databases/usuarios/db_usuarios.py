import os
import json


class UsuariosDB:
    
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.saldo = None
        self.caminho_db = os.path.join(os.path.dirname(__file__), 'data', f'usuarios.json')
        self.verificar_existencia_db()
    
    def verificar_existencia_db(self):
        if not os.path.exists(self.caminho_db):
            open(self.caminho_db, 'a').close()
            
    def select(self, cpf: str) -> dict:
        with open(self.caminho_db, 'r') as arquivo:
            database = arquivo.read()
            
        if not database:
            return {}
        
        usuarios = json.loads(database)            
        usuario = usuarios.get(cpf)
        if usuario:
            return usuario

    def insert_update(self):
        with open(self.caminho_db, 'r') as arquivo:
            database = arquivo.read()

        with open(self.caminho_db, 'w') as arquivo:
            usuario = {'CPF': self.cpf,
                       'nome': self.nome,
                       'saldo': self.saldo}

            database = json.loads(database) if database else {}
            database[self.cpf] = usuario

            json.dump(database, arquivo, indent=4)

    def insert(self) -> None:
        self.insert_update()

    def update(self) -> None:
        self.insert_update()
