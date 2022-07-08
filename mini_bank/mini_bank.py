from .ui import ui
from .utils import utils
from datetime import datetime
from .databases.usuarios.usuario import Usuario
from .databases.extratos.db_extratos import ExtratosDB


class MiniBank:
    TITULO = "Mini Bank"
    
    def __init__(self) -> None:
        self.usuario = None
        self.is_running = False
    
    def solicitar_cpf(self, cpf_invalido=False) -> str | None:
        ui.solicitar_cpf(self.TITULO)
        if cpf_invalido: ui.cpf_invalido()
        
        entrada = ui.console_input()
        
        if entrada in ('SAIR', 'X'):
            return self.stop()
        
        cpf = utils.limpar_cpf(entrada)
        if utils.validar_cpf(cpf):
            return cpf
        else: 
            return self.solicitar_cpf(cpf_invalido=True)
        
    def interpretar_escolha(self) -> None:
        escolha = ui.console_input()
        match escolha:
            case '1' | 'DEPOSITO' | 'DEPÓSITO':
                self.deposito()
            case '2' | 'SAQUE': 
                self.saque()
            case '3' | 'EXTRATO' | 'SALDO': 
                self.extrato_saldo()
            case '4' | "LOGOUT":
                ui.logout()
            case _:
                ui.operacao_invalida(titulo=self.TITULO)
                self.interpretar_escolha()
                
    def menu_principal(self):
        ui.display_menu_principal(titulo=self.TITULO, 
                                  nome_usuario=self.usuario.nome,
                                  saldo=self.usuario.saldo)
        self.interpretar_escolha()

    def deposito(self):
        valor_deposito = ui.deposito()
        
        if not valor_deposito:
            return self.menu_principal()
        
        self.usuario.saldo += valor_deposito
        self.usuario.update()
        
        extrato_db = ExtratosDB()
        extrato_db.insert({'CPF': self.usuario.cpf,
                           'operacao': 'DEPÓSITO',
                           'valor': valor_deposito,
                           'saldo': self.usuario.saldo,
                           'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')})
        
        ui.operacao_sucesso('Depósito', self.usuario.saldo)
        if ui.voltar_ao_menu_principal():
            self.menu_principal()
        else:
            ui.logout()
        
    def saque(self):
        valor_saque = ui.saque(self.usuario.saldo)
        
        if not valor_saque:
            return self.menu_principal()
        
        if valor_saque > self.usuario.saldo:
            ui.saque_invalido()
            return self.saque()
        
        self.usuario.saldo -= valor_saque
        self.usuario.update()
        
        extrato_db = ExtratosDB()
        extrato_db.insert({'CPF': self.usuario.cpf,
                           'operacao': 'SAQUE',
                           'valor': valor_saque,
                           'saldo': self.usuario.saldo,
                           'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')})
        
        ui.operacao_sucesso('Saque', self.usuario.saldo)
        if ui.voltar_ao_menu_principal():
            self.menu_principal()
        else:
            ui.logout()

    def extrato_saldo(self):
        ui.limpar_console()
        ui.display_titulo('EXTRATO')
        self.usuario.extrato()
        self.menu_principal()
                
    def start(self) -> None:
        self.is_running = True
        while self.is_running:
            cpf = self.solicitar_cpf()
            if cpf:
                self.usuario = Usuario(cpf)
                self.menu_principal()
                
    def stop(self) -> None:
        ui.finaliza_execucao()
        self.is_running = False
