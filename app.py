from flask import Flask, request, jsonify

app = Flask(__name__)

commande_en_cours = {"action": "rien"}

@app.route("/")
def home():
    return "API Pico OK"

@app.route("/commande", methods=["GET"])
def get_commande():
    return jsonify(commande_en_cours)

@app.route("/commande", methods=["POST"])
def set_commande():
    data = request.get_json()
    commande_en_cours["action"] = data.get("action", "rien")
    return jsonify({"status": "ok", "nouvelle_action": commande_en_cours["action"]})

@app.route("/etat", methods=["POST"])
def recevoir_etat():
    data = request.get_json()
    print("Etat recu du Pico :", data)
    return jsonify({"status": "recu"})
