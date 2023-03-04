# import files
from flask import Flask, render_template, request, jsonify
import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.arabic")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=['POST', 'GET'])
def get_bot_response():

    '''
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
    '''
    if request.method == 'GET':
        userText = request.args.get('msg')
        text_format = str(chatbot.get_response(userText))
        li = list(text_format.split("-#-"))
        #str_li = '\n'.join(li)
        print(li)
        #return jsonify({"msg": str_li})

        #return jsonify({"errorCod": 200, "msgs": [{"msg": li}]})
        listjson=[]
        for item in li:
            listjson.append({"message":item})
        print(listjson)
        now = datetime.datetime.now()
        s=now.strftime("%d/%m/%Y, %H:%M:%S")
        return jsonify({"errorCod": 200, "datatime": s, "messages": listjson})
        #return str_li

    if request.method == 'POST':
        userText = request.args.get('msg')
        return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
