from constantes import TIPO_FILA_NORMAL
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila

import os

os.system("clear")

fila_teste = FilaNormal()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(12))
print(fila_teste.chama_cliente(5))

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(7))
print(fila_teste_2.estatistica("10/01/1980", 198, "detail"))

print()
teste_fabrica = FabricaFila.pega_fila(TIPO_FILA_NORMAL)
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(5))
print(teste_fabrica.chama_cliente(2))
