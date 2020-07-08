import chatbot as bot
nome_bot = "R2D2"
bot.saudacao(nome_bot)
while True:
    texto = bot.recebeTexto(nome_bot)
    resposta = bot.buscaResposta("Cliente: "+texto+"\n",nome_bot)
    if bot.exibeResposta(texto,resposta,nome_bot) == "fim":
        break