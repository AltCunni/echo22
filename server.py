import socket
import logging

logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    logging.info(f'Connection established from address {address}')

    while True:
        data = clientSocket.recv(1024).decode("utf-8")
        if data == "exit":
            logging.info("Client has disconnected")
            clientSocket.close()
            break
        else:
            logging.info(f"Received: {data}")

s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6060))
s.listen(5)
logging.info("Server is now listening for new connections")
