from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    # Get the data from the request
    data = request.json

    # Print the received data to the console
    print("Received data:", data)

    return "Data received and printed", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999)
