"""
Using python 3.8 
server side 
"""
import socket
import threading

# FUNCIONT TO ACCEPT MULTIBLE CONNECTION AT THE SAME TIME


def connect_client():
    while True:
        if stop_flag:
            break
# SETTING TIMEOUT SO THE LOOP CONTINUE LOOKING FOR OTHER CONNECTIONS FASTER
        SOK.settimeout(1)
# ACCEPTING CONNECTIONS AND APPENDING CONNECTED DEVICES TO AN ARRY
# HANDLING ERRORS BY USING TRY , EXCEPT METHOD
        try:
            print("trying to find connection")
            client, ip = SOK.accept()
            CLIENTS.append(client)
            IPS.append(ip)
            print(f"{str(ip)} Has been Connected ")
        except:
            print("Error")
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
print(f'Establishing Connection')
# TO STOP THE LOOP FOR THE CONNECTION IF NEEDED
stop_flag = False
# START THREADING TO ACCEPTE MULTIPULE CONNECTION
T = threading.Thread(target=connect_client)
T.start()
