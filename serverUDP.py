import socket
import argparse

parser = argparse.ArgumentParser(description='Simple UDP server')
parser.add_argument('-p', '--port', help='port', type=int, required=True)

args = parser.parse_args()
port = args.port

host = "0.0.0.0"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((host, port))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
