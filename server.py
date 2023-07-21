#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

HOST = 'localhost'
PORT = 65535

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((HOST, PORT))
my_socket.listen()

print("Waiting for connection!")

conn, address = my_socket.accept()

print("Connecting on ", address)

while True:
    data = conn.recv(1024)
    
    if not data:
        print("Closing connection")
        conn.close()
        
        break
    
    conn.sendall(data)
    conn.close()
    break
    