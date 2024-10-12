from tkinter import *

def calcula_soma():
    try:
        n1 = int(campo1.get())
        n2 = int(campo2.get()) 
        soma = n1 + n2
        label_resultado_soma.config(text=f'{soma}')
    except ValueError:
        label_resultado_soma.config(text='Erro: entrada inválida.')

window = Tk()

window.title("Soma de dois números")

window.geometry("300x300")

label_numero1 = Label(window, text="Número 1:", fg='blue', font='arial 12 bold')
label_numero1.pack()

campo1 = Entry(window, font='arial 12')
campo1.pack(pady=10)
campo1.focus()

label_numero2 = Label(window, text="Número 2:", fg='blue', font='arial 12 bold')
label_numero2.pack()

campo2 = Entry(window, font='arial 12')
campo2.pack(pady=10)

botao = Button(window, text='Calcular', command=calcula_soma, font='arial 12 bold')
botao.pack()

label_resultado = Label(window, text='Resultado', font='arial 12')
label_resultado.pack(pady=20)

label_resultado_soma = Label(window, text='0', fg='red', font='arial 12 bold')
label_resultado_soma.pack()

window.mainloop()