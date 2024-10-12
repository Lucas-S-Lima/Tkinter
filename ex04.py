from tkinter import *

def triangulo_area():
    try:
        base = int(campo1.get())
        altura = int(campo2.get())
        area_triangulo = (base * altura) / 2
        label_resultado_calculo.config(text=f'{area_triangulo}')
    except ValueError:
        label_resultado_calculo.config(text='Erro: entrada inválida.')

def limpar_campos():
    campo1.delete(0, END)
    campo2.delete(0, END)
    label_resultado_calculo.config(text='0')

window = Tk()

window.title("Cálculo da área de um triângulo")

window.geometry('300x350')

label_numero1 = Label(window, text='Base do Triângulo:', font='arial 12 bold', fg='blue')
label_numero1.pack(pady='10')

campo1 = Entry(window, font='arial 12')
campo1.pack()
campo1.focus()

label_numero2 = Label(window, text='Altura do Triângulo:', font='arial 12 bold', fg='blue')
label_numero2.pack(pady='10')

campo2 = Entry(window, font='arial 12')
campo2.pack()

botao_calcular = Button(window, text='Calcular', command=triangulo_area, width='12', font='arial 11')
botao_calcular.pack(pady='20')

botao_limpar = Button(window, text='Limpar', command=limpar_campos, width='12', font='arial 11')
botao_limpar.pack()

label_resultado = Label(window, text='Resultado:', font='arial 12 bold')
label_resultado.pack(pady='20')

label_resultado_calculo = Label(window, text='0', font='arial 12 bold', fg='red')
label_resultado_calculo.pack()

window.mainloop()