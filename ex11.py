from tkinter import *
from tkinter import Label

def exibir_numero():
    try:
        numero = int(campo_numero.get())
        
        if marcavel_anterior_status.get() and marcavel_posterior_status.get():
            numero_anterior = numero - 1
            numero_posterior = numero + 1
            lista.insert("end", f'Anterior = {numero_anterior}')
            lista.insert("end", f'Posterior = {numero_posterior}')
        
        elif marcavel_anterior_status.get():
            numero_anterior = numero - 1
            lista.insert("end", f'Anterior = {numero_anterior}')
        
        elif marcavel_posterior_status.get():
            numero_posterior = numero + 1
            lista.insert("end", f'Posterior = {numero_posterior}')
    
    except ValueError:
        lista.insert('Erro: entrada inválida.')

def limpar_lista():

    lista.delete(0, END)

window = Tk()

window.title("Anterior e Posterior")

window.geometry("300x420")

label_numero = Label(window, text="Digite um valor numérico: ", font="arial 12 bold", fg="blue")
label_numero.pack(pady=10)

campo_numero = Entry(window, font='arial 12')
campo_numero.pack()
campo_numero.focus()

marcavel_posterior_status = BooleanVar()
posterior = marcavel_posterior_status.set(False)

marcavel_anterior_status = BooleanVar()
anterior = marcavel_anterior_status.set(False)

botao_marcavel_anterior = Checkbutton(window, text='Anterior', var=marcavel_anterior_status, font=12)
botao_marcavel_anterior.pack(pady=10)

botao_marcavel_posterior = Checkbutton(window, text='Posterior', var=marcavel_posterior_status, font=12)
botao_marcavel_posterior.pack()

botao_executar = Button(window, text='Executar', font='arial 12 bold', command=exibir_numero)
botao_executar.pack(pady=10)

botao_limpar = Button(window, text='Limpar', font='arial 12 bold', command=limpar_lista)
botao_limpar.pack(pady=10)

lista =  Listbox(window, width=30, height=5, font='arial 11 bold')
lista.pack()

window.mainloop()