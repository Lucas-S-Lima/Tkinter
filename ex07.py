from tkinter import *

def verificar_numero():
    try:
        numero = int(campo_numero.get())
        opcao_selecionada = lista_verificacao.get(ACTIVE)
        
        #CASO DO NÚMERO POSITIVO
        
        if numero > 0:
            if opcao_selecionada == 'POSITIVO':
                label_resultado_verificacao.config(text='VERDADEIRO')
            else:
               label_resultado_verificacao.config(text='FALSA') 
        
        # CASO DO NÚMERO NEGATIVO

        elif numero < 0:
            if opcao_selecionada == 'NEGATIVO':
                label_resultado_verificacao.config(text='VERDADEIRO')
            else:
               label_resultado_verificacao.config(text='FALSA') 
      
        # CASO DO NÚMERO ZERO

        else:
            if opcao_selecionada == 'ZERO':
                label_resultado_verificacao.config(text='VERDADEIRO')
            else:
                label_resultado_verificacao.config(text='FALSA')
        

    except ValueError:
        label_resultado_verificacao.config(text='Erro: entrada inválda.')
             

window = Tk()

window.title("Verificação de um número - 07")

window.geometry('300x390')

label_numero = Label(window, text='Digite um número: ', font='arial 12 bold', fg='blue')
label_numero.pack(pady='10')

campo_numero = Entry(window, font='arial 12 bold')
campo_numero.pack()
campo_numero.focus()

label_tipo = Label(window, text='Selecione o tipo de verificação:', font='arial 11 bold')
label_tipo.pack(pady=15)

lista_verificacao = Listbox(window, width=20, height=6, font='arial 11', justify=CENTER)
lista_verificacao.insert(1, 'POSITIVO')
lista_verificacao.insert(2, 'NEGATIVO')
lista_verificacao.insert(3, 'ZERO')
lista_verificacao.pack(pady=3)

botao_verificar = Button(window, text='Verificar', width=10, font='arial 11 bold', fg='white', bg='blue', command=verificar_numero)
botao_verificar.pack(pady=10)

label_resultado = Label(window, text='Resultado', font='arial 12 bold')
label_resultado.pack(pady=10)

label_resultado_verificacao = Label(window, text='Status', font='arial 12 bold', fg='red')
label_resultado_verificacao.pack()

window.mainloop()