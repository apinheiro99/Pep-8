class filanormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhaatual:str = ""

    def gerasenhaatual(self)-> None:
        self.senhaatual = f"NM{self.codigo}"

    def resetafila(self)-> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self)-> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa:int)-> str:
        clienteatual: str = self.fila.pop()
        self.clientesatendidos.append(clienteatual)
        return f"Cliente atual: {clienteatual} dirija-se ao caixa {caixa}"