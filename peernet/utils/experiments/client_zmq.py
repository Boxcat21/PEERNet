import zmq
import time

# Initialize ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)  # REQ = Request
ip = ''
# ip = '127.0.1.1'
port = '49152'
socket.connect("tcp://" + ip + ":" + port)  # Replace <Server_IP> with the IP of Machine 1

print("Client is sending request to the server...")

while True:
    try:
        # Send a request
        socket.send_string("CLIENT: Hello from the client! This is a unique message!")
        print("Sent request to the server.")
        
        # Wait for the reply from the server
        message = socket.recv_string()
        print(f"Received reply: {message}")
        break  # Break out of loop after receiving a reply
        
    except zmq.ZMQError as e:
        print(f"ZMQ Error: {e}")
        time.sleep(1)  # Retry after a short pause
    except Exception as e:
        print(f"Error: {e}")
        break
