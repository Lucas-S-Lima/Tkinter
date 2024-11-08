from tkinter import *  
from tkinter.ttk import Combobox

def dobro_triplo():
    numero = int(campo_numero.get())

    try:
        if combo.current() == 0:
            dobro = numero * 2
            lista.insert("end", f"O dobro é: {dobro}")

        elif combo.current() == 1:
           triplo = numero * 3
           lista.insert("end", f"O triplo é: {triplo}")

        elif combo.current() == 2:
            dobro = numero * 2
            triplo = numero * 3
            lista.insert("end", f"O dobro é: {dobro}")
            lista.insert("end", f"O triplo é: {triplo}")

    except ValueError:
        lista.insert("Erro: entrada inválida.")


def limpar_lista():
    lista.delete(0, END)

window = Tk()

window.title("Dobro e Triplo")

window.geometry("300x420")

label_numero = Label(window, text="Digite um valor numérico: ", font="arial 12 bold", fg="blue")
label_numero.pack(pady=10)

campo_numero = Entry(window, font='arial 11 bold')
campo_numero.pack()
campo_numero.focus()

combo = Combobox(window, font='arial 9')
combo['values'] = ('Dobro', 'Triplo', 'Ambos')
combo.current(0)
combo.pack(pady=10)

botao_executar = Button(window, text='Executar', font='arial 12 bold', command=dobro_triplo)
botao_executar.pack(pady=10)

botao_limpar = Button(window, text='Limpar', font='arial 12 bold', command=limpar_lista)
botao_limpar.pack(pady=10)


lista = Listbox(window, width=30, height=5, font='arial 11 bold')
lista.pack()

window.mainloop()