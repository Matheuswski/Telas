from tkinter import*

def bt_soma():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 + num2

def bt_multiplicacao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 * num2

def bt_divisao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 / num2

def bt_menos():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 - num2


i=Tk()
i.title("Programa financeiro")
i.geometry('980x720+250+30')

lb=Label(i, text="0")
lb.place(x=230, y=200)

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

lb=Label(i, text="Matheus Golanowski")
lb.place(x=400, y=380)

i.mainloop()