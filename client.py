import zmq

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

message = input("Type 1 to get a random book recommendation or '/q' to quit\n")

# Client terminates the connection if message == '/q'
while True:
    socket.send_string(message)       # send message
    data = socket.recv_string()   # receive response
    if data == "/q":
        break
    print(data)
    message = input("> ")

socket.close()                          # close the connection
