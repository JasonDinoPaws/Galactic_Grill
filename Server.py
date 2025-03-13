import socket, pickle
from Menu import Menu
from threading import Thread

m = Menu()
receipts = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.110.91",8888))
sock.listen(1)

def Client(cli:socket,address):
    global receipts
    print(f"Client connected from {address}")
    while True:
        data = cli.recv(4096)
        if not data:
            break
        decode = data.decode()

        if decode == "m":
            cli.sendall(pickle.dumps(m.GetMenu()))
        elif decode == "t":
            redata = cli.recv(4096)
            receipt = repr(pickle.load(redata))
            receipts.append(receipt)


while True:
    cli, addr = sock.accept()
    Thread(target=Client,args=(cli,addr,)).start()