import chatbot as bot
from tkinter import *

nome_maquina = "Ultron"
entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ""

def roda_chatbot():
    global entrada_sugestao
    global entrada_nome_usuario
    global nome_usuario
    global historico_conversa
    
    if entrada_nome_usuario:
        nome_usuario = e_mensagem.get()
        saudacao = bot.saudacao_GUI(nome_maquina)
        historico_conversa = nome_maquina+": "+saudacao+"\n"
        v.set(historico_conversa)
        entrada_nome_usuario = False
        e_mensagem.delete(0,END)
        
    else:
        texto = e_mensagem.get()
        historico_conversa += ("\n"+nome_usuario+": "+texto)
        v.set(historico_conversa)
        e_mensagem.delete(0,END)
        if texto == "vou embora":
            historico_conversa += "\n Muito obrigado pela experiência!"
            v.set(historico_conversa)
            main_window.destroy()
        
        if entrada_sugestao:
            bot.salva_sugestao(texto)
            entrada_sugestao = False
            historico_conversa += "\n Agora aprendi! Pode continuar de onde paramos!\n"
            v.set(historico_conversa)
        
        else:
            resposta = bot.buscaResposta_GUI("Cliente: "+texto+"\n")
            if resposta == "Desculpe, não entendi o que quis dizer...":
                historico_conversa += "\n Desculpe, não sei o que te responder. O que você esperava?\n"
                v.set(historico_conversa)  
                entrada_sugestao = True
            else:
                historico_conversa += "\n" + bot.exibeResposta_GUI(texto,resposta,nome_maquina)
                v.set(historico_conversa)

main_window = Tk()
main_window.title("Chatbot Ultron")
main_window.geometry("500x700+800+100")
main_window.grid()

frame = Frame(main_window)
frame.grid()

identif = Label(frame, text="Digite sua mensagem: ")
identif.grid(row=0,column=0)

e_mensagem = Entry(frame)
e_mensagem.grid(row=0,column=1)
v = StringVar()
v.set("Digite seu nome")
Label(frame, textvariable=v).grid()

button = Button(frame, text="Enviar", width=8, height=3, bg= "black", fg= "white",command=roda_chatbot)
button.grid(row=0,column=2)


main_window.mainloop() 