from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import mac_morpho
from nltk.metrics import edit_distance
from collections import Counter


nltk.download('punkt_tab')
nltk.download('stopwords')  # Para obter stopwords
nltk.download('mac_morpho')

palavras = [palavra.lower() for palavra in mac_morpho.words()]
vocabulario = set(palavras)
frequencias = Counter(palavras)

app = Flask(__name__)

from chatterbot import ChatBot

chatbot = ChatBot(
    'Training Example',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri="mongodb+srv://whatscode:root123@chatbotwc.nbegg.mongodb.net/chatbot?retryWrites=true&w=majority&appName=chatbotWC",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe, não entendi. Me faça outro questionamento por favor.',
            'maximum_similarity_threshold': 0.50
        }
    ],
    read_only=True
)

# Treinamento do chatbot
if __name__ == "__main__":

   trainer = ListTrainer(chatbot)

   ################# TREINO #################

   list_training = [
    [
        [
            "oi",
            "olá",
        ],
        "Olá! Como eu poderia ser útil?"
    ],
    [
        [
            "onde posso achar a página de visualizar usuários",
            "onde está a página de visualizar usuários",
            "como posso visualizar usuários",
        ],
        "Você pode encontrar a página clicando no modal que aparece ao clicar na página de 'Gerenciar usuários'."
    ],
    [
        [
            "listar áreas",
            "listar área",
            "listar todas áreas",
        ],
        "Você pode listar as áreas cadastradas clicando no botão 'Gerenciar Áreas' na barra lateral."
    ],
    [
        [
            "onde vejo o acesso às áreas",
            "onde posso ver o acesso às áreas",
            "qual lugar posso verificar o acesso às áreas",
            "onde poderia achar o acesso das áreas",
        ],
        "Você pode entrar na página de 'Últimos Acessos' para melhor visualização dos acessos."
    ],
    [
        [
            "Como vejo o horário de funcionamento da empresa?",
            "Qual o horário de atendimento da empresa?",
            "A que horas a empresa abre e fecha?"
        ],
        "Você pode ver o horário de funcionamento acessando o menu 'Gerenciar Empresas'. Lá, você encontrará todas as empresas listadas com os respectivos horários de abertura e fechamento."
    ],
    [
        [
            "Como vejo a lista de usuários de uma empresa?",
            "Quais usuários estão cadastrados em uma empresa?",
            "Como saber quem são os usuários de uma empresa específica?"
        ],
        "Para ver a lista de usuários de uma empresa, vá em 'Gerenciar Empresas'. Lá, você encontrará todos os usuários listados."
    ],
    [
        [
            "Quais câmeras estão instaladas em um cômodo?",
            "Como vejo as câmeras disponíveis em um cômodo específico?",
            "Onde encontro as câmeras de um determinado local?"
        ],
        "Vá até 'Gerenciar Áreas' e selecione o cômodo desejado para visualizar as imagens das câmeras."
    ],
    [
        [
            "Como vejo as portas de um cômodo?",
            "Quais portas estão instaladas em um determinado cômodo?",
            "Onde posso ver as portas de um cômodo específico?"
        ],
        "Para ver as portas de um cômodo, acesse 'Gerenciar Áreas'. Lá estarão listadas as portas instaladas."
    ],
    [
        [
            "Onde vejo os detalhes dos acessos em um cômodo?",
            "Como posso acessar o histórico de acessos de um cômodo?",
            "Quais informações estão disponíveis sobre acessos em um cômodo?"
        ],
        "No menu, vá até 'Gerenciar Acessos'. Lá estarão listados os detalhes dos acessos."
    ],
    [
        [
            "Como saber o nível de acesso de um usuário?",
            "Qual o nível de permissão de um usuário?",
            "Como posso ver as permissões de um usuário específico?"
        ],
        "No menu 'Gerenciar Usuários', selecione o usuário para visualizar o nível de acesso e suas permissões no sistema."
    ],
    [
        [
            "Como vejo os dados de um usuário?",
            "Onde encontro as informações de contato de um usuário?",
            "Como acessar o perfil de um usuário específico?"
        ],
        "Acesse 'Gerenciar Usuários' no menu. Lá estarão listados os dados de contato e outras informações do usuário."
    ],
    [
        [
            "Como posso ver as informações da empresa?",
            "Quais são os detalhes de uma empresa cadastrada?",
            "Onde vejo o endereço e contato de uma empresa?"
        ],
        "No menu, vá em 'Gerenciar Empresas'. Lá existe uma lista com as informações de todas as empresas cadastradas, como endereço, telefone e horários de funcionamento."
    ],
    [
        [
            "Como vejo os cômodos de uma empresa?",
            "Onde posso encontrar informações sobre os cômodos de uma empresa?",
            "Como acessar a lista de cômodos de uma empresa?"
        ],
        "No menu, vá em 'Gerenciar Áreas'. Lá existe uma lista com todos os cômodos cadastrados."
    ],
    [
        [
            "Quem acessou uma porta recentemente?",
            "Como vejo o histórico de acessos de uma porta?",
            "Quais foram os últimos acessos registrados em uma porta?"
        ],
        "Para ver o histórico de acessos de uma porta, vá em 'Gerenciar Acessos'. Lá existe uma lista com todos os registros de acessos."
    ],
    [
        [
            "Quem pode acessar um cômodo específico?",
            "Quais usuários têm permissão para entrar em um determinado cômodo?",
            "Como vejo as permissões de acesso de um cômodo?"
        ],
        "Vá até 'Gerenciar Acessos' para ver quem tem permissão de acesso em cada cômodo. Lá você poderá configurar e visualizar as permissões dos usuários."
    ],
    [
        [
            "Obrigado",
            "Valeu",
            "Obrigada",
            "Muito obrigado",
            "Agradecido",
            "Agradecida",
            "Obrigado pela ajuda",
            "Valeu pela assistência"
        ],
        "De nada! Estou aqui para ajudar. Se precisar de mais alguma coisa, é só chamar!"
    ]
]


   

   for treino in list_training:
      for frase in treino[0]:
         trainer.train([frase, treino[1]]) 



################# ROTAS #################
# Obter as stopwords em português
print(type(stopwords.words('portuguese')))
stop_words = stopwords.words('portuguese') + ['um', 'uma','de','da', 'do', 'o', 'a']
stop_words = set(stop_words)

def corrigir_ou_validar(palavra, vocabulario):

    if palavra in vocabulario:
        return palavra  # Palavra já está correta
    else:
        # Encontrar a palavra mais próxima com base na distância de edição
        sugestao = min(vocabulario, key=lambda v: edit_distance(palavra, v))
        return sugestao

@app.route('/chatbot', methods=['POST'])
def chatbot_answer():
    data = request.get_json()
    query = data.get('query')

    # Tokenizar a entrada do usuário
    tokens = word_tokenize(query, language='portuguese')
    listwords = []
    for palavra in tokens:
      resultado = corrigir_ou_validar(palavra.lower(), vocabulario)
      listwords.append(resultado)
      
    # Remover as stopwords
    palavras_sem_stopwords = [word for word in listwords if word.lower() not in stop_words]
    # Obter a resposta do chatbot
    response = str(chatbot.get_response(" ".join(palavras_sem_stopwords)))
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=False)
