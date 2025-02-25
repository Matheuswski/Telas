from tkinter import*

i=Tk()
i.title("Programa financeiro")
i.geometry('980x720+250+30')

""" lb1 = Label(i, text="Login", bg="red")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e cluna(column).
lb1.place(x=1130, y=100)

lb2 = Label(i,text="SENHA", bg="blue")
lb2.place(x=1130, y=150)

ed1 = Entry(i)
ed1.place(x=1130, y=80)

ed2 = Entry(i)
ed2.place(x=1130, y=130)

bt1 = Button(i, text="Login")
bt1.place(x=950,  y=540) """

#o codigo abaixo faz correção das posições das labels, caixa de texto e botão
lb1 = Label(i, text="LOGIN", bg="yellow")
lb1.grid(row=1, column=1)

lb2 = Label(i,text="Senha", bg="red")
lb2.grid(row=2, column=1)

ed1 = Entry(i)
ed1.grid(row=1, column=2)

ed2 = Entry(i)
ed2.grid(row=2, column=2)

bt1 = Button(i, text="Login")
bt1.grid(row=3, column=1)


i.mainloop()