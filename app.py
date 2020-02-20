from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot("Candice")
#bot.storage.drop()
#bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)
trainer2 = ChatterBotCorpusTrainer(bot)
trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])
trainer2.train("chatterbot.corpus.english.greetings")
trainer2.train("chatterbot.corpus.english.conversations")
trainer.train(['What is the closest branch near me?','One is at 601 Stewart Green SW Calgary'])
trainer.train(['What is the closest branch near me?','One is at 2140 34 Ave SW, Calgary, AB T2T 5P6'])
trainer.train(['Who are all of my counterparties?', 'Right now your counter parties; Telus, University of Calgary,'])
trainer.train(['What types of preferred credit cards do you offer?', 'We offer Fixed-rate master card and Variable-rate master card'])




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()
