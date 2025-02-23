import zmq
import time

# Initialize ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REP)  # REP = Reply
port = '5000'
socket.bind("tcp://*:" + port)  # Binding to port 49152

print("Server is waiting for requests...")

cnt = 0
while True:
    cnt += 1
    try:
        # Waiting to receive a message
        message = socket.recv_string(flags=zmq.NOBLOCK)  # Non-blocking
        if message:
            print(f"Received request: {message}")
            # Simulate some processing
            time.sleep(1)
            socket.send_string("Hello from the server!")
            print("Sent reply to the client.")
            break  # Break out of loop after sending a reply
        else:
            # No message received, check if it's an issue with waiting
            print("No message received, waiting for a request...")

    except zmq.Again:
        # This exception is raised when no message is received (non-blocking mode)
        # print("No request received yet, retrying... ({})".format(cnt))
        # time.sleep(1)  # Pause for a moment before checking again
        pass
    except Exception as e:
        print(f"Error: {e}")
        break
