import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

conn = psycopg2.connect(os.environ['DataBase_URL'], sslmode='require')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS commandes (
        id SERIAL PRIMARY KEY,
        valeurs TEXT[]
    );
""")

@app.route("/")
def home():
    return "API Pico OK"

@app.route("/command", methods=["GET"])
def get_command():
    cur.execute("SELECT valeurs FROM commandes LIMIT 1;")
    result = cur.fetchone()
    if result:
        return jsonify(result[0])
    else:
        return jsonify(["null", "null", "null", "null", "null", "null", "null"])

@app.route("/command", methods=["POST"])
def set_command():
    command = request.get_json()

    cur.execute("DELETE FROM commandes;")
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS commandes (
            id SERIAL PRIMARY KEY,
            valeurs TEXT[]
        );
    """)
    conn.commit()

    cur.execute("DELETE FROM commandes;")  # On vide la table avant d'insérer
    cur.execute("INSERT INTO commandes (valeurs) VALUES (%s);", (command,))
    conn.commit()

    return jsonify({"status": "ok", "nouvelle_action": command})

@app.route("/etat", methods=["POST"])
def get_state():
    data = request.get_json()
    print("Etat recu du Pico :", data)
    return jsonify({"status": "recu"})
