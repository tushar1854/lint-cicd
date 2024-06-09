from flask import Flask, jsonify, request
import random

app = Flask(__name__)


@app.route("/api/v1/getPolarity", methods=["GET"])
def getPolarity():
    text = request.args.get('text')
    polarity_score = random.uniform(0.3, 0.9)
    if polarity_score > 0.5:
        polarity = 'postive'
    else:
        polarity = 'negative'
    return jsonify({"msg": text, "polarity_score": polarity_score, "polarity": polarity})


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)