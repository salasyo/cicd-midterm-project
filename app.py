from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "0.1.0"


@app.route("/")
def home():
    return jsonify(status="healthy", message="CI Foundation Operational")


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/version")
def version():
    return jsonify(version=VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
