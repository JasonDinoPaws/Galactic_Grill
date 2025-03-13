import socket, pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.0.12.2", 8888))
# data = client_socket.recv(4096)
# data = pickle.loads(data)
# print(repr(data))
while True:
    text = input('send: ')
    client_socket.send(text.encode())
    data = client_socket.recv(4096)
    if not data:
        break
    print(repr(pickle.loads(data)))
