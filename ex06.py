from tkinter import *

def verificar_numero():
    try:
        numero = int(campo_numero.get())

        if numero == 0:
            label_resultado_calculo.config(text='O número informado é nulo.')
        elif numero > 0:
            label_resultado_calculo.config(text=f'O número {numero} é positivo.')

        elif numero < 0:
            label_resultado_calculo.config(text=f'O número {numero} é negativo.')
            

    except ValueError:
        label_resultado_calculo.config(text='Erro: entrada inválida.')

window = Tk()

window.title("Verificação de um número - 06")

window.geometry('300x350')

label_numero = Label(window, text='Digite um número: ', font='arial 12 bold', fg='blue')
label_numero.pack(pady='10')

campo_numero = Entry(window, font='arial 12 bold')
campo_numero.pack()
campo_numero.focus()

botao_verificar = Button(window, text='Verificar', command=verificar_numero, width='12', font='arial 12 bold', bg='blue', fg='white')
botao_verificar.pack(pady='15')

label_resultado = Label(window, text='Resultado', font='arial 12 bold', fg='blue')
label_resultado.pack(pady='10')

label_resultado_calculo = Label(window, text='Status', font='arial 12 bold', fg='red')
label_resultado_calculo.pack()

window.mainloop()