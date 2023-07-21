import openai

import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')

system_msg = '''
Você é um extrator de informações. Você recebe um anúncio de marketing
sobre um produto e retorna os dados brutos sobre o produto em formato JSON. 
Exemplo de retorno:
{
  "marca": "Pear",
  "modelo": "Notebook Pear",
  "cor": "Preto"
}
'''

message = input("Informe o anúncio: ")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": message},
        ]
    )
    reply = response["choices"][0]["message"]["content"]
    print("\nResposta em JSON:\n" + reply + "\n")
except Exception as e:
    print("Ocorreu um erro na solicitação à API: ", e)
