from abc import ABC


class FilaBase(ABC):

    def __init__(self) -> None:
        self.codigo: int = 0
        self.fila = []
        self.clientes_atendidos = []
        self.senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
