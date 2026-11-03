import math

print("Insira os valores para calcular um triâgulo")
a = int(input("Valor A: "))
b = int(input("Valor B: "))
c = int(input("Valor C: "))

if a < b + c and b < a + c and c < a + b:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Área:", area)
else:
    print("Não formam triângulo:", a, b, c)
