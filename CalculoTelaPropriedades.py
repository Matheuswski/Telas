from tkinter import*

def bt_soma():
    #Codigo abaixo é para validar a entrada apenas de numeros
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #Se valores não forem numericos imprime a mensagem abaixo:
        lb["text"] = num1 + num2
        lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos"
        lb["bg"] = "red"


def bt_multiplicacao():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
       num1 = int(ed1.get())
       num2 = int(ed2.get())
       lb["text"] = num1 * num2
       lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos"
        lb["bg"] = "red"

def bt_divisao():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
       num1 = int(ed1.get())
       num2 = int(ed2.get())
       lb["text"] = num1 / num2
       lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos"
        lb["bg"] = "red"

def bt_menos():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
       num1 = int(ed1.get())
       num2 = int(ed2.get())
       lb["text"] = num1 - num2
       lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos"
        lb["bg"] = "red"


i=Tk()
i.title("Programa financeiro")
i.title("")
i.geometry('980x720+250+30')

lb=Label(i, text="0")
lb.place(x=230, y=200)

lb2=Label(i, text="Matheus Golanowski")
lb2.place(x=250, y=380)


bt=Button(i, width="20", text='soma', command=bt_soma)
bt.place(x=230, y=230)

bt=Button(i, width="20", text='multiplicar', command=bt_multiplicacao)
bt.place(x=230, y=260)

bt=Button(i, width="20", text='divisão', command=bt_divisao)
bt.place(x=230, y=290)

bt=Button(i, width="20", text='menos', command=bt_menos)
bt.place(x=230, y=320)

ed1 = Entry(i)
ed1.place(x=230, y=150)

ed2 = Entry(i)
ed2.place(x=230, y=180)


i.mainloop()