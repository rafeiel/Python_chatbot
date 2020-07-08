def saudacao(nome):
    import random
    frases = ["Olá, tudo bem?","Oi, meu nome é "+nome+" e estou aqui pra te ajudar!","Fala aí, beleza?"]
    print(nome+": "+random.choice(frases))
    
def saudacao_GUI(nome): #### GUI ####
    import random
    frases = ["Olá, tudo bem?","Oi, meu nome é "+nome+" e estou aqui pra te ajudar!","Fala aí, beleza?"]
    return random.choice(frases)
    
def recebeTexto(nome):
    texto = input("Cliente: ")
    palavrasProibidas = ["idiota","burro","maluco"]
    for i in palavrasProibidas:
        if i in texto:
            print(nome+": Qual é cara, não sou isso!")
            return recebeTexto()
        return texto

def buscaResposta(texto,nome):
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
                print(nome+": Desculpe, não entendi o que quis dizer...")
                conhecimento.write(texto)
                respostaUsuario = input(nome+": O que você esperava de resposta?\n")
                conhecimento.write("Chatbot: "+respostaUsuario+"\n")
                return "Chatbot: Huum, não sabia disso. Vou me lembrar disso!\n"
            
def buscaResposta_GUI(texto):  #### GUI ####
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
                conhecimento.write(texto)
                return "Desculpe, não entendi o que quis dizer..."

def exibeResposta(texto,resposta,nome):
    print(resposta.replace("Chatbot",nome))
    if texto == "muito obrigado":
        print(nome+": Eu que agradeço o contato. Bye!")
        return "fim"
    return "continua"

def exibeResposta_GUI(texto,resposta,nome):  #### GUI ####
    return resposta.replace("Chatbot",nome)

def salva_sugestao(sugestao):  #### GUI ####
    with open("conversa.txt","a+") as conhecimento:
         conhecimento.write("Chatbot: "+sugestao+"\n")
