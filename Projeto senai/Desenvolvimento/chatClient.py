import json
import requests

class ChatGPTClient:
    def traduzir(self, OPENAI_API_KEY, texto):
        prompt = f"Traduzir o texto {texto}, dando duas opções de respostas em português."
        requisicao = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "max_tokens": 100
        }
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.openai.com/v1/completions", data=json.dumps(requisicao), headers=headers)
        chatGPTResponse = response.json()
        completion = chatGPTResponse["choices"][0]["text"]
        return completion

    def perguntarChat(self, OPENAI_API_KEY, perguntaCriancas):
        prompt = f"{perguntaCriancas}. Responda em menos de 30 palavras de forma simples."
        requisicao = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "max_tokens": 100
        }
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.openai.com/v1/completions", data=json.dumps(requisicao), headers=headers)
        chatGPTResponse = response.json()
        completion = chatGPTResponse["choices"][0]["text"]
        return completion
