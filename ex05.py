from tkinter import *

def calculo_do_anterior():
    try:
        valor = int(campo1.get())
        anterior = valor - 1
        label_resultado_calculo.config(text=f'{anterior}')
    except ValueError:
        label_resultado_calculo.config(text='Erro: entrada inválida.')

def limpar_campos():
    campo1.delete(0, END)
    label_resultado_calculo.config(text='0')
    
window = Tk()

window.title("Cálculo do número anterior")

window.geometry('300x350')

label_numero1 = Label(window, text='Digite um valor:', font='arial 12 bold', fg='blue')
label_numero1.pack(pady='10')

campo1 = Entry(window, font='arial 12')
campo1.pack()
campo1.focus()

botao_calcular = Button(window, text='Calcular', command=calculo_do_anterior, width='12', font='arial 11')
botao_calcular.pack(pady='20')

botao_limpar = Button(window, text='Limpar', command=limpar_campos, width='12', font='arial 11')
botao_limpar.pack()

label_resultado = Label(window, text='Resultado:', font='arial 12 bold')
label_resultado.pack(pady='20')

label_resultado_calculo = Label(window, text='0', font='arial 12 bold', fg='red')
label_resultado_calculo.pack()

window.mainloop()