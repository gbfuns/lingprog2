dias = int(input("Informe sua idade em dias: "))

anos, resto = divmod(dias, 365)
meses, dias = divmod(resto, 30)

print(f"Você tem {anos} anos, {meses} meses e {dias} dias")
