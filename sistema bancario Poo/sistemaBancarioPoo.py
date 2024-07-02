<<<<<<< HEAD
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco): 
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property 
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False
        
        elif valor > 0:
            self._saldo -= valor
            print("\n||| Saque realizado com sucesso! |||")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n@@@ Depósito realizado com sucesso! @@@")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def __str__(self):
        return f"""\nAgência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente.nome}"""

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self) 

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property 
    def valor(self):
        return self._valor 
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)   

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
=======
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco): 
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property 
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False
        
        elif valor > 0:
            self._saldo -= valor
            print("\n||| Saque realizado com sucesso! |||")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n@@@ Depósito realizado com sucesso! @@@")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def __str__(self):
        return f"""\nAgência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente.nome}"""

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self) 

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property 
    def valor(self):
        return self._valor 
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)   

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
