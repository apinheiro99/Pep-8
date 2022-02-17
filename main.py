from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria

import os

os.system("clear")

fila_teste = filanormal()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
print(fila_teste.chamacliente(12))
print(fila_teste.chamacliente(5))

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(7))
print(fila_teste_2.estatistica("10/01/1980",198,"detail"))