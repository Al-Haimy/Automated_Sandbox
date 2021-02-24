"""
Using python 3.8 
server side 
"""
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
import json

# FUNCIONT TO ACCEPT MULTIBLE CONNECTION AT THE SAME TIME


def send_command(target):
    jsondata = json.dumps('check')
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
        send_command(target)
        respons = recive_check(target)
        print(respons)


def connect_client():
    while True:
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
        except:
            pass


# SETING THE CONNECTION FIRST
# CHOOSE THE IP WHERE IS THE SERVER LOCAL IP IS ? , AND CHOOSE PORT THAT IS NOT IN USE
IP = '192.168.1.2'
PORT = 55555
# THIS WILL BE THE LIST OF CLIENTS WILL BE ADDED TO THIS ARRAY
print(f'just assigned Ip {IP} and Port {PORT}')
CLIENTS = []
IPS = []
# INITIATE THE CONNECTION WITH SOCKET
SOK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOK.bind((IP, PORT))
SOK.listen(10)
# TO STOP THE LOOP FOR THE CONNECTION IF NEEDED
stop_flag = False
# START THREADING TO ACCEPTE MULTIPULE CONNECTION
T = threading.Thread(target=connect_client)
T.start()

# CHECK HOW MANY DEVICES WAS FOUND AND THEN START THE PROCESS
while True:
    if len(IPS) == 0:
        pass
    elif len(IPS) == 1:
        init_Sandbox(CLIENTS[0])
    elif len(IPS) > 1:
        for n in CLIENTS:
            Process(target=init_Sandbox, args=(n,)).start()
