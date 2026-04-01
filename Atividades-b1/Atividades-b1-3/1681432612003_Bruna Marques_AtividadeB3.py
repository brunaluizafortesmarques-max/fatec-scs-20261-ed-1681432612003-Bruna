"""
------------------------------- ------------------------------------------------------------
* Fatec São Caetano do Sul                                                                   *
* Atividade B1-3                                                                             *
* *
* Autor: 1681432612003 nome: Bruna Luíza Fortes Marques                             *
* Objetivo: Criação de uma cauculadora utilizando pilha       *
* data: 31/03/2026                                                                           *
---------------------------------------------------------------------------------------------
"""

class pilha_calc:
    def __init__(self):
        self.X1 = 0
        self.Y1 = 0
        self.Z1 = 0
        self.T1 = 0

    def mostrar_pilha(self):
        print(f"T={self.T1} | Z={self.Z1} | Y={self.Y1} | X={self.X1}")

    def empilhar_valor(self, item):
        self.T1 = self.Z1
        self.Z1 = self.Y1
        self.Y1 = self.X1
        self.X1 = float(item)

    def desempilhar_resultado(self, resultado):
        self.X1 = resultado
        self.Y1 = self.Z1
        self.Z1 = self.T1


class hp12c_calc(pilha_calc):
    def __init__(self):
        super().__init__()

    def verificar_operador(self, item):
        if item not in ["+", "-", "*", "/"]:
            raise ValueError("Operador inválido!")

        a = self.Y1
        b = self.X1

        if item == "+":
            resultado = a + b
        elif item == "-":
            resultado = a - b
        elif item == "*":
            resultado = a * b
        elif item == "/":
            if b == 0:
                raise ZeroDivisionError("Divisão por zero!")
            resultado = a / b

        self.desempilhar_resultado(resultado)


class conversao_exp:
    def __init__(self):
        self.pilha_exp = []

    def acrescentar(self, item):
        b = self.pilha_exp.pop()
        a = self.pilha_exp.pop()
        self.pilha_exp.append(f"({a} {item} {b})")

    def empilhar_item(self, item):
        self.pilha_exp.append(item)


minha_pilha = hp12c_calc()
minha_pilha2 = conversao_exp()

rpn = input("Digite a expressão RPN: ")
expressao = rpn.split()

print("\n--- Passo a passo (X, Y, Z, T) ---")

for item in expressao:
    if item.replace('.', '', 1).isdigit():
        minha_pilha.empilhar_valor(item)
        minha_pilha2.empilhar_item(item)
    else:
        minha_pilha.verificar_operador(item)
        minha_pilha2.acrescentar(item)

    minha_pilha.mostrar_pilha()

print("\nExpressão algébrica:")
print(*minha_pilha2.pilha_exp)

print(f"\nO resultado da expressão algébrica é: {minha_pilha.X1:.0f}")