import os
from flask import Flask, jsonify
import psycopg2
app = Flask(__name__)

def connexion_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        dbname=os.environ.get("DB_NAME", "ventes"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres"),
    )
    
    

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/ventes")
def ventes():
    conn = connexion_db()
    cur = conn.cursor()
    cur.execute("SELECT id, produit, montant FROM ventes;")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)
if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8000)