"""
Escopo é o “alcance” onde aquele nome (variável, função etc.) pode ser usado.
Python segue a regra conhecida como LEGB, que define a ordem de busca de variáveis:

L → Local → E → Enclosing → G → Global → B → Built-in

Letra  Nome completo	Explicação
L	   Local	        Escopo dentro da função atual
E	   Enclosing	    Escopo de funções que contêm outra função
G	   Global	        Escopo do arquivo (fora de funções)
B	   Built-in	        Nomes nativos do Python (print, len, etc.)

Global:

x = 10  # variável global

def mostrar():
    print(x)  # acessa a variável global

mostrar()  # saída: 10


Local: 

def exemplo():
    y = 5   # variável local
    print(y)

exemplo()
print(y)   # erro: y não existe fora da função


Modificar uma variável Global:

contador = 0

def incrementar():
    global contador # Sem global, o Python criaria uma nova variável local chamada contador, e a global continuaria intacta.
    contador += 1

incrementar()
print(contador)  # saída: 1

"""

inimigos = 2

def aumentar_inimigos(atual):
    return atual + 1

inimigos = aumentar_inimigos(inimigos) # irá pegar a quantidade atual e incrementar 1
print(inimigos)