import json


class ChatGPTRequest:
    def __init__(self, model, prompt, max_tokens):
        self.model = model
        self.prompt = prompt
        self.max_tokens = max_tokens


import requests

""""
def main():
    # Faça a solicitação ao Bard
    response = requests.post(
        "https://api.bard.ai/v1/engines/davinci/generate",
        headers={
            "Authorization": "Bearer *******",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "prompt": "Por que o céu é azul?",
            "max_tokens": 150
        })
    )

    # Verifique o status da resposta
    if response.status_code != 200:
        raise Exception(
            "Bard API returned error code {}".format(response.status_code)
        )

    # Extraia a resposta do JSON
    response_json = response.json()
    response_text = response_json["choices"][0]["text"]

    # Imprima a resposta
    print(response_text)


if __name__ == "__main__":
    main()
    """
