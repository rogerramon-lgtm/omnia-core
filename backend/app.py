from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "status": "ok",
        "app": "Omnia Core",
        "message": "Backend ativo"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
