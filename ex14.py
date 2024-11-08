from tkinter import *

entradas = []
labels_notas = []

def gerar_campos():

    try:
        numero_campos = int(campo_numero.get())
        
        botao_criarcampos.config(state='disabled')
        botao_media.config(state='active')  

        for widget in entradas:
            widget.destroy()
        entradas.clear()
            
        for widget in labels_notas:
            widget.destroy()
        labels_notas.clear()

        for i in range(numero_campos):
            numeracao_campos = Label(window, text=f'Nota {i+1}', font='arial 12 bold', fg='blue')
            numeracao_campos.pack()
            labels_notas.append(numeracao_campos)

            campo = Entry(window, font='arial 11 bold')
            campo.pack(pady=5)
            entradas.append(campo)

    except ValueError:
        label_erro.config(text='Erro: entrada inválida')


def calcular_media():
    
    botao_media.config(state='disabled') 
    botao_criarcampos.config(state='active')  

    lista_valores = []

    try:
        for campo in entradas:
            valor = float(campo.get())  
            lista_valores.append(valor)

            media = sum(lista_valores) / len(lista_valores)
            label_resultado.config(text=f'A média é: {media:.2f}')

    except ValueError:
        label_resultado.config(text="Erro: entrada inválida, tente novamente.")
        

window = Tk()
window.title("Calculadora de Média")
window.geometry("300x520")


label_numero = Label(window, text="Quantidade de notas: ", font="arial 12 bold", fg="blue")
label_numero.pack(pady=10)


campo_numero = Entry(window, font='arial 11 bold')
campo_numero.pack(pady=10)
campo_numero.focus()


botao_criarcampos = Button(window, text='Criar Campos de Notas', font='arial 12 bold', command=gerar_campos)
botao_criarcampos.pack(pady=5)


botao_media = Button(window, text='Calcular Média', font='arial 12 bold', command=calcular_media)
botao_media.pack(pady=5)


label_resultado = Label(window, text="Resultado", font="arial 12 bold", fg='red')
label_resultado.pack(pady=5)


label_erro = Label(window, font='arial 12 bold')
label_erro.pack()

window.mainloop()
