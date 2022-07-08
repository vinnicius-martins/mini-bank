import os
import json


class ExtratosDB:
    
    def __init__(self):
        self.caminho_db = os.path.join(os.path.dirname(__file__), 'data', f'extratos.json')
        self.verificar_existencia_db()
    
    def verificar_existencia_db(self):
        if not os.path.exists(self.caminho_db):
            open(self.caminho_db, 'a').close()
            
    def select(self, cpf: str) -> list:
        with open(self.caminho_db, 'r') as arquivo:
            database = arquivo.read()
            
        if not database:
            return []
        
        extratos = json.loads(database)            
        extrato = extratos.get(cpf)
        if extrato:
            return extrato

    def insert(self, registro: dict):
        cpf = registro['CPF']
        
        with open(self.caminho_db, 'r') as arquivo:
            database = arquivo.read()

        with open(self.caminho_db, 'w') as arquivo:
            if database:
                database = json.loads(database)
            else:
                database = {}
                
            if database.get(cpf):
                database[cpf].append(registro)
            else:
                database[cpf] = [registro]

            json.dump(database, arquivo, indent=4)
