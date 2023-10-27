import json
class ChatGPTRequest:
    def __init__(self, model, prompt, max_tokens):
        self.model = model
        self.prompt = prompt
        self.max_tokens = max_tokens


# Criando um objeto ChatGPTRequest
chat_gpt_request = ChatGPTRequest("text-davinci-003", "Por que o céu é azul", 150)

# Serializando o objeto para JSON
json_string = json.dumps(chat_gpt_request.__dict__)

print(json_string)

# Desserializando o JSON para um objeto Python
copia_dict = json.loads(json_string)
copia = ChatGPTRequest(**copia_dict)

print(copia.model)
