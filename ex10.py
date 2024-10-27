from tkinter import *
from tkinter.ttk import Radiobutton

def recuperarEstado():
    try:
        numero = int(campo_numero.get())
        positivo = var_positivo.get()
        negativo = var_negativo.get()
        zero = var_zero.get()
        
        #CASO DO NÚMERO POSITIVO
        
        if numero > 0 and positivo:
            label_resultado_opcao.config(text='VERDADEIRO') 

        elif numero < 0 and negativo:
            label_resultado_opcao.config(text='VERDADEIRO') 

        elif numero == 0 and zero:
            label_resultado_opcao.config(text='VERDADEIRO')
        
        else:
            label_resultado_opcao.config(text='FALSA')        

    except ValueError:
        label_resultado_opcao.config(text='Erro: entrada inválda.')

window = Tk()

window.title("Verificação de um número - 08")

window.geometry('300x390')

label_numero = Label(window, text='Digite um número: ', font='arial 12 bold', fg='blue')
label_numero.pack(pady='10')

campo_numero = Entry(window, font='arial 12 bold')
campo_numero.pack()
campo_numero.focus()

label_tipo = Label(window, text='Selecione o tipo de verificação:', font='arial 11 bold')
label_tipo.pack(pady=15)

var_positivo = StringVar()
var_negativo = StringVar()
var_zero = StringVar()

botao_check_positivo = Radiobutton(window, text='POSITIVO', var=var_positivo)
botao_check_positivo.pack()

botao_check_negativo = Radiobutton(window, text='NEGATIVO', var=var_negativo)
botao_check_negativo.pack()

botao_check_zero = Radiobutton(window, text='ZERO', var=var_zero)
botao_check_zero.pack()

botao_verificar = Button(window, text='Verificar', width=10, font='arial 11 bold', fg='white', bg='blue', command=recuperarEstado)
botao_verificar.pack(pady=15)

label_resultado = Label(window, text='Resultado', font='arial 12 bold')
label_resultado.pack(pady=10)

label_resultado_opcao = Label(window, text='Status', font='arial 12 bold', fg='red')
label_resultado_opcao.pack()

window.mainloop()