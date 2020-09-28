from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot('Lily')

talk = ['Hi there!', 'Hi!','Hello!', 'My name is Lily',
        'I am doing great, you?', 'I\'m doing well, thanks for asking',
        'excellent, glad to hear that.',
        'Sorry to hear that.']

list_trainer = ListTrainer(my_bot)
list_trainer.train(talk)
while True:
    text = input('Type a message...\n')
    reply = chatbot.get_response(text)
    print('Lily:', reply)
    
