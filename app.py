from flask import Flask, request, jsonify
import random

app = Flask(__name__)

random.seed(57)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b  = random.uniform(-10, 10)

@app.route('/predict')
def predict():
    try:
        x1 = float(request.args.get('x1'))
        x2 = float(request.args.get('x2'))
        x3 = float(request.args.get('x3'))
    except (TypeError, ValueError):
        return jsonify({"error": "x1, x2, x3 required"}), 400

    prediction = a1*x1 + a2*x2 + a3*x3 + b
    return jsonify({
        "registration number": "SP23-BAI-057",
        "prediction": round(prediction, 2)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
