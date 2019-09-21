import socket
import atexit

import task

host = "192.168.1.12"
port = 23008

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
print("Connected to " + host + ":" + str(port))


def close():
	socket.close()

atexit.register(close)


def request_task():
	socket.send("REQ_TASK".encode())
	print("req")
	return socket.recv(1024).decode()

def return_result(task_id, result):
	socket.send(("RETURN:" + str(task_id) + ":" + result).encode())
	print(socket.recv(1024).decode())

while True:
   task_id = int(request_task())
   return_result(task_id, task.get_result(task_id))