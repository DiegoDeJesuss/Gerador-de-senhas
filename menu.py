import tkinter as tk
import random
from tkinter import PhotoImage

def gerar_senhas():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç', '`', '/', '|',
             'ª', 'º', '¿', ]

  print("Senha gerada!")
  # quantas letras quer em sua senha?
  nr_letters = int(7)
  # quantos simbolos quer em sua senha?
  nr_symbols = int(1)
  # quantos numeros quem em sua senha?
  nr_numbers = int(4)

  password_list = []

  for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

    # print(password_list)
    random.shuffle(password_list)
  # print(password_list)

  password = ""
  for char in password_list:
    password += char

  mensagem["text"]=(f"{password}")
  print(password)





janela = tk.Tk()
janela.title('Gerador de senhas fortes')
janela.geometry("400x260")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)

logo = PhotoImage(file="logoCadeado.png")
app_label = tk.Label(janela, image=logo)
app_label.grid(row=1, column=1, pady=10)

Menu = tk.Label(text="Gerador de senhas")
Menu.grid(row=0, column=0, columnspan=2, sticky="NSEW")
Menu.configure(font=("Cooper Black", 20, "bold" ))

mensagem = tk.Label(bg='#FFd700')
mensagem.grid(row=2, column=1, columnspan=2, sticky="NSEW")

botao = tk.Button(janela, text="Gerar Senhas fortes",  command=gerar_senhas, width=80, height=2)
botao.grid(row=3, column=1, columnspan=2)



janela.mainloop()