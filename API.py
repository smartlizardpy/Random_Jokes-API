from flask import Flask, request
import json
import random

app = Flask(__name__)

@app.route("/")
def home():
    with open('jokes.json', 'r') as file:
        data = json.load(file)

# Specify the joke number you want to retrieve
    joke_number = random.randrange(1, 100)

# Get the joke based on the specified number
    joke = data['jokes'][joke_number - 1][str(joke_number)]
    return joke


if __name__ == "__main__":
    app.run(debug=True)