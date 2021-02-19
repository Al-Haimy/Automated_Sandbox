"""
Using Python 3.8   
Clinet side 
"""
import socket
import json
import subprocess
import time
import os
import threading
import shutil
import sys


def connectToServer():
    while True:

        try:
            SOK.connect((IP, PORT))
            print('connected')
            break
        except:
            time.sleep(9)
            connectToServer()


IP = '192.168.1.2'
PORT = 55555
SOK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connectToServer()
SOK.close()
