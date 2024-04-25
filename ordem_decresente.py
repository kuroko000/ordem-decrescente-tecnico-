#codigo aonde a pessoa escreve 3 numeros e os colocamos em ordem decrecente 

#expecificção do que vai ser feito
print("Precisamos que você nos dê 3 números, para colocarmos eles em ordem decrescente para você!")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Inicializando as variáveis
maiornumero = num1
numerodomeio = num2
menornumero = num3

# Encontrando o maior número
if num2 > maiornumero:
    maiornumero = num2
if num3 > maiornumero:
    maiornumero = num3

# Encontrando o menor número
if num2 < menornumero:
    menornumero = num2
if num1 < menornumero:
    menornumero = num1

# Encontrando o número do meio
numerodomeio = (num1 + num2 + num3) - (maiornumero + menornumero)

print("\n", maiornumero, numerodomeio, menornumero)