from tkinter import *

entradas = []
entradas_pesos = []
lista_notas = []
lista_pesos = []

def gerar_campos():

    try:
        numero_campos = int(campo_numero.get())
        
        botao_criarcampos.config(state='disabled')
        botao_media.config(state='active')  

        for widget in entradas:
            widget.destroy()
        entradas.clear()
            
        for widget in lista_notas:
            widget.destroy()
        lista_notas.clear()

        for widget in lista_pesos:
            widget.destroy()
        lista_notas.clear()

        for widget in entradas_pesos:
            widget.destroy()
        lista_pesos.clear()

        for i in range(numero_campos):
            
            notas = Label(window, text=f'Nota {i+1}', font='arial 12 bold', fg='blue')
            notas.pack()
            lista_notas.append(notas)

            campo_nota = Entry(window, font='arial 11 bold')
            campo_nota.pack(pady=5)
            entradas.append(campo_nota)

            pesos = Label(window, text=f'Peso {i+1}', font='arial 12 bold', fg='blue')
            pesos.pack()
            lista_pesos.append(pesos)

            campo_peso = Entry(window, font='arial 11 bold')
            campo_peso.pack()
            entradas_pesos.append(campo_peso)


    except ValueError:
        label_erro.config(text='Erro: entrada inválida')


def calcular_media():
    
    botao_media.config(state='disabled') 
    botao_criarcampos.config(state='active')  

    lista_valores = []
    lista_pesos = []
    lista_ponderada = []

    try:
        
        for campo in entradas:
            valor = float(campo.get())  
            lista_valores.append(valor)

        for campo_peso in entradas_pesos:
            peso = float(campo_peso.get())
            lista_pesos.append(peso)    

        for valor, peso in zip(lista_valores, lista_pesos):
            ponderada = valor * peso
            lista_ponderada.append(ponderada)

            media_ponderada = sum(lista_ponderada) / sum(lista_pesos)
            label_resultado.config(text=f'A média ponderada é: {media_ponderada:.2f}')

    except ValueError:
        label_resultado.config(text="Erro: entrada inválida, tente novamente.")
        

window = Tk()
window.title("Calculadora de Média Ponderada")
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
