from abc import ABC, abstractmethod
from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(ABC):

    def __init__(self) -> None:
        self.codigo: int = 0
        self.fila = []
        self.clientes_atendidos = []
        self.senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def __insere_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.__insere_cliente()

    @abstractmethod
    def gera_senha_atual(self) -> None:
        pass

    @abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        pass
