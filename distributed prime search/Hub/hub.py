import socket
import threading

import task

host = '' # accept all requests
port = 23008

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))


def handle_request(req):
    if req.startswith("REQ_TASK"):
        return str(task.get_task())
    elif req.startswith("RETURN"):
        cmd, id, result = req.split(":")
        return task.receive_results(id, result)

    return "error_invalid"


class Responder(threading.Thread):
    def __init__(self, socket, address):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.start()

    def run(self):
        while True:
            data = self.socket.recv(1024).decode().strip()
            print("[]" + data)
            self.socket.send(handle_request(data).encode())


serversocket.listen(5)
print ('Listening on port ' + str(port))


while True:
    response_socket, address = serversocket.accept()
    print("Inbound connection from " + address[0] + ":" + str(address[1]))
    Responder(response_socket, address)