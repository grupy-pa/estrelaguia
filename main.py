import requests
from decouple import config
from pprint import pprint
import json

from web_scraping import scraper

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [{"role": "developer", "content": ""}],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "pega_nome",
                "description": "Pega o nome completo do usuário",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "nome": {
                            "type": "string",
                            "description": "Nome completo do usuário."
                        }
                    },
                    "required": [
                        "nome"
                    ],
                    "additionalProperties": False
                },
                "strict": True
            }
        },
        {
            "type": "function",
            "function": {
                "name": "busca_horoscopo_hoje",
                "description": "Execute esta função apenas quando o usuário pedir explicitamente para saber o seu horóscopo de hoje.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "signo": {
                            "type": "string",
                            "description": "Signo do usuário, deve ser no formato minúsculo e sem acentuação. Ex: Áries → aries, Gêmeos → gemeos"
                        }
                    },
                    "required": [
                        "signo"
                    ],
                    "additionalProperties": False
                },
                "strict": True
            }
        },
        {
            "type": "function",
            "name": "gera_numero_aleatorio",
            "description": "função para gerar números inteiros aleatórios entre x e 100",
            "parameters": {
                "type": "object",
                "properties": {
                    "numero": {
                        "type": "int",
                        "description": "numero que será utilizado para definir o intervalo entre x e 100. Ex 30 e 100, 10 e 100, 1 e 100."
                    }
                },
                "required": [
                    "location"
                ],
                "additionalProperties": False
            }
        }
    ]
}

with open('instructions.txt', 'r') as file:
    instructions = file.read()
    data['messages'][0]['content'] = instructions

while True:
    try:

        user = input('$$ ')

        # Adiciona a mensagem do usuário na lista de mensagens
        data['messages'].append({"role": "user", "content": user})

        resp = requests.post(f'{api_url}/chat/completions',
                             headers=headers, json=data)
        body = resp.json()

        tool_calls = body['choices'][0]['message'].get("tool_calls")

        if (tool_calls):
            function_name = tool_calls[0]['function']['name']
            function_args = json.loads(tool_calls[0]['function']['arguments'])

            if (function_name == "pega_nome"):
                print("Simulando a manipulação do nome...")
                nome = function_args["nome"]
                nome = nome.upper()
                text = f"Olá: {nome}! Você poderia me informar qual é o seu signo?"

            elif (function_name == "busca_horoscopo_hoje"):
                signo = function_args["signo"]
                horoscopo = scraper(signo)
                text = f"{horoscopo}"
            
            elif (function_name == "gera_numero_aleatorio"):
                numero = function_args["numero"]
                print(numero)
        else:
            text = body['choices'][0]['message']['content']

        # Adiciona a resposta da modelo na lista de mensagens
        data['messages'].append({"role": "assistant", "content": text})

        print(text)

    except Exception as e:
        raise print(e)
