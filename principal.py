import tkinter
from tkinter import *
from tkinter import ttk
import pandas as pd
import win32com.client as win32

#Cores
co0 = "#FFFFFF" #Branco
co1 = "#222222"
co2 = "#FFFF00" #Amarelo
co3 = "#000080" #Azul
co4 = "#00FFFF" #Blue
co5 = "#2F4F4F" #Dark Gray
co6 = "#C0C0C0" #Cinza
co7= "#FF0000" #Red 
fundo = "#000" #Black

# criando janela principal
janela = Tk()
janela.title("Jogo da Velha")
janela.geometry("260x370")
janela.configure(bg=fundo)

#Dividindo a janela em 2 frames
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

  #Criando o Frame de cima
app_x = Label(frame_cima, text="X", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=co1, fg=co7)
app_x.place(x=25, y=10)

app_x = Label(frame_cima, text="Jogador 1", height=1, relief="flat", anchor="center", font=("Ivy 7 bold"), bg=co1, fg=co0)
app_x.place(x=17, y=70)

app_x_pontos = Label(frame_cima, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=":", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_separador.place(x=110, y=20)

app_y = Label(frame_cima, text="O", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=co1, fg=co3)
app_y.place(x=170, y=10)

app_y = Label(frame_cima, text="Jogador 2", height=1, relief="flat", anchor="center", font=("Ivy 7 bold"), bg=co1, fg=co0)
app_y.place(x=165, y=70)

app_y_pontos = Label(frame_cima, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_y_pontos.place(x=130, y=20)


#Criando a lógica
jogador_1 = "X"
jogador_2 = "O"

score_1 = 0;
score_2 = 0;

tabela = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

jogando = "X"
joga = ""
contador = 0
contador_de_rodada = 0

def iniciar_jogo():
  b_play.place(x=800, y=350)
  #controlar jogo
  def controlar_jogo(i):
    global jogando
    global contador
    global jogar
    
    #comparando valor recebido
    if i == str(1):
      #verificando se a posição esta vazia
      if b_0['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_0["fg"] = cor
        b_0["text"] = jogando
        tabela[0][0] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == "X":
          jogando = "O"
          joga = "Jogador 1"
        else:
          jogando = "X"
          joga = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
            
    if i == str(2):
      #verificando se a posição esta vazia
      if b_1['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_1["fg"] = cor
        b_1["text"] = jogando
        tabela[0][1] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
            
    if i == str(3):
      #verificando se a posição esta vazia
      if b_2['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_2["fg"] = cor
        b_2["text"] = jogando
        tabela[0][2] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
        #incrementando contador
        contador += 1
            
    if i == str(4):
      #verificando se a posição esta vazia
      if b_3['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_3["fg"] = cor
        b_3["text"] = jogando
        tabela[1][0] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
                
    if i == str(5):
      
      #verificando se a posição esta vazia
      if b_4['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_4["fg"] = cor
        b_4["text"] = jogando
        tabela[1][1] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
          
    if i == str(6):
      
      #verificando se a posição esta vazia
      if b_5['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_5["fg"] = cor
        b_5["text"] = jogando
        tabela[1][2] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
            
    if i == str(7):
      
      #verificando se a posição esta vazia
      if b_6['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_6["fg"] = cor
        b_6["text"] = jogando
        tabela[2][0] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
            
    if i == str(8):
      
      #verificando se a posição esta vazia
      if b_7['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_7["fg"] = cor
        b_7["text"] = jogando
        tabela[2][1] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
          
    if i == str(9):
      
      #verificando se a posição esta vazia
      if b_8['text'] == '':
        #Verificando quem esta jogando
        if jogando == "X":
          cor = co7
        if jogando == "O":
          cor = co3
            
        #Definindo a cor do texto do botão e marcando posição com o valor do jogador atual
        b_8["fg"] = cor
        b_8["text"] = jogando
        tabela[2][2] = jogando
        
        #verificando quem esta jogando, alterando jogador
        if jogando == 'X':
          jogando = "O"
          jogar = "Jogador 1"
        else:
          jogando = "X"
          jogar = "Jogador 2"
          
          
        #incrementando contador
        contador += 1
        
        
    #Apos contador maior de 5, verificar se houve vencedor
    if contador >= 5:
      #linhas
      if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
        vencedor_jogo(jogando)
      elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
        vencedor_jogo(jogando)
      elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
        vencedor_jogo(jogando)
            
      #colunas
      if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
        vencedor_jogo(jogando)
      elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
        vencedor_jogo(jogando)
      elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
        vencedor_jogo(jogando)
          
      #Diagonais      
      if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
        vencedor_jogo(jogando)
      elif tabela[0][2] == tabela[1][1] == tabela [2][0] != "":
        vencedor_jogo(jogando)
              
      #Empate
      if contador >= 9:
        vencedor_jogo("Empate")    
                
  #decidir vencedor
  def vencedor_jogo(i):
    global tabela
    global score_1
    global score_2
    global contador_de_rodada
    global contador
    
    #Bloquar botões
    b_0["state"] = "disable"
    b_1["state"] = "disable"
    b_2["state"] = "disable"
    b_3["state"] = "disable"
    b_4["state"] = "disable"
    b_5["state"] = "disable"
    b_6["state"] = "disable"
    b_7["state"] = "disable"
    b_8["state"] = "disable"
    
    #Vencedor
    app_vencedor = Label(frame_baixo, text="", width=20, height=1, font=('Ivy 10 bold'), relief='raised', bg=co3, fg=fundo)
    app_vencedor.place(x=55, y=88)
    
    if i == "X":
      score_2 += 1
      app_vencedor["text"] = "Jogador 2 Venceu"
      app_y_pontos["text"] = score_2
      app_vencedor["fg"] = co0
      
    if i == "O":
      score_1 += 1
      app_vencedor["text"] = "Jogador 1 Venceu"
      app_vencedor["bg"] = co7
      app_vencedor["fg"] = co0
      app_x_pontos["text"] = score_1
            
    if i == "Empate":
      app_vencedor["text"] = "Empate"
      app_vencedor["bg"] = co2
      app_vencedor["fg"] = fundo
      
    def start():
        #Limpando botões
      b_0["text"] = ""
      b_1["text"] = ""
      b_2["text"] = ""
      b_3["text"] = ""
      b_4["text"] = ""
      b_5["text"] = ""
      b_6["text"] = ""
      b_7["text"] = ""
      b_8["text"] = ""
            
      b_0["state"] = "normal"
      b_1["state"] = "normal"
      b_2["state"] = "normal"
      b_3["state"] = "normal"
      b_4["state"] = "normal"
      b_5["state"] = "normal"
      b_6["state"] = "normal"
      b_7["state"] = "normal"
      b_8["state"] = "normal"  

      app_vencedor.destroy()
      b_play.destroy()
      
      #Botão Play
    b_play = Button(frame_baixo, command=start, text="Próxima Rodada", width=15, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
    b_play.place(x=65, y=197)

    def final_jogo():
        b_play.destroy()
        app_vencedor.destroy()
        
        terminar_jogo()      
      
    if contador_de_rodada >=5:
      final_jogo()
    else:
      contador_de_rodada += 1 
      #Reiniciando a tabela
      tabela = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
      contador = 0
      
  #terminar jogo
  def terminar_jogo():
    global tabela
    global contador_de_rodada
    global score_1
    global score_2
    global contador

    
    tabela = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    contador_de_rodada = 0
    score_1 = 0
    score_2 = 0
    contador = 0
    
    b_0["state"] = "disable"
    b_1["state"] = "disable"
    b_2["state"] = "disable"
    b_3["state"] = "disable"
    b_4["state"] = "disable"
    b_5["state"] = "disable"
    b_6["state"] = "disable"
    b_7["state"] = "disable"
    b_8["state"] = "disable"
    
    
    app_fim = Label(frame_baixo, text="Fim de Jogo", width=20, height=1, font=('Ivy 10 bold'), relief='raised', bg=co0, fg=fundo)
    app_fim.place(x=65, y=88)
    
    #Jogar de novo
    def jogar_navamente():
      app_x_pontos["text"] = "0"
      app_y_pontos["text"] = "0"
      app_fim.destroy()
      b_play.destroy()
      
      #Chamando função iniciar jogo
      iniciar_jogo()
      
      #Botão Play
    b_play = Button(frame_baixo, command=jogar_navamente, text="PLAY", width=10, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
    b_play.place(x=80, y=197)

  #Botões linha 1
  b_0 = Button(frame_baixo, command=lambda: controlar_jogo('1'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_0.place(x=30, y=15)

  b_1 = Button(frame_baixo, command=lambda: controlar_jogo('2'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_1.place(x=98, y=15)

  b_2 = Button(frame_baixo, command=lambda: controlar_jogo('3'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_2.place(x=168, y=15)

  #Botões linha 2
  b_3 = Button(frame_baixo, command=lambda: controlar_jogo('4'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_3.place(x=30, y=73)

  b_4 = Button(frame_baixo, command=lambda: controlar_jogo('5'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_4.place(x=98, y=73)

  b_5 = Button(frame_baixo, command=lambda: controlar_jogo('6'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_5.place(x=168, y=73)

  #Botões linha 3
  b_6 = Button(frame_baixo, command=lambda: controlar_jogo('7'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_6.place(x=30, y=133)

  b_7 = Button(frame_baixo, command=lambda: controlar_jogo('8'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_7.place(x=98, y=133)

  b_8 = Button(frame_baixo, command=lambda: controlar_jogo('9'), text="", width=3, padx=8, pady=4, relief="flat", font=('Ivy 15 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
  b_8.place(x=168, y=133)


  #Linhas verticais
  app_ = Label(frame_baixo, text="", height=25, relief="flat",pady=5, anchor="center", font=('Ivy 4 bold'), bg=co5, fg=co7)
  app_.place(x=90, y=15)

  app_ = Label(frame_baixo, text="", height=25, relief="flat",pady=5, anchor="center", font=('Ivy 4 bold'), bg=co5, fg=co7)
  app_.place(x=160, y=15)


  #Linhas horizontais
  app_ = Label(frame_baixo, text="", width=188, relief="flat",padx=2, anchor="center", font=('Ivy 1 bold'), bg=co5, fg=co7)
  app_.place(x=30, y=63)

  app_ = Label(frame_baixo, text="", width=188, relief="flat",padx=2, anchor="center", font=('Ivy 1 bold'), bg=co5, fg=co7)
  app_.place(x=30, y=123)


#Botão Play
b_play = Button(frame_baixo, command=iniciar_jogo, text="PLAY", width=10, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
b_play.place(x=85, y=210)

janela.mainloop()