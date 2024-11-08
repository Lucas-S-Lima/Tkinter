from tkinter import *  
from tkinter.ttk import Combobox

def calculo():
    try: 
        numero = float(campo_numero.get())
        escolha_porcentagem = porcentagem.get()

        if escolha_porcentagem == '25':
            valor = numero * 0.25
            lista.insert("end", f"25% = {valor}")

        elif escolha_porcentagem == '50':
            valor = numero * 0.50
            lista.insert("end", f"50% = {valor}")

        elif escolha_porcentagem == '100':
            valor = numero * 1
            lista.insert("end", f"100% = {valor}")

        elif escolha_porcentagem == '150':
            valor = numero * 1.50
            lista.insert("end", f"150% = {valor}")

    except ValueError:
        lista.insert("end", "Erro: entrada inválida")

def limpar_lista():
    
    lista.delete(0, END)

window = Tk()

window.title("Dobro e Triplo")

window.geometry("300x520")

label_numero = Label(window, text="Digite um valor numérico: ", font="arial 12 bold", fg="blue")
label_numero.pack(pady=10)

campo_numero = Entry(window, font='arial 11 bold')
campo_numero.pack(pady=10)
campo_numero.focus()

porcentagem = StringVar()

porcentagem25 = Radiobutton(window, text='25%',value="25", variable=porcentagem, font='arial 12')
porcentagem50 = Radiobutton(window, text='50%',value="50", variable=porcentagem, font='arial 12')
porcentagem100 = Radiobutton(window, text='100%',value="100", variable=porcentagem, font='arial 12')
porcentagem150 = Radiobutton(window, text='150%',value="150", variable=porcentagem, font='arial 12')

porcentagem25.pack(pady=2)
porcentagem50.pack(pady=2)
porcentagem100.pack(pady=2)
porcentagem150.pack(pady=2)

botao_executar = Button(window, text='Executar', font='arial 12 bold', command=calculo)
botao_executar.pack(pady=5)

botao_limpar = Button(window, text='Limpar', font='arial 12 bold', command=limpar_lista)
botao_limpar.pack(pady=10)

lista = Listbox(window, width=30, height=7, font='arial 11 bold')
lista.pack()

window.mainloop()