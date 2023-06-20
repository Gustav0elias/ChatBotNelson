from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json
import random

DADOS_DE_TREINO = ['arquivosJson/perguntas.json', 'arquivosJson/saudaçoes.json']

def iniciar():
    nelson = ChatBot("Nelson - IA", read_only=True)
    return nelson

def treino(instancia):
    treino = ListTrainer(instancia)
    conversa = []

    for dados in DADOS_DE_TREINO:
        with open(dados, 'r', encoding='utf-8') as arq:
            try:
                dadosJson = json.load(arq)
                conversa.append(dadosJson['conversas'])
            except:
                print(f"Ocorreu um erro ao carregar o arquivo json com os dados: {dados}")
            finally:
                arq.close()
    
    for dados in conversa:
        for perguntas_respostas in dados:
            perguntas = perguntas_respostas['pergunta']
            resposta = perguntas_respostas['resposta']
            for pergunta in perguntas:
                treino.train([pergunta, resposta])

def loop(instancia):
    while True:
        print('---------------pergunta-----------------')
        entrada = input("Converse com o assistente Virtual Nelson: ")
        botResposta = instancia.get_response(entrada.lower())
        if botResposta.confidence > 0.7:
            print('---------------resposta-----------------')
            print('Assistente Nelson: ', botResposta.text)
        else:
            n_reconheceu = ['não tenho certeza da resposta', 'não consegui entender', 'para uma melhor compreensão, você oderia digitar novamente?']
            print(random.choice(n_reconheceu))

if __name__ == "__main__":
    nelson= iniciar()
    treino(nelson)
    loop(nelson)
