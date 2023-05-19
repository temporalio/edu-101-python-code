from flask import Flask, request

app = Flask(__name__)

@app.route('/get-spanish-greeting', methods=['GET'])
def spanish_greeting_handler():
    name = request.args.get('name', None)
    if name:
        translation = f"¡Hola, {name}!"
        return translation,  200
    else:
        return "Missing required 'name' parameter.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
