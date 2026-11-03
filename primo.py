def primo(n):
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True

numero = int(input("Digite um número: "))

if primo(numero):
    print("Verdadeiro: o número", numero, "é primo.")
else:
    print("Falso: o número", numero, "não é primo.")
