from tkinter import* 

i=Tk()
i.title("Programa financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i, text="Login", bg="red")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e cluna(column).
lb1.place(x=1130, y=100)

lb2 = Label(i,text="SENHA", bg="blue")
lb2.place(x=1130, y=150)

ed1 = Entry(i)
ed1.place(x=1130, y=80)

ed2 = Entry(i)
ed2.place(x=1130, y=130)

bt1 = Button(i, text="Login")
bt1.place(x=950,  y=540) 

i.mainloop()