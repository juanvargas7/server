# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 20:31:06 2021

@author: Juan
"""

import socket
import os


password = 'juan'
HOST = ''  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
while True:
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                login = conn.recv(1024)
                if login.decode('utf-8') == 'juan':
                
                    conn.sendall(b'200')
                    
                    while True:
                        try:
                            cmd = conn.recv(1024).decode('utf-8')
                        except Exception:
                            break
                        print(cmd)
                        if cmd == 'exit\n':
                            break
                        output = os.popen(cmd).read()
                        conn.sendall(output.encode('utf-8'))
                    break
                else:
                    conn.sendall(b'404')
                    break   # Close the connection
