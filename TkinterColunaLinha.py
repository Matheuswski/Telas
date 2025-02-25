from tkinter import*

i=Tk()
i.title("Programa financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i, text="Login", bg="red")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e cluna(column).
lb1.grid(row=3, column=1)

lb2 = Label(i,text="SENHA", bg="blue")
lb2.grid(row=1, column=1)

ed1 = Entry(i)
ed1.grid(row=3, column=1)

ed2 = Entry(i)
ed2.grid(row=2, column=1)

bt1 = Button(i, text="Login")
bt1.grid(row=5, column=3)

i.mainloop()