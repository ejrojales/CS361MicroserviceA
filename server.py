import zmq
import json
import random


def getRandomBook():
    books_json_path = './books.json'
    with open(books_json_path, 'r') as book_file:
        data = json.load(book_file)

    books = list(data.items())
    index = random.randint(0, len(data) - 1)
    title = books[index][0]
    author = books[index][1]["author"]
    genre = books[index][1]["genre"]
    return f"Title: {title} \n Author: {author} \n Genre: {genre}"


def microserviceA():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Server started. Waiting for requests...")
    try:
        while True:
            # Wait for next request from client
            message = socket.recv_string()

            if message == "/q":
                print("Received quit command. Shutting down...")
                socket.send_string("/q")
                break

            if message == "1":
                # Get random book
                randomBook = getRandomBook()
                # Send reply back to client
                socket.send_string(randomBook)
            else:
                socket.send_string(
                    "Invalid usage. Please enter 1 to receive a book recommendation or '/q' to quit")
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        # clean up
        socket.close()
        context.term()


if __name__ == "__main__":
    microserviceA()
