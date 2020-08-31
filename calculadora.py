n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))
operacao = input("Entre com o tipo de operação(+, -, *, /): ")

result = 0

def equacao():
    if operacao == "+" :
        result = n1 + n2
        print(result)


equacao()

