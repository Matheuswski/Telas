from tkinter import*

i=Tk()
i.title("Programa financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i, text='Label 1', bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i, text='Label 2', bg="pink")
lb2.place(x=230,y=200)

lb3 = Label(i, text='Label 3', bg="green")
lb3.place(x=230,y=200)

lb4 = Label(i, text='Label 4', bg="red")
lb4.place(x=230,y=200)

""" lb1.pack(side=TOP,fill=X) #comando FILL e responsavel do preenchimento 100%, deve usar x para horizontal deve ser maisuculo
lb2.pack(side=RIGHT,fill=Y)
lb3.pack(side=LEFT,fill=Y) #comando FILL e responsavel do preenchimento 100%, deve usar x para VERTICAL deve ser maisuculo
lb4.pack(side=BOTTOM,fill=X) """

lb1.pack(side=TOP,fill=BOTH,expand=1) 
lb2.pack(side=TOP,fill=BOTH,expand=1)
lb3.pack(side=TOP,fill=BOTH,expand=1) 
lb4.pack(side=TOP,fill=BOTH,expand=1)


i.mainloop()