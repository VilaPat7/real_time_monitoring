from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_alerts():
    alert = request.json
    print("Received Alert:", alert)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5001)

