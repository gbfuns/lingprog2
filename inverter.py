def inverter(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return " ".join(palavras_invertidas)

frase = input("Digite uma frase:")
print("Frase invertida:", inverter(frase))
