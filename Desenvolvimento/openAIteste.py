import requests

# Definir a chave da API
API_KEY = ""


# Temas permitidos
temas_permitidos = ["SENAI", "SAMSUNG", "EDUCACIONAL", "TECNOLÓGICO"]

""""# Função para verificar se a resposta está dentro dos temas permitidos
def respostaTemas(resposta, temas_permitidos):
    resposta_em_caixa_alta = resposta.upper()
    for tema in temas_permitidos:
        if tema in resposta_em_caixa_alta:
            return True
    return False"""

# Definir o prompt
mensagem = input("Digite a sua pergunta à SELENE: ")

# Chamar a API
response = requests.post(
    "https://api.openai.com/v1/engines/text-davinci-002/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"prompt": mensagem, "temperature": 0.9, "max_tokens": 100},
)

# Verificar se a resposta foi bem-sucedida
if response.status_code == 200:
    response_json = response.json()
    if "choices" in response_json:
        # Exibir a resposta
        print(response_json["choices"][0]["text"])
    else:
        # Lidar com uma resposta inesperada
        print("Erro: Resposta inesperada da API.")
else:
    # Lidar com erros de solicitação à API
    print(f"Erro na solicitação à API: {response.status_code}")
    print(response.text)
