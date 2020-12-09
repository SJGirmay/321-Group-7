#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)


#bot = ChatBot("Candice")
#trainers = ListTrainer(bot)
#trainers.train("chatterbot.corpus.english")

import json

data = json.loads(open('intents.json', 'r').read())
data1 = []

for intent in data["intents"]:
	for pattern in intent["patterns"]:
		data1.append(pattern)
	for response in intent["responses"]:
		data1.append(response)

from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

# Create a new chatbot name Lily
bot = ChatBot('Lily')

trainers = ListTrainer(bot)

trainers.train(data1)

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()

