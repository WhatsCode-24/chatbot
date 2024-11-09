from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
nltk.download('punkt_tab')

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

trainer = ListTrainer(chatbot)

################# TREINO #################

list_training = [
    [
        [
            "oi",
            "ola",
            "oie",
            "oin",
            "salve",
            "oizinho",
        ],
        "Ola! Como eu poderia ser util?"
    ],
    [
        [
            "onde posso achar a pagina de visualizar usuarios",
            "onde esta a pagina de visualizar usuarios",
            "como posso visualizar usuarios",
        ],
        "Voce pode encontrar a pagina clicando no modal que aparece quando ao clicar na pagina de 'Gerenciar usuarios'."
    ],
    [
        [
            "listar areas",
            "listar area",
            "listar todas areas",
        ],
        "Voce pode listar as areas cadastradas clicando no botao 'Gerenciar Areas' na barra lateral."
    ],
    [
        [
            "onde vejo o acesso as areas",
            "onde posso ver o acesso as areas",
            "qual lugar posso verificar o acesso as areas",
            "onde poderia achar o acesso das areas",
        ],
        "Voce pode entrar na pagina de 'Ultimos Acessos' para melhor visualizacao dos acessos."
    ],
    [
       [
          "Como vejo o horario de funcionamento da empresa?",
          "Qual o horario de atendimento da empresa?",
          "A que horas a empresa abre e fecha?"
       ],
       "Voce pode ver o horario de funcionamento acessando o menu 'Gerenciar Empresas'. La, voce encontrara todas empresas listadas com os respectivos horarios de abertura e fechamento."
    ],
    [
       [
          "Como vejo a lista de usuarios de uma empresa?",
          "Quais usuarios estao cadastrados em uma empresa?",
          "Como saber quem sao os usuarios de uma empresa especifica?"
       ],
       "Para ver a lista de usuarios de uma empresa, va em 'Gerenciar Empresas', la, voce encontrara todos os usuarios listados"
    ],
    [
       [
          "Quais cameras estao instaladas em um comodo?",
          "Como vejo as cameras disponiveis em um comodo especifico?",
          "Onde encontro as cameras de um determinado local?"
       ],
       "Va ate 'Gerenciar Areas' e selecione o comodo desejado para visualizar as imagens das cameras."
    ],
    [
       [
          "Como vejo as portas de um comodo?",
          "Quais portas estao instaladas em um determinado comodo?",
          "Onde posso ver as portas de um comodo especifico?"
       ],
       "Para ver as portas de um comodo, acesse 'Gerenciar Areas'. La estarao listadas as portas instaladas."
    ],
    [
       [
          "Onde vejo os detalhes dos acessos em um comodo?",
          "Como posso acessar o historico de acessos de um comodo?",
          "Quais informacoes estao disponiveis sobre acessos em um comodo?"
       ],
       "No menu, va ate 'Gerenciar Acessos', la estarao listados os detalhes dos acessos"
    ],
    [
       [
          "Como saber o nivel de acesso de um usuario?",
          "Qual o nivel de permissao de um usuario?",
          "Como posso ver as permissoes de um usuario especifico?"
       ],
       "No menu 'Gerenciar Usuarios', selecione o usuario para visualizar o nivel de acesso e suas permissoes no sistema."
    ],
    [
       [
          "Como vejo os dados de um usuario?",
          "Onde encontro as informacoes de contato de um usuario?",
          "Como acessar o perfil de um usuario especifico?"
       ],
       "Acesse 'Gerenciar Usuarios' no menu, la estarao listados os dados de contato e outras informacoes de usuario."
    ],
    [
       [
          "Como posso ver as informacoes da empresa?",
          "Quais sao os detalhes de uma empresa cadastrada?",
          "Onde vejo o endereco e contato de uma empresa?"
       ],
       "No menu va em 'Gerenciar Empresas', la existe uma lista com as informacoes de todas empresas cadastradas como endereco, telefone e horarios de funcionamento."
    ],
    [
       [
          "Como vejo os comodos de uma empresa?",
          "Onde posso encontrar informacoes sobre os comodos de uma empresa?",
          "Como acessar a lista de comodos de uma empresa?"
       ],
       "No menu va em 'Gerenciar Areas', la existe uma lista com todos os comodos cadastrados."
    ],
    [
       [
          "Quem acessou uma porta recentemente?",
          "Como vejo o historico de acessos de uma porta?",
          "Quais foram os ultimos acessos registrados em uma porta?"
       ],
       "Para ver o historico de acessos de uma porta, va em 'Gerenciar Acessos', la existe uma lista com todos os registros de acessos."
    ],
    [
       [
          "Quem pode acessar um comodo especifico?",
          "Quais usuarios tem permissao para entrar em um determinado comodo?",
          "Como vejo as permissoes de acesso de um comodo?"
       ],
       "Va ate 'Gerenciar Acessos' para ver quem tem permissao de acesso em cada comodo. La voce podera configurar e visualizar as permissoes dos usuarios."
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
           "Valeu pela assistencia"
        ],
        "De nada! Estou aqui para ajudar. Se precisar de mais alguma coisa, e so chamar!"
     ]
]

 

for treino in list_training:
    for frase in treino[0]:
        trainer.train([frase, treino[1]]) 



################# ROTAS #################



@app.route('/chatbot', methods=['POST'])
def chatbot_answer():
    data = request.get_json()
    query = data.get('query')
    response = str(chatbot.get_response(query))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
