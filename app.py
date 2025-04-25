from flask import Flask, request, jsonify

app = Flask(__name__)

command = ["null","null","null","null","null","null","null"]

@app.route("/")
def home():
    return "API Pico OK"

@app.route("/command", methods=["GET"])
def get_commande():
    return jsonify(command)

@app.route("/command", methods=["POST"])
def set_commande():
    data = request.get_json()
    for i in range(len(data))
    {
        command[i] = data[i]
    }
    return jsonify({"status": "ok", "nouvelle_action": command})

@app.route("/etat", methods=["POST"])
def recevoir_etat():
    data = request.get_json()
    print("Etat recu du Pico :", data)
    return jsonify({"status": "recu"})
