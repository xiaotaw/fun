#!/usr/bin/env python2
#import log
import os
import socket
import time


server_addr = "./demo_socket"

def demo():
    print("init engine ... ")
    time.sleep(0.3)

    if os.path.exists(server_addr):
        os.unlink(server_addr)

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(server_addr)
    sock.listen(3)

    print("server start ... ")

    while(1):
        conn, client_addr = sock.accept()
        print("connected by: %s " % str(client_addr))
        conn.settimeout(5)

        try:
            request_data = conn.recv(1500)
            if request_data:
                print("    recieved: %s" % request_data)
                print("    processing (convert to uppercase) ... ")
                time.sleep(1)
                response_data = request_data.upper()
                conn.sendall(response_data)
                print("    responsed: %s" % response_data)
        except Exception as e:
            print(e)
        finally:
            conn.close()
            print("connect close.")

if __name__ == "__main__":
    demo()
