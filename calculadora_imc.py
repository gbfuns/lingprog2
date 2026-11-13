import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        altura = int(campo_altura.get()) / 100
        peso = float(campo_peso.get().replace(",", "."))

        if altura <= 0 or peso <= 0:
            raise ValueError

        imc = peso / altura**2
        resultado.config(text=f"IMC: {imc:.2f}")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Informe uma altura e um peso válidos."
        )

def reiniciar():
    for campo in (campo_nome, campo_endereco, campo_altura, campo_peso):
        campo.delete(0, tk.END)

    resultado.config(text="Resultado")
    campo_nome.focus()

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("370x300")

tk.Label(janela, text="Nome Completo").grid(
    row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0)
)
campo_nome = tk.Entry(janela)
campo_nome.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)

tk.Label(janela, text="Endereço").grid(
    row=2, column=0, columnspan=2, sticky="w", padx=10, pady=(8, 0)
)
campo_endereco = tk.Entry(janela)
campo_endereco.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10)

tk.Label(janela, text="Altura (cm)").grid(
    row=4, column=0, sticky="w", padx=10, pady=(10, 0)
)
campo_altura = tk.Entry(janela)
campo_altura.grid(row=5, column=0, sticky="ew", padx=10)

tk.Label(janela, text="Peso (kg)").grid(
    row=6, column=0, sticky="w", padx=10, pady=(8, 0)
)
campo_peso = tk.Entry(janela)
campo_peso.grid(row=7, column=0, sticky="ew", padx=10)

resultado = tk.Label(janela, text="Resultado", relief="groove", width=18)
resultado.grid(
    row=4, column=1, rowspan=4, sticky="nsew", padx=10, pady=10
)

botoes = tk.Frame(janela)
botoes.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

botoes.columnconfigure(0, weight=1)
botoes.columnconfigure(1, weight=1)
botoes.columnconfigure(2, weight=1)

tk.Button(botoes, text="Calcular", command=calcular).grid(
    row=0, column=0, sticky="w"
)
tk.Button(botoes, text="Reiniciar", command=reiniciar).grid(
    row=0, column=1
)
tk.Button(botoes, text="Sair", command=janela.destroy).grid(
    row=0, column=2, sticky="e"
)

janela.mainloop()
