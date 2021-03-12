"""
Using python 3.8 
server side 
"""


import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
import json
from time import sleep
import sqlite3
import os

BUFFER_SIZE = 1024


def creatPath(pat):
    mypath = str(pat)

    if not os.path.isdir(mypath):
        os.makedirs(mypath)


def data_store(file_name, file_type, file_size, file_path, socket_obj, IP, scanned):

    con = sqlite3.connect('man.db')
    cursor = con.cursor()
    try:
        # file_type = str(file_type.replace('/', ' '))
        file_size = int(file_size)
        file_path = str(file_path.replace(r'\\', '/'))
        cursor.execute(
            "INSERT INTO FileAnalysis(file_name, file_type, file_size, file_path, IP, scanned) VALUES (?,?,?,?,?,?)", (file_name, file_type, file_size, file_path, IP, scanned))
        con.commit()
        con.close()
    except Exception as e:
        con.close()
        print(f"error ------->{e}")
#  file_name file_type file_size  file_path socket_obj IP  scanned


def check_file(file_name, target, ip):
    send_command(target, 'download '+file_name)
    file_info = recive_check(target)
    file_type = file_info[0]
    file_size = file_info[1]
    socket_obj = target
    creatPath(ip[0])
    file_path = ip[0] + r'\\'+file_name
    scanned = 0
    print(f'file Name: {file_name}')
    print(f'file Type: {file_type}')
    print(f'file Size: {file_size}')
    print(f'Receiving from {ip[0]}')
    # info = ()

    f = open(file_path, 'wb')

    print(f'downloading the file {file_name}')
    data_chunk = target.recv(1024)
    target.settimeout(1)
    print(f'receiving data.....!')
    while data_chunk:
        try:

            f.write(data_chunk)
            data_chunk = target.recv(1024)
        except socket.timeout:
            target.settimeout(None)
            print('file transfered successfully')
            data_store(file_name, file_type, str(file_size),
                       file_path, socket_obj, ip[0], scanned)
            break
    f.close()


def send_command(target, msg):
    jsondata = json.dumps(msg)
    target.send(jsondata.encode())


def recive_check(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().strip()
            return json.loads(data)
        except ValueError:
            continue

# FUNCTION TO START THE CONNUNICATION BETWEEN TWO DEVICES


def init_Sandbox(target, ip):
    while True:
        send_command(target, 'check')
        print('Sending command to check for files')
        respons = recive_check(target)

        if respons == 'not found':
            print('No files found [!!]')
            pass
        elif respons != 'not found':
            print(f'Files has been found {respons}')
            if len(respons) > 1:
                for n in respons:
                    print(f'sending request to get file {n}')
                    check_file(n, target, ip)
                    sleep(2)
            else:
                check_file(respons[0], target, ip)
        sleep(5)

# FUNCIONT TO ACCEPT MULTIBLE CONNECTION AT THE SAME TIME


def data_base():
    try:
        con = sqlite3.connect('man.db')
        cursor = con.cursor()
        cursor.execute(
            "create table if not exists FileAnalysis(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, file_name TEXT NOT NULL, file_type TEXT NOT NULL,file_size INTEGER NOT NULL, file_path TEXT NOT NULL, IP TEXT NOT NULL, scanned INTEGER NOT NULL    )")
        con.commit()
        con.close
    except Exception as Error:
        print(Error)


def connect_client():
    while len(CLIENTS) != 2:
        if stop_flag:
            break
# SETTING TIMEOUT SO THE LOOP CONTINUE LOOKING FOR OTHER CONNECTIONS FASTER
        SOK.settimeout(1)
# ACCEPTING CONNECTIONS AND APPENDING CONNECTED DEVICES TO AN ARRY
# HANDLING ERRORS BY USING TRY , EXCEPT METHOD
        try:
            tar = SOK.accept()
            client, ip = tar
            CLIENTS.append(client)
            IPS.append(ip)
            print(f"{str(ip)} Has been Connected ")
            threading.Thread(target=init_Sandbox, args=(client, ip,)).start()
        except:
            pass


# SETING THE CONNECTION FIRST
# CHOOSE THE IP WHERE IS THE SERVER LOCAL IP IS ? , AND CHOOSE PORT THAT IS NOT IN USE
IP = '192.168.1.7'
PORT = 55555
# THIS WILL BE THE LIST OF CLIENTS WILL BE ADDED TO THIS ARRAY
print(f'just assigned Ip {IP} and Port {PORT}')
CLIENTS = []
IPS = []
# INITIATE THE CONNECTION WITH SOCKET
SOK = socket.socket()
SOK.bind((IP, PORT))
SOK.listen(10)
data_base()
# TO STOP THE LOOP FOR THE CONNECTION IF NEEDED
stop_flag = False
# START THREADING TO ACCEPTE MULTIPULE CONNECTION

T = threading.Thread(target=connect_client)
T.start()
