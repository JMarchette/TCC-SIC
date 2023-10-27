class ChatGPTResponse:
    def __init__(self):
        self.choices = []


class Choice:
    def __init__(self):
        self.text = ""


response = ChatGPTResponse()
choice1 = Choice()
choice1.text = "Texto da primeira escolha"
choice2 = Choice()
choice2.text = "Texto da segunda escolha"

response.choices.append(choice1)
response.choices.append(choice2)
