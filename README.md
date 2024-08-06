# Communication Contract
The random book recommendation retrieves a random book's title, author, and genre in a local dataset file called books.json. 

## Request
After the socket connection has been made between the microservice and the main program, the main program should use send_string() to communicate with the service. Specifically send_string("1") to get a random book recommendation or send_string("/q") to close the connection with the service. 

## Response
After the request has been made, the main program should use recv_string() to receive any response from the microservice.

![Alt text](/UMLDiagram.png "UML Sequence Diagram")
