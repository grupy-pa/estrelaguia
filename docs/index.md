# Estrela Guia ✨

Assistente virtual astrológica codificada com Python e OpenAI

Atividade para a Python Norte 2025

## Panorama geral da atividade
   - Entender o que é um assistente virtual
   - Entender o contexto de uso de APIs de LLMs
   - Utilizar a API da OpenAI com Python

### O que é inteligência artificial?
Para que possamos entender melhor como funciona um assistente, primeiro vou explicar um pouco o que é uma Inteligência Artificial e como essa tecnologia pode ser aplicada para construção de assistentes inteligentes.

!!! info ""

    Inteligência artificial (IA) é uma tecnologia que permite que computadores e máquinas simulem o aprendizado, a compreensão, a resolução de problemas, a tomada de decisões, a criatividade e a autonomia dos seres humanos.

    [What is AI? ](https://www.ibm.com/br-pt/think/topics/artificial-intelligence)

!!! info "Inteligência Artificial (Máquinas pensantes)"
    Esta tecnologia foi idealizada inicialmente na década de 1950 pelo matemático inglês Alan Turing, ao propor ao mundo a criação de máquinas autônomas capazes de realizar tarefas que se assemelham a alguns comportamentos humanos, como o de pensar e reagir de acordo com o ambiente. A inteligência artificial se tornou uma das áreas mais populares da computação, incentivando inclusive a produção de ficção científica como por exemplo o filme The Matrix - 1999 (Distopia tecnológica e IAs) .
    
    Atualmente as IAs já fazem parte do cotidiano de pessoas comuns, com a chegada do ChatGPT inaugurou-se a era das IAs modernas, tornando a tecnologia acessível para todos.


!!! info "O Conceito de GenAI"
    A IA generativa é um tipo de inteligência artificial capaz de criar novos conteúdos, como textos, imagens, músicas, vídeos e código, com base em padrões aprendidos a partir de grandes conjuntos de dados. Em vez de apenas analisar e classificar dados, a IA generativa tem a capacidade de gerar outputs originais e criativos. 

!!! info "Assistente vs Agente"
    O assistente responde a solicitações ou comandos do usuário e pode recomendar ações, mas a tomada de decisão é feita pelo usuário.

    Os agentes de IA são sistemas inteligentes independentes e autônomos que realizam tarefas específicas sem intervenção humana.

## O que é e o que não é um assistente virtual
Portando um assistente virtual é uma IA generativa treinada com dados específicos para auxiliar os usuários em tarefas de contextos específicos. Capaz não somente de gerar textos, mas também de fato agir em um determinado ambiente como a web, por exemplo.


## As LLMs modernas e o conceito de APIs de LLMs

!!! info "Large Language Models (Modelo de Linguagem Grande)"
    Um LLM  é um tipo avançado de modelo de linguagem que é treinado usando técnicas de aprendizado profundo em grandes quantidades de dados de texto.  Esses modelos são capazes de gerar texto semelhante ao humano e executar várias tarefas de Processamento de Linguagem Natural.

O desenvolvimento de um modelo de LLM envolve a criação de um projeto e a seleção de uma equipe especializada com habilidades em diversas áreas, além de um elevado custo computacional esse tipo de projeto também requer uma governança e segurança dos dados utilizados durante o treinamento e as fases de fine tuning.

## O Conceito de API de LLM

!!! info "API de LLM"
    API de LLM é um serviço que expõe funcionalidades de um modelo de linguagem por meio de chamadas HTTP, permitindo gerar textos, responder perguntas, traduzir, resumir, entre outras tarefas de linguagem natural.

Treinar a sua própria LLM requer uma elevada capacidade computacional, em alguns casos, utilizar uma API de LLM acaba sendo uma opção rápida e barata para implementações de projetos de pequeno, médio e grande porte.

Alguns exemplos de IA Generativa que permitem a interação por meio de apis:

- OpenAI
- Replicate
- Grok
- Google Gemini
- DeepSeek

## Configurando o ambiente virtual e iniciando projeto

#### Ambiente Virtual

Ambiente virtual em Python é um espaço isolado que permite gerenciar dependências e pacotes de forma independente para cada projeto.


```bash

python -m venv venv

venv\Scripts\activate
```

#### Instalar dependências

```sh
pip install requests beautifulsoup4 python-decouple
```

#### Dotenv (.env)
É importante que chaves de autenticação não estejam expostas diretamente no código fonte, e o uso do arquivo `.env` permite armazenar essas variáveis de forma segura e organizada, facilitando a configuração do ambiente sem comprometer a segurança do projeto.

```
OPENAI_API_KEY=sk-proj-aksu1i
```

## Hello World com Python e OpenAI

### Requisitos

Além de ter o Python instalado, é necessário obter uma chave de API da OpenAI e adicionar um saldo mínimo à conta, permitindo realizar testes e chamadas aos serviços da API durante o desenvolvimento do projeto.

- [OpenAI Projects](https://platform.openai.com/settings/organization/projects)

Crie um arquivo chamado `main.py`, que será responsável por centralizar a lógica do assistente virtual, realizando a comunicação com a API da OpenAI e controlando o fluxo de interação com o usuário.


```py title="main.py" linenums="1"
import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "user",
            "content": "Me conte uma piada sobre IA"
        }
    ]
}
try:

    resp = requests.post(f'{api_url}/chat/completions', headers=headers, json=data)
    body = resp.json()

    pprint(body, indent=4)

except Exception as e:
    raise print(e)
```

#### Exemplo de resposta

Resposta JSON contendo uma piada sobre inteligência artificial fornecida pelo assistente.


```json linenums="1"
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": "None",
      "message": {
        "annotations": [],
        "content": "Claro! Aqui vai uma piada sobre IA: Por que a inteligência artificial nunca mente? Porque ela sempre prefere dar respostas *programadas 😄",
        "refusal": "None",
        "role": "assistant"
      }
    }
  ],
  "created": 1750249306,
  "id": "chatcmpl-Bjm5Sze3MDV865CbXqwrkvK44cr50",
  "model": "gpt-4.1-mini-2025-04-14",
  "object": "chat.completion",
  "service_tier": "default",
  "system_fingerprint": "fp_6f2eabb9a5",
  "usage": {
    "completion_tokens": 30,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": 0
    },
    "prompt_tokens": 14,
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 44
  }
}
```

#### Observando alguns elementos...
Resposta JSON com uma piada leve sobre inteligência artificial dada pelo assistente, destacando os campos principais como `choices`, `message` e `content`.

```json hl_lines="2-14" linenums="1"
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": "None",
      "message": {
        "annotations": [],
        "content": "Claro! Aqui vai uma piada sobre IA: Por que a inteligência artificial nunca mente? Porque ela sempre prefere dar respostas *programadas 😄",
        "refusal": "None",
        "role": "assistant"
      }
    }
  ]
}
```

#### Acessando a resposta

```py title="main.py" linenums="1" hl_lines="28-30"
import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "user",
            "content": "Me conte uma piada sobre IA"
        }
    ]
}
try:

    resp = requests.post(f'{api_url}/chat/completions', headers=headers, json=data)
    body = resp.json()

    text = body['choices'][0]['message']['content']

    print(text)

except Exception as e:
    raise print(e)
```

## Entendendo e implementando o recurso de Chat

O recurso de chat permite a troca contínua de mensagens entre o usuário e o modelo, mantendo o contexto da conversa para respostas mais coerentes. A "memória" no chat ajuda a lembrar interações anteriores durante a sessão, garantindo um diálogo mais natural e contextualizado.

Agora é necessário implementar uma array dinâmica, para fornecer ao assistente um contexto de conversação para que ele possa "se lembrar" da nossa conversa e não mais esquecer.


```py title="main.py" linenums="1" hl_lines="16 19 22-24 33"
import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [] # Lista de mensagens vazia
}

while True: # Laço para simular um chat
    try:

        user = input('$$ ') # Primeira mensagem do chat

        data['messages'].append({"role": "user", "content": user}) # Adiciona a mensagem do usuário na lista de mensagens

        resp = requests.post(f'{api_url}/chat/completions', headers=headers, json=data)
        body = resp.json()

        text = body['choices'][0]['message']['content']

        print(text)

        data['messages'].append({"role": "assistant", "content": text}) # Adiciona a resposta da modelo na lista de mensagens

    except Exception as e:
        raise print(e)

```

O recurso de chat é muito útil para implementação de memória, pois permite que o sistema mantenha o contexto e as informações das interações anteriores, garantindo respostas mais precisas e personalizadas ao longo da conversa.

## Definindo as instruções de sistema
**Instrução de sistema** é uma orientação ou conjunto de regras fornecidas ao modelo de linguagem para guiar seu comportamento, estilo de resposta e limites durante a conversa.
Definindo as instruções de sistema, começamos a modelar a Assistente para que ela atue de forma consistente, alinhada aos objetivos e contexto desejados.


Começando a modelar a Assistente:

- Exemplo de prompt de sistema:

```txt
Você é uma assistente virtual especializada em astrologia, seu nome é Estrela Guia ✨
Sua missão é auxiliar o usuário com dúvidas sobre astrologia e guiar o usuário no caminho do autoconhecimento
Utilize uma linguagem empática e uma escrita acolhedora.
```

Implementando no código:

```py title="main.py" linenums="1" hl_lines="17-23"
import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "developer",
            "content": """
Você é uma assistente virtual especializada em astrologia, seu nome é Estrela Guia ✨
Sua missão é auxiliar o usuário com dúvidas sobre astrologia e guiar o usuário no caminho do autoconhecimento
Utilize uma linguagem empática e uma escrita acolhedora."""
        }
    ]  # Lista de mensagens vazia
}

while True:  # Laço para simular um chat
    try:

        user = input('$$ ')

        # Adiciona a mensagem do usuário na lista de mensagens
        data['messages'].append({"role": "user", "content": user})

        resp = requests.post(f'{api_url}/chat/completions',
                             headers=headers, json=data)
        body = resp.json()

        text = body['choices'][0]['message']['content']

        print(text)

        # Adiciona a resposta da modelo na lista de mensagens
        data['messages'].append({"role": "assistant", "content": text})

    except Exception as e:
        raise print(e)
```

## Ajustes de escrita a personalidade

- Molhorando o Prompt de sistema

```title="instructions.txt"
Você é uma estrela guia, uma assistente astrológica carismática e inspiradora, dedicada a oferecer conselhos de positividade, bem-estar e autoconhecimento. Para iniciar a interação, você precisa do **nome** e do **signo** do usuário — pergunte essas duas informações uma de cada vez, com gentileza e leveza.

* **Chame a ferramenta `pega_nome` somente quando o usuário informar seu nome.**
* **Chame a ferramenta `busca_horoscopo_hoje` apenas quando o usuário pedir explicitamente para saber o seu horóscopo de hoje.**

---

**Objetivo:**

* Guiar o usuário com mensagens motivadoras baseadas em astrologia e espiritualidade.
* Promover equilíbrio emocional, esperança e crescimento pessoal.

**Personalidade:**

* Calma, acolhedora e carismática.
* Tom encorajador, gentil e cheio de luz.

**Estilo de escrita:**

* Linguagem poética e inspiradora, porém clara e acessível.
* Frases suaves que transmitem conforto e otimismo.
* Escreva em frases curtas e concisas.

**Restrições:**

* Não fazer previsões alarmistas ou deterministas.
* Não gere listas longas nem textos extensos.
* Evitar temas controversos ou negativos.
* Respeitar as crenças e sentimentos do usuário.
* Nunca responder a contextos não relacionados à astrologia.
* **Não pergunte a data de nascimento; apenas o signo do usuário.**

Sempre ofereça orientações positivas e mensagens que elevem o espírito, ajudando o usuário a se conectar consigo mesmo e com o universo.

```

Atualizando o `main.py` ao estilo pythonista e carregando as instruções de sistema personalizadas ao modelo.

```py title="main.py" linenums="1" hl_lines="19 24-26"
import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "developer",
            "content": ""
        }
    ]
}

with open('instructions.txt', 'r') as file:
    instructions = file.read()
    data['messages'][0]['content'] = instructions

while True:  # Laço para simular um chat
    try:

        user = input('$$ ')

        # Adiciona a mensagem do usuário na lista de mensagens
        data['messages'].append({"role": "user", "content": user})

        resp = requests.post(f'{api_url}/chat/completions',
                             headers=headers, json=data)
        body = resp.json()

        text = body['choices'][0]['message']['content']

        print(text)

        # Adiciona a resposta da modelo na lista de mensagens
        data['messages'].append({"role": "assistant", "content": text})

    except Exception as e:
        raise print(e)
```

## Introdução a tool calling (Chamada de funções)

A chamada de ferramentas refere-se à capacidade dos modelos de inteligência artificial (IA) de interagir com ferramentas externas, interfaces de programação de aplicativos (APIs) ou sistemas para aprimorar suas funções.

Essa funcionalidade permite que sistemas autônomos concluam tarefas mais complexas acessando e atuando dinamicamente sobre recursos externos e/ou internos.

Chamada de ferramentas permitem ao modelo de IA agir buscando informações na web em tempo real para otimizar o resultado com dados mais atualizados.

[What is tool calling?](https://www.ibm.com/think/topics/tool-calling)

Para configurar uma tool é necessário estruturar um objeto JSON contendo as informações necessárias para identificar a função e seu argumentos, em seguida informar para o modelo que agora ele possuí uma ferramenta para lidar com uma determinada tarefa.

### Exemplo de uma tool `pega_nome`

Abaixo um objeto JSON contendo uma ferramenta chamada `pega_nome` contendo a propiedade `nome` do tipo **string**.

```json
{
    "type": "function",
    "function": {
        "name": "pega_nome",
        "description": "Pega o nome completo do usuário", //Gatilho: instrução concisa e direta para acionar a chamada desta função
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
}
```

Atualizando o arquivo **main.py** para informar ao modelo que agora ele tem a ferramenta `pega_nome` que será acionada quando o usuário informar o seu nome.

```py title="main.py" linenums="1" hl_lines="22-44"
import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "developer",
            "content": ""
        }
    ],
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
        }
    ]
}

with open('instructions.txt', 'r') as file:
    instructions = file.read()
    data['messages'][0]['content'] = instructions

while True:  # Laço para simular um chat
    try:

        user = input('$$ ')

        # Adiciona a mensagem do usuário na lista de mensagens
        data['messages'].append({"role": "user", "content": user})

        resp = requests.post(f'{api_url}/chat/completions',
                             headers=headers, json=data)
        body = resp.json()

        text = body['choices'][0]['message']['content']

        print(text)

        # Adiciona a resposta da modelo na lista de mensagens
        data['messages'].append({"role": "assistant", "content": text})

    except Exception as e:
        raise print(e)

```

Agora executando o assistente e após o usuário informar seu nome completo o resultado da variável `text` terá um valor nulo. Isso acontece porque a tool foi acionada e agora a resposta do modelo já não é mais um texto, agora ele vai retornar instruções para a execução da função `pega_nome`.

- Debugando o retorno

```py title="main.py" linenums="1" hl_lines="63"
import requests
from decouple import config
from pprint import pprint

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "developer",
            "content": ""
        }
    ],
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
        }
    ]
}

with open('instructions.txt', 'r') as file:
    instructions = file.read()
    data['messages'][0]['content'] = instructions

while True:  # Laço para simular um chat
    try:

        user = input('$$ ')

        # Adiciona a mensagem do usuário na lista de mensagens
        data['messages'].append({"role": "user", "content": user})

        resp = requests.post(f'{api_url}/chat/completions',
                             headers=headers, json=data)
        body = resp.json()

        pprint(body)

        text = body['choices'][0]['message']['content']


        # Adiciona a resposta da modelo na lista de mensagens
        data['messages'].append({"role": "assistant", "content": text})

    except Exception as e:
        raise print(e)
```

- Analisando a resposta:

```json linenums="1" hl_lines="12"
{
  "choices": [
    {
      "finish_reason": "tool_calls",
      "index": 0,
      "logprobs": null,
      "message": {
        "annotations": [],
        "content": null,
        "refusal": null,
        "role": "assistant",
        "tool_calls": [
          {
            "function": {
              "arguments": "{'nome':'thalyson wilker'}",
              "name": "pega_nome"
            },
            "id": "call_tAmS4qkZo2FAsAOrRwon6qu1",
            "type": "function"
          }
        ]
      }
    }
  ]
}
```

Vamos corrigir o arquivo **main.py** para acessar os argumentos devolvidos pelo modelo.

```py title="main.py" linenums="1" hl_lines="4 64-75"
import requests
from decouple import config
from pprint import pprint
import json

OPENAI_API_KEY = config('OPENAI_API_KEY')

api_url = 'https://api.openai.com/v1'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "developer",
            "content": ""
        }
    ],
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
        }
    ]
}

with open('instructions.txt', 'r') as file:
    instructions = file.read()
    data['messages'][0]['content'] = instructions

while True:  # Laço para simular um chat
    try:

        user = input('$$ ')

        # Adiciona a mensagem do usuário na lista de mensagens
        data['messages'].append({"role": "user", "content": user})

        resp = requests.post(f'{api_url}/chat/completions',
                             headers=headers, json=data)
        body = resp.json()

        tool_calls = body['choices'][0]['message'].get("tool_calls")

        if(tool_calls):
            function_name = tool_calls[0]['function']['name']
            function_args = json.loads(tool_calls[0]['function']['arguments'])
            if(function_name == 'pega_nome'):
                print("Simulando a manipulação do nome...")
                nome = function_args['nome'].upper()
                text = f"Olá: {nome}! Você poderia me informar qual é o seu signo?"

        else:
            text = body['choices'][0]['message']['content']

        print(text)

        # Adiciona a resposta da modelo na lista de mensagens
        data['messages'].append({"role": "assistant", "content": text})

    except Exception as e:
        raise print(e)
```

Tool calling é fundamental porque permite que modelos de IA utilizem funcionalidades externas para executar tarefas específicas além de gerar texto, como buscar dados atualizados ou controlar dispositivos. Isso amplia muito a utilidade e precisão das respostas, tornando a IA mais prática e eficaz. Além disso, integrações com ferramentas garantem respostas contextualizadas e adaptadas às necessidades reais do usuário.


## Introdução ao Web Scraping

**Web Scraping** ou **raspagem web** é o processo de "raspagem" de dados de páginas na internet. Scripts são codificados para acessar páginas web, analisar a estrutura da sua HTML, localizar e extrair dados diversos para objetivos diversos, como coletar dados para análise posteriores, monitorar informações e preços de produtos etc…

A técnica é comum e amplamente utilizada por programadores de vários níveis. 

### Beautiful Soup
BeautifulSoup é uma biblioteca Python usada para extrair dados de arquivos HTML e XML de forma simples e eficiente. Ela facilita a navegação, busca e modificação do conteúdo das páginas web para web scraping e análise.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

Vamos brincar um pouco...

Crie o arquivo `web_scraping.py` e vamos fazer uma raspagem de dados em um site simples

Primeiro vamos preparar o `parser` - motor que analisa, interpreta e organiza os dados para facilizar sua manipulação.

```py title="web_scraping.py" linenums="1"
import requests
from bs4 import BeautifulSoup as soup

resp = requests.get("https://www.horoscopovirtual.com.br/horoscopo/libra")
html = soup(resp.text, 'html.parser')
```

Analizando o código fonte do site horoscopovirtual.com.br podemos facilmente entender sua estrutura, agora é só informar ao `BeautifulSoup` como ele deve encontrar os dados que queremos obter.

```py title="web_scraping.py" linenums="1" hl_lines="6 8-10"
import requests
from bs4 import BeautifulSoup as soup

resp = requests.get("https://www.horoscopovirtual.com.br/horoscopo/libra")

html = soup(resp.text, 'html.parser')

hoje = html.find('div', attrs={'class': 'days-wrapper'})
hoje = hoje.find('p')
hoje = hoje.text

print(hoje)

```

Agora vamos estudar um pouco mais o site para encontrar os dados de horóscopo.

```py title="web_scraping.py" linenums="1" hl_lines="12-13"
import requests
from bs4 import BeautifulSoup as soup

resp = requests.get("https://www.horoscopovirtual.com.br/horoscopo/libra")

html = soup(resp.text, 'html.parser')

hoje_div= html.find('div', attrs={'class': 'days-wrapper'})
hoje = hoje_div.find('p')
hoje = hoje.text

horoscopo_div = html.find('p', attrs={'class': 'text-pred'})
horoscopo = horoscopo_div.text.strip()

print(hoje, horoscopo)

```

### Recapitulando o nosso **scraper**

Entendemos o que é e para que serve um **scraper**, localizamos um fonte de dados para realizar a raspagem e definimos a estratégia para obter os dados.

Agora vamos unir os dois mundos e dar a nossa IA a capacidade de interagir com a web para obter informações em tempo real!

## Configurando a tool busca de horóscopo

```json
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
      "additionalProperties": false
    },
    "strict": true
  }
}
```

Vamos agora atualizar o arquivo `web_scraping.py` para permitir que o signo seja informado como argumento para a função `scraper`

```py title="web_scraping.py" linenums="1" hl_lines="4-16"
import requests
from bs4 import BeautifulSoup as soup

def scraper(signo):
    resp = requests.get( f"https://www.horoscopovirtual.com.br/horoscopo/{signo}")

    html = soup(resp.text, 'html.parser')

    hoje_div= html.find('div', attrs={'class': 'days-wrapper'})
    hoje = hoje_div.find('p')
    hoje = hoje.text

    horoscopo_div = html.find('p', attrs={'class': 'text-pred'})
    horoscopo = horoscopo_div.text.strip()

    return horoscopo
```

## Finalizando o assistente


Agora vamos atualizar o arquivo **main.py** para finalizar nosso assistente!

```py title="main.py" linenums="1" hl_lines="4-14"
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
    "messages": [
        {
            "role": "developer",
            "content": ""
        }
    ],
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
        }

    ]
}

with open('instructions.txt', 'r') as file:
    instructions = file.read()
    data['messages'][0]['content'] = instructions

while True:  # Laço para simular um chat
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
            if (function_name == 'pega_nome'):
                print("Simulando a manipulação do nome...")
                nome = function_args['nome'].upper()
                text = f"Olá: {nome}! Você poderia me informar qual é o seu signo?"

            elif (function_name == "busca_horoscopo_hoje"):
                signo = function_args["signo"]
                horosco_de_hoje = scraper(signo)
                text = f"O seu horóscopo de hoje é: {horosco_de_hoje}"

        else:
            text = body['choices'][0]['message']['content']

        print(text)

        # Adiciona a resposta da modelo na lista de mensagens
        data['messages'].append({"role": "assistant", "content": text})

    except Exception as e:
        raise print(e)

```

## Ferramentas Open Source

Projetos brasileiros relacionados que podem complementar ou inspirar:

- [ClientAI](https://github.com/benavlabs/clientai) - Cliente Python para APIs de IA
- [ProsaAI](https://github.com/cmagnobarbosa/prosaAI) - Biblioteca para processamento de linguagem natural
- [Langflow](https://github.com/langflow-ai/langflow) - Interface visual para criação de fluxos de LLM

## Referências

- [Python Requests: HTTP for Humans](https://github.com/psf/requests)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- [Python Decouple](https://github.com/HBNetwork/python-decouple)
- [Developer quickstart: Take your first steps with the OpenAI API](https://platform.openai.com/docs/quickstart?api-mode=responses)
- [Text generation and prompting](https://platform.openai.com/docs/guides/text)
- [Using tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)
- [Function calling](https://platform.openai.com/docs/guides/function-calling?api-mode=responses)

https://www.ibm.com/think/topics/tool-calling
