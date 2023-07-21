#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = 'localhost'
PORT = 65535

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((HOST, PORT))

my_socket.sendall(str.encode("Hello World!"))

data = my_socket.recv(1024)

print("MSG: ", data.decode())
