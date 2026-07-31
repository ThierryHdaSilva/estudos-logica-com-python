import requests

try:
    # timeout evita que o programa fique esperando indefinidamente.
    resposta = requests.get('https://www.google.com.br', timeout=5)
    print(resposta.status_code)
except requests.RequestException as erro:
    print(f"Não foi possível acessar o site: {erro}")
