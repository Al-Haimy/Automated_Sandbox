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

PATH = 'downlaod/'


def send_data(data):
    jsondata = json.dumps(data)
    SOK.send(jsondata.encode())


def recv_data():
    data = ''
    while True:
        try:
            data = data + SOK.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def _check():
    ls = os.listdir(PATH)
    return ls


def share_file():
    while True:
        con = recv_data()
        print(con)
        if con[:3] == "che":
            folders = []
            folders = _check()
            print(folders)
            send_data(folders)
        # elif con


def connectToServer():
    while True:

        try:
            # print("trying to find connection")
            SOK.connect((IP, PORT))
            print('connected')
            share_file()
            break
        except:
            # print("Error")
            time.sleep(9)
            # connectToServer()


IP = '192.168.1.7'
PORT = 55555
print(f'just assigned Ip {IP} and Port {PORT}')
SOK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'Establishing Connection')
connectToServer()
SOK.close()
