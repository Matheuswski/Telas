from tkinter import*

#criando uma funçao para clique no botão
def bt_click():
    #o label que usa propriedade TEXT recebera a mensagem "Trocou o texto"
    lb['text'] = "Trocou o texto"
    #esse print abaixo exibe o texto na tela do console.
    print("o botão foi clicado!")

def bt_clickar():
    #esse print exibe o texto digitado na caixa de texto e exibe na label da tela
    print(ed.get())
    lb["text"] = ed.get()

#i (instanciar) recebe o objeto Tk
i = Tk()
#gerar titulo na janela
i.title('Programa Financeiro')
i.geometry('980x720+250+39')
i["bg"]= "green"

#i.wm_iconbitmap('icone.ico')
lb = Label(i, text='Matheus Golanowski')
lb.place(x=100, y=100)

bt =Button(i,width="20", text='Ok', command=bt_click)
bt.place(x=230,y=100)

#o codigo abaixo cria um botão que posiciona abaixo do butão OK
bt = Button(i,width="20", text='Capturar', command=bt_clickar)
bt.place(x=230, y=190)

#o codigo abaixo cria a caixa de texto para digitar algo dentro
ed=Entry(i)
ed.place(x=230, y=150)

i.mainloop()