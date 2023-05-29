from dataclasses import dataclass
from mailbox import NotEmptyError

@dataclass
class Funcionario:
    nome: str
    cpf: str
    salario: float

@dataclass
class Enfermeira(Funcionario):
    def __init__(self, nome, cpf, salario, especialidade):
        super().__init__(nome, cpf, salario)
        self.especialidade = especialidade


@dataclass
class TecnicaEnfermagem(Funcionario):
    turno: str
