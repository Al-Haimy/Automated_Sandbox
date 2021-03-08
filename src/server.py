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

BUFFER_SIZE = 1024


def check_file(file_name, target):
    send_command(target, 'download '+file_name)
    # file_size = int(recive_check(target))
    f = open(file_name, 'wb')
    target.settimeout(1)

    print(f'downloading the file {file_name}')
    data_chunk = target.recv(1024)

    while data_chunk:
        try:
            print(f'receiving data.....!')
            f.write(data_chunk)
            data_chunk = target.recv(1024)
        except socket.timeout:
            target.settimeout(None)
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


def init_Sandbox(target):
    while True:
        send_command(target, 'check')
        print('Sending command to check for files')
        respons = recive_check(target)
        print(f'Files has been found {respons}')
        if respons == 'not found':
            pass
        elif respons != 'not found':

            if len(respons) > 1:
                for n in respons:
                    print(f'sending request to get file {n}')
                    check_file(n, target)
                    sleep(2)
            else:
                check_file(respons[0], target)
        sleep(5)

# FUNCIONT TO ACCEPT MULTIBLE CONNECTION AT THE SAME TIME


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
            threading.Thread(target=init_Sandbox, args=(client,)).start()
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
# TO STOP THE LOOP FOR THE CONNECTION IF NEEDED
stop_flag = False
# START THREADING TO ACCEPTE MULTIPULE CONNECTION

T = threading.Thread(target=connect_client)
T.start()
