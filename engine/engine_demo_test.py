#!/usr/bin/env python2
import socket 
import sys

server_addr = "./demo_socket"

def demo_test():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    try:
        sock.connect(server_addr)
    except socket.error, msg:
        print("exception: %s" % msg)
        sys.exit(1)

    print("Connected to server.")
    message = "test message."

    sock.sendall(message)
    print("    send: %s" % message)

    data = sock.recv(1024)

    print("    recieved: %s" % data)

    sock.close()


if __name__ == "__main__":
    demo_test()
