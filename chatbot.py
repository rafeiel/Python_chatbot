def saudacao(nome):
    import random
    frases = ["Olá, tudo bem?","Oi, meu nome é "+nome+" e estou aqui pra te ajudar!","Fala aí, beleza?"]
    print("Chatbot: "+frases[random.randint(0,2)])
    
def recebeTexto():
    texto = input("Cliente: ")
    palavrasProibidas = ["idiota","burro","maluco"]
    for i in palavrasProibidas:
        if i in texto:
            print("Chatbot: Qual é cara, não sou isso!")
            return recebeTexto()
        return texto

def buscaResposta(texto):
    with open("conversa.txt","a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto == viu:
                    proximaLinha = conhecimento.readline()
                    if "Chatbot: " in proximaLinha:
                        return proximaLinha
                    
            else:
                print("Desculpe, não entendi o que quis dizer...")
                conhecimento.write(texto)
                respostaUsuario = input("Chatbot: O que você esperava de resposta?\n")
                conhecimento.write("Chatbot: "+respostaUsuario+"\n")
                return "Chatbot: Huum, não sabia disso. Vou me lembrar disso!\n"

def exibeResposta(texto,resposta,nome):
    print(resposta.replace("Chatbot",nome))
    if texto == "muito obrigado":
        print("Chatbot: Eu que agradeço o contato. Bye!")
        return "fim"
    return "continua"