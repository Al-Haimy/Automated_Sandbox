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
import filetype

PATH = 'downlaod'
BUFFER_SIZE = 1024


def send_data(data):
    jsondata = json.dumps(data)
    SOK.send(jsondata.encode())


def send_file(file_name):

    file_name = PATH + '\\' + file_name
    f = open(file_name, 'rb')
    data = f.read(1024)
    while data:
        SOK.send(data)
        data = f.read(1024)
    f.close()
    os.remove(file_name)


def recv_data():
    data = ''
    while True:
        try:
            data = data + SOK.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def _check():
    s = []
    ls = os.listdir(PATH)
    if ls != s:
        return ls
    else:
        return 'not found'


def share_file():
    while True:
        print('Listening for commands .....')
        con = recv_data()
        print(con)
        if con[:3] == "che":
            folders = []
            folders = _check()
            print(folders)
            send_data(folders)
        elif con[:8] == 'download':
            send_file(con[9:])


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
SOK = socket.socket()
print(f'Establishing Connection')
connectToServer()
SOK.close()
