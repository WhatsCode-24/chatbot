
# Instruções para Rodar o Chatbot

Siga os passos abaixo para configurar e rodar o chatbot.

## 1. Criação do Ambiente Virtual

Execute o seguinte comando para criar um ambiente virtual:

```bash
py -m venv venv
```

## 2. Ativação do Ambiente Virtual

Ative o ambiente virtual com o comando:

```bash
venv\Scripts\activate
```

## 3. Instalação das Dependências

Instale as dependências do projeto usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 4. Execução do Chatbot

Por fim, execute o chatbot com o seguinte comando:

```bash
flask run
```

## Observações

- Certifique-se de que o Python e o Flask estão instalados corretamente.
- O MongoDB deve estar configurado e acessível conforme especificado na configuração do chatbot.
