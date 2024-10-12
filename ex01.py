from tkinter import *

def calcula_soma():
    try:
        n1 = int(campo1.get())
        n2 = int(campo2.get()) 
        soma = n1 + n2
        label_resultado_soma.config(text=f'{soma}')
    except ValueError:
        label_resultado_soma.config(text='Erro: entrada inválida.')

def limpar_dados():
    campo1.delete(0, END)
    campo2.delete(0, END)
    label_resultado_soma.config(text='0')


window = Tk()

window.title("Soma de dois números")

window.geometry("300x350")

label_numero1 = Label(window, text="Número 1:", fg='blue', font='arial 12 bold')
label_numero1.pack(pady='15')
campo1 = Entry(window, font='arial 12')
campo1.pack(pady=10)
campo1.focus()

label_numero2 = Label(window, text="Número 2:", fg='blue', font='arial 12 bold')
label_numero2.pack()
campo2 = Entry(window, font='arial 12')
campo2.pack(pady=10)

botao_calcular = Button(window, text='Calcular', command=calcula_soma, font='arial 12 bold', overrelief=RAISED)
botao_calcular.pack()

botao_limpar = Button(window, text='Limpar', command=limpar_dados, font='arial 12 bold', overrelief=RAISED)
botao_limpar.pack(pady='15')

label_resultado = Label(window, text='Resultado', font='arial 12')
label_resultado.pack()

label_resultado_soma = Label(window, text='0', fg='red', font='arial 12 bold')
label_resultado_soma.pack(pady=20)

window.mainloop()