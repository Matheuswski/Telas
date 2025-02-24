#Comando a baixo importa tudo da bblioteca que é necessaria
#para a criação de telas. (ATERISCO significa tudo)
from tkinter import *

#i ( intanciar) recebe o objeto TK
i = Tk()
#gerar titulo da janela
i.title('Programa Financeiro')

#propriedade que altera o tamanho da janela (980 x720) e distancia da direita e topo da tela(250x30)
i.geometry('980x720+250+30')

#propriedades graficas, cor, cor de fundo da tela (bg)ou (background)
#não pode passar o i com ponto! DEVE SER i[]
i["bg"] = "black"

#CRIA O ICONE NA JANELA, VOCE DEVE TER A IMAGEM NO MESMO LOCAL DO CODIGO.
#i.wm_iconbitmap('icone.ico')

#cria label e posiciona (place). ele em relação a tela
lb = Label(i,text='Nome do usuario')
lb.place(x=100, y=100)

#cria um botão e posiciona (place) ele em relação a label.

bt = Button(i, width='20', text='Ok')
bt.place(x=230, y=100)

#gera a janela grafica
i.mainloop()