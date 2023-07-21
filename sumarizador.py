import openai

import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')

system_msg = '''
Você é um sumarizador de textos. Você vai receber um feedback de um
consumidor a respeito de um produto e definir qual o perfil desse
consumidor. 

O formato de retorno deverá ser um texto curto resumindo
três pontos: Nível de satisfação do consumidor; probabilidade de 
realizar mais compras; Tipos de produtos que podem interessar o 
consumidor.
'''

message = input("Informe o texto: ")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=500,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": message},
        ]
    )
    reply = response["choices"][0]["message"]["content"]
    print("\nPerfil do consumidor:\n" + reply + "\n")
except Exception as e:
    print("Ocorreu um erro na solicitação à API: ", e)
