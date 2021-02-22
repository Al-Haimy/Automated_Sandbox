"""
Using python 3.8 
server side 
"""
import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# FUNCIONT TO ACCEPT MULTIBLE CONNECTION AT THE SAME TIME


def init_Sandbox():


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
            TARGETS.append(tar)
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
TARGETS = []
# INITIATE THE CONNECTION WITH SOCKET
SOK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOK.bind((IP, PORT))
SOK.listen(10)
# TO STOP THE LOOP FOR THE CONNECTION IF NEEDED
stop_flag = False
# START THREADING TO ACCEPTE MULTIPULE CONNECTION
T = threading.Thread(target=connect_client)
T.start()


while True:
    if len(IPS) == 0:
        pass
    elif len(IPS) == 1:
        init_Sandbox(CLIENTS[0], IPS[0])
    elif len(IPS) > 1:
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(init_Sandbox, TARGETS)
