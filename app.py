from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def main():
    return "Please go to /pokemon/<query> and insert either pokedex number or pokemon name"

@app.route('/pokemon/<query>', methods=['GET'])
def pokemon(query):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{query}/")
    # r = r.json()
    req = json.loads(r.text)
    print("id: ")
    print(req["id"])
    print("name: ")
    print (req["name"])
    pokeid = str(req["id"])
    name = req["name"]
    if (str(query) == pokeid):
        text = f"The pokemon with id {pokeid} is {name}"
    else:
        text = f"{name} has id {pokeid}"
    return render_template('page.html', text=text)


if __name__ == '__main__':
    app.run()
