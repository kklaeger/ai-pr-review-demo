from flask import Flask, request, jsonify

app = Flask(__name__)

txt = "Hello World"

@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name")

    if name:
        greeting = "Hello " + name
    else:
        greeting = "Hello World"

    response = {
        "message": greeting,
        "success": True
    }

    return jsonify(response), 200


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
