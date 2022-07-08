from .db_usuarios import UsuariosDB
from ..extratos.db_extratos import ExtratosDB


class Usuario(UsuariosDB):
    def __init__(self, cpf):
        super().__init__()
        self.cpf = cpf
        self.nome = ""
        self.saldo = 0
    
        usuario = self.select(self.cpf)
        if usuario:
            self.nome = usuario['nome']
            self.saldo = usuario['saldo']
        else:
            self.cadastrar_usuario()
            
    def cadastrar_usuario(self):
        print('Para abrir sua conta, insira seu nome:')
        self.nome = input('> ')
        self.insert()
        
    def extrato(self):
        db_extrato = ExtratosDB()
        extrato = db_extrato.select(self.cpf)
        
        print(f'{"OPERAÇÃO":<10}{"VALOR DA OPERAÇÃO":<22}{"SALDO":<15}{"DATA"}\n')
        if extrato:
            for registro in extrato:
                operacao = registro['operacao']
                valor = f"R$ {registro['valor']:.2f}"
                saldo = f"R$ {registro['saldo']:.2f}"
                data = registro['data']
                
                print(f"{operacao:<10}{valor:<22}{saldo:<15}{data}")
        else:
            print('Não existe movimentação.')
    
        print(f'\n\nSaldo Atual: {self.saldo}')
        input('Pressione enter para voltar ao menu principal...')
        