from flask import Flask
app = Flask(__name__)

@app.route("/")
def intro():
    return "<h1>I am Jimwel</h1>"

@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    return "Hobbies: 1. Eating 2. Singing 3. Gaming"

@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def opinion(topic):
    return f"{topic}"

@app.route("/opinion/food")
def food():
    return "My favourite foods: 1.Lasagna 2.Sinigang 3.Fried Chicken 4.Kare-Kare 5. Sisig"


app.run()