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
        SOCK.settimeout(1)
# ACCEPTING CONNECTIONS AND APPENDING CONNECTED DEVICES TO AN ARRY
# HANDLING ERRORS BY USING TRY , EXCEPT METHOD 
        try: 
            client, ip = SOCK.accept()
            CLIENTS.append(client)
            IPS.append(ip)
            print(f"{str(ip)} Has been Connected ")
        except:
            pass
# SETING THE CONNECTION FIRST 
# CHOOSE THE IP WHERE IS THE SERVER LOCAL IP IS ? , AND CHOOSE PORT THAT IS NOT IN USE
IP = '192.168.1.1'
PORT = 54545
# THIS WILL BE THE LIST OF CLIENTS WILL BE ADDED TO THIS ARRAY 
CLIENTS = [] 
IPS = [] 
# INITIATE THE CONNECTION WITH SOCKET 
SOCK  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
SOCK.bind((IP, PORT))
# TO STOP THE LOOP FOR THE CONNECTION IF NEEDED 
stop_flag = False 
# START THREADING TO ACCEPTE MULTIPULE CONNECTION 
T = threading.Thread(target=connect_client)
T.start()