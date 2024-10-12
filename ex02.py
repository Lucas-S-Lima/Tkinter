from tkinter import *

def quadrado_area():
    try:
        lado = int(campo1.get())
        area_quadrado = (lado ** 2)
        label_resultado_calculo.config(text=f'{area_quadrado}')
    except ValueError:
        label_resultado_calculo.config(text='Erro: entrada inválida.')

def limpar_campos():
    campo1.delete(0, END)
    label_resultado_calculo.config(text='0')

    
window = Tk()

window.title("Cálculo da área de um quadrado")

window.geometry('300x350')

label_numero1 = Label(window, text='Lado do Quadrado:', font='arial 12 bold', fg='blue')
label_numero1.pack(pady='10')

campo1 = Entry(window, font='arial 12')
campo1.pack()
campo1.focus()

botao_calcular = Button(window, text='Calcular', command=quadrado_area, width='12', font='arial 11')
botao_calcular.pack(pady='20')

botao_limpar = Button(window, text='Limpar', command=limpar_campos, width='12', font='arial 11')
botao_limpar.pack()

label_resultado = Label(window, text='Resultado:', font='arial 12 bold')
label_resultado.pack(pady='20')

label_resultado_calculo = Label(window, text='0', font='arial 12 bold', fg='red')
label_resultado_calculo.pack()

window.mainloop()