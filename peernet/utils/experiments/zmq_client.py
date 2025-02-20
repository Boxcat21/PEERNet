import zmq
import time

# Initialize ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)  # REQ = Request
socket.connect("tcp://192.168.4.182:5555")  # Replace <Server_IP> with the IP of Machine 1

print("Client is sending request to the server...")

while True:
    try:
        # Send a request
        socket.send_string("Hello from the client!")
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
