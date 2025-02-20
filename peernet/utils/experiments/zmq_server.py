import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)  # REP = Reply
socket.bind("tcp://*:5555")  # Binds to all network interfaces

print("Server waiting for request...")
while True:
    message = socket.recv_string()
    print(f"Received request: {message}")
    socket.send_string("Hello from the server!")
