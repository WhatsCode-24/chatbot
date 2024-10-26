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
        "Olá! Como eu poderia ser útil?"
    ],
    [
        [
            "onde posso achar a pagina de visualizar usuarios",
            "onde esta a pagina de visualizar usuarios",
            "como posso visualizar usuarios",
        ],
        "Você pode encontrar a página clicando no modal que aparece quando ao clicar na página de 'Visualizar usuário'."
    ],
    [
        [
            "listar areas",
            "listar area",
            "listar todas áreas",
        ],
        "Você pode listar as áreas cadastradas clicando no botão 'Áreas' na barra lateral."
    ],
    [
        [
            "onde vejo o acesso as areas",
            "onde posso ver o acesso as areas",
            "qual lugar posso verificar o acesso as areas",
            "onde poderia achar o acesso das areas",
        ],
        "Você pode entrar na pagina de 'Ultimos Acessos' para melhor visualização do acessos."
    ],

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
