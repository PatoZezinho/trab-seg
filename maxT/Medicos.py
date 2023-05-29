from dataclasses import dataclass

@dataclass
class Medico:
    nome: str
    cpf: str
    salario: float
    especialidade: str
    crm: str

@dataclass
class MedicoEspecialista(Medico):
    area_especializacao: str
