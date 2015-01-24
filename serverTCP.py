#!/usr/bin/python2.7

import socket
import argparse
import threading


parser = argparse.ArgumentParser(description='Simple TCP server')
parser.add_argument('-l', '--listen', help='listen address', required=True)
parser.add_argument('-p', '--port', help='listen port', type=int, required=True)

args = parser.parse_args()
address = args.listen
port = args.port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen(5)
print "[*] Listening on %s,%d" % (address, port)


def handleClient(clientSocket):
    request = clientSocket.recv(1024)

    print "[*] Recieved %s" % request

    clientSocket.send("ACK!")

    clientSocket.close()

while True:

    client, addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    # spin up our client thread to handle incoming data

    clientHandler = threading.Thread(target=handleClient, args=(client,))
    clientHandler.start()
