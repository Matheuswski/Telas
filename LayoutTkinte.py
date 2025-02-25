from tkinter import*
i=Tk()
i.title("Programa financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i, text='Label 1', bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i, text='Label 1', bg="pink")
lb2.place(x=230,y=200)

lb3 = Label(i, text='Label 1', bg="green")
lb3.place(x=230,y=200)

lb4 = Label(i, text='Label 1', bg="red")
lb4.place(x=230,y=200)


""" lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack() """

""" # o codigo abaixo é resposavel em posicionar o label na parte de cima
lb1.pack(side="top")
# o codigo abaixo é responsavel por posicionar a esquerda
lb2.pack(side="left")
# o codigo abaixo é responsavel por posicionar a direita
lb3.pack(side="right")
# o codigo abaixo é resposavel em posicionar o label na parte de baixo
lb4.pack(side="bottom")
 """
""" #o codigo abaixo é resposavel em posicionar o label na parte de cima
lb1.pack(side="left")
#o codigo abaixo é responsavel por posicionar a esquerda
lb2.pack(side="left")
#o codigo abaixo é responsavel por posicionar a direita
lb3.pack()
#o codigo abaixo é resposavel em posicionar o label na parte de baixo
lb4.pack() """


i.mainloop()