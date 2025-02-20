import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)  # REQ = Request
socket.connect("tcp://<Server_IP>:5555")  # Use the IP of Machine 1

socket.send_string("Hello from the client!")
message = socket.recv_string()
print(f"Received reply: {message}")
