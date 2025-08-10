from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def intro():
    now = datetime.now()
    return render_template("introduction.html", hour=now.hour)

@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    hobbies = ["Eating", "Singing", "Gaming"]
    return render_template("hobbies.html", hobbies=hobbies)

@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def opinion(topic):
    return f"{topic}"

@app.route("/opinion/food")
def food():
    foods = ["Lasagna", "Sinigang", "Fried Chicken", "Kare-Kare", "Sisig"]
    return render_template("foods.html", foods=foods)

@app.route("/skills/")
def skills():
    skill_levels = {
        "Singing" : "Proficient",
        "Dancing" : "Poor",
        "Coding" : "Abysmal",
        "Eating" : "Professional",
    }
    return render_template("skills.html", skills=skill_levels)

app.run()