from projeto.models.principal.funcionario import Funcionario
from projeto.models.principal.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, 
                 dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, oab:str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.oab = oab

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nOAB: {self.oab}")
    