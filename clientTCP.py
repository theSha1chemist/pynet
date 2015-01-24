#!/usr/bin/python2.7

import socket
import argparse

parser = argparse.ArgumentParser(description='Simple tcp client')
parser.add_argument('-t', '--target', help='target hostname or ip', required=True)
parser.add_argument('-p', '--port', help='port', type=int, required=True)
parser.add_argument('-m', '--message', help='message to send. eg GET / HTTP/1.1\r\nHost: google.com\r\n\r\n', type=str, required=True)

args = parser.parse_args()

host = args.target
port = args.port
message = args.message

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client.connect((host, port))

client.send(message)

# recieve some data
response = client.recv(4096)

print response

client.close()
