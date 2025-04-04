from flask import Flask, jsonify
from flask_socketio import SocketIO
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Mock traffic data (replace with SUMO integration)
traffic_data = {
    "north": 0,
    "south": 0,
    "east": 0,
    "west": 0,
    "emergency": False
}

def update_traffic_data():
    while True:
        # Simulate random traffic changes
        traffic_data["north"] = random.randint(0, 20)
        traffic_data["south"] = random.randint(0, 20)
        traffic_data["east"] = random.randint(0, 20)
        traffic_data["west"] = random.randint(0, 20)
        traffic_data["emergency"] = random.random() < 0.1
        
        # Send data via WebSocket
        socketio.emit('traffic_update', traffic_data)
        time.sleep(2)

@app.route('/api/traffic', methods=['GET'])
def get_traffic():
    return jsonify(traffic_data)

if __name__ == '__main__':
    threading.Thread(target=update_traffic_data).start()
    socketio.run(app, port=5000)
