from flask import Flask, request, jsonify

app = Flask(__name__)

txt = "Hello World"

@app.route("/hello", methods=["GET"])
def hello():
    """
    Provide a greeting message based on the optional "name" query parameter.
    
    If "name" is present in the request query string, the greeting is "Hello {name}"; otherwise the greeting defaults to "Hello World".
    
    Returns:
        tuple: A pair (response, status_code) where `response` is a JSON object with keys `message` (the greeting string) and `success` (`True`), and `status_code` is 200.
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
    Indicates the application's health status.
    
    Returns:
        dict: A dictionary containing {"status": "ok"}.
    """
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)