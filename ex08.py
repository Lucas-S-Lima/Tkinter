from tkinter import *
from tkinter.ttk import Combobox

def verificar_numero():
    try:
        numero = int(campo_numero.get())
        opcao_selecionada = combo.get()
        
        #CASO DO NÚMERO POSITIVO
        
        if numero > 0:
            if opcao_selecionada == 'POSITIVO':
                label_resultado_opcao.config(text='VERDADEIRO')
            else:
               label_resultado_opcao.config(text='FALSA') 
        
        # CASO DO NÚMERO NEGATIVO

        elif numero < 0:
            if opcao_selecionada == 'NEGATIVO':
                label_resultado_opcao.config(text='VERDADEIRO')
            else:
               label_resultado_opcao.config(text='FALSA') 
      
        # CASO DO NÚMERO ZERO

        else:
            if opcao_selecionada == 'ZERO':
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

combo = Combobox(window)
combo['values'] = ('Selecione', 'POSITIVO', 'NEGATIVO', 'ZERO')
combo.current(0)
combo.pack()

botao_verificar = Button(window, text='Verificar', width=10, font='arial 11 bold', fg='white', bg='blue', command=verificar_numero)
botao_verificar.pack(pady=15)

label_resultado = Label(window, text='Resultado', font='arial 12 bold')
label_resultado.pack(pady=10)

label_resultado_opcao = Label(window, text='Status', font='arial 12 bold', fg='red')
label_resultado_opcao.pack()

window.mainloop()