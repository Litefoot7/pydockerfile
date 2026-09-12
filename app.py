from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do.",
    "Code never lies, comments sometimes do.",
    "First, solve the problem. Then, write the code.",
    "Simplicity is the soul of efficiency.",
    "Docker doesn't fix bad code, but it ships it consistently."
]

@app.route('/')
def home():
    return jsonify(message="Welcome to the Quote API! Try /quote or /health")

@app.route('/quote')
def get_quote():
    return jsonify(quote=random.choice(quotes))

@app.route('/health')
def health():
    return jsonify(status="healthy")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
