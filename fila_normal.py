from fila_base import FilaBase
from constantes import CODIGO_NORMAL


class filanormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senhaatual = f"{CODIGO_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        clienteatual: str = self.fila.pop(0)
        self.clientes_atendidos.append(clienteatual)
        return f"Cliente atual: {clienteatual} dirija-se ao caixa {caixa}"
