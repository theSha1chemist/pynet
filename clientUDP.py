#!/usr/bin/python2.7

import socket
import argparse

parser = argparse.ArgumentParser(description='Simple udp client')
parser.add_argument('-t', '--target', help='target hostname or ip', required=True)
parser.add_argument('-p', '--port', help='port', type=int, required=True)
parser.add_argument('-m', '--message', help='message you want to send', type=str, required=True)

args = parser.parse_args()

host = args.target
port = args.port
message = args.message
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send message
client.sendto(message, (host, port))


# recieve some data
data, addr = client.recvfrom(4096)

print data


