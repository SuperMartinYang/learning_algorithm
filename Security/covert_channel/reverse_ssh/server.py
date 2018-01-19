import socket
import paramiko
import threading
import sys

KEYNAME = 'rsa.key'
HOST = '127.0.0.1'
PORT = 22
USERNAME = 'test'
PASSWORD = 'test'
host_key = paramiko.RSAKey(filename=KEYNAME)


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == USERNAME and password == PASSWORD:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(100)
    print("Listening for connections ...")
    client, addr = sock.accept()
except Exception as e:
    print("Listen/bind/accept failed: " + str(e))
    sys.exit(1)

try:
    t = paramiko.Transport(client)
    t.load_server_moduli()
    t.add_server_key(host_key)
    server = Server()
    t.start_server(server=server)

    chan = t.accept(20)
    print(chan.recv(2048))

    while True:
        command = input("SHELL >> ")
        chan.send(command)
        print(chan.recv(2048).decode('utf-8'))
except Exception as e:
    print('Caught exception: ' + str(e) + ":" + str(e))
    t.close()
    sys.exit(1)
