import openai
import os
from dotenv import load_dotenv
import requests
from requests.exceptions import Timeout

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')

system_msg = '''

'''

message = input("Informe o texto: ")

try:
    # Configurações de timeout e rate limit
    timeout = 10
    max_retry_attempts = 3

    # Função para enviar a requisição à API com tratamento de erro
    def send_openai_request(payload):  # sourcery skip: raise-specific-error
        retries = 0
        while retries < max_retry_attempts:
            try:
                response = requests.post("https://api.openai.com/v1/chat/completions",
                                         headers={
                                             "Content-Type": "application/json",
                                             "Authorization": f"Bearer {openai.api_key}"
                                         },
                                         json=payload,
                                         timeout=timeout)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as http_err:
                print(f"Erro HTTP: {http_err}")
                retries += 1
            except Timeout:
                print(f"Timeout - tentativa {retries + 1} de {max_retry_attempts}")
                retries += 1

        raise Exception("Falha na solicitação à API OpenAI após várias tentativas.")

    payload = {
        "model": "gpt-3.5-turbo",
        "temperature": 1,
        "max_tokens": 500,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": message},
        ]
    }

    response = send_openai_request(payload)

    reply = response["choices"][0]["message"]["content"]
    print("\nPerfil do consumidor:\n" + reply + "\n")
    
except Exception as e:
    print("Ocorreu um erro na solicitação à API: ", e)
