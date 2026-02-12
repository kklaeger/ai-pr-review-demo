from flask import Flask, request, jsonify

app = Flask(__name__)

txt = "Hello World"

@app.route("/hello", methods=["GET"])
def hello():
    """
    Handle GET /hello requests and return a greeting using an optional `name` query parameter.
    
    If `name` is provided the greeting is "Hello <name>"; otherwise the greeting is "Hello World".
    Returns a JSON response with keys "message" (the greeting) and "success" (True) and an HTTP status code 200.
    """
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
    """
    Provide a simple health-check payload.
    
    Returns:
        dict: A JSON-serializable dictionary `{'status': 'ok'}` indicating the service is healthy.
    """
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)