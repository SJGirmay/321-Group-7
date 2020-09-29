import json

data = json.loads(open('intents.json', 'r').read())

train = []

for intent in data["intents"]:
	for pattern in intent["patterns"]:
		train.append(pattern)
	for response in intent["responses"]:
		train.append(response)

from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

# Create a new chatbot name Lily
chatbot = ChatBot('Lily')

trainers = ListTrainer(chatbot)

trainers.train(train)

while True:
	text = input('Type a message...\n')
	reply = chatbot.get_response(text)
	print('Lily:', reply)
    
