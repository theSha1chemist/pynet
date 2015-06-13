import socket
import argparse

parser = argparse.ArgumentParser(description='Simple UDP client')
parser.add_argument('-t', '--target', help='target hostname or ip', required=True)
parser.add_argument('-p', '--port', help='port', type=int, required=True)
parser.add_argument('-m', '--message', help='message you would like to send', type=str, required=True)

args = parser.parse_args()
host = args.target
port = args.port
message = args.message

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(message, (host, port))
