from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai
from pymongo import MongoClient
openai.api_key = "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"




app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://jainanshul1304:77wonders@promptmaster.f0en01l.mongodb.net/ChatGPT"
mongo = PyMongo(app)
client = MongoClient("mongodb+srv://jainanshul1304:77wonders@promptmaster.f0en01l.mongodb.net/ChatGPT")
db = client.ChatGPT
users_collection = db.users 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        user = users_collection.find_one({'username': username})
        if user and user['password'] == password:

            return render_template('index.html')
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"question": question, "answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = openai.completions.create(
                    model="text-davinci-003",
                    prompt=question,
                    temperature=0.7,
                    max_tokens=1800,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
            print(response)
            data = {"question": question, "answer": response.choices[0].text}
            mongo.db.chats.insert_one({"question": question, "answer": response.choices[0].text})
            return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
        
    return jsonify(data)


app.run(debug=True, port=5001)