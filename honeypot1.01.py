from socket import *
import os
from datetime import datetime
import winsound

def alarm():
    frequency = 2000
    duration = 1500
    winsound.Beep(frequency, duration)

def main():
    now = datetime.now()
    ip_add = ""
    port = 80
    print("[+] Honeypot started.........")
    try:
        get_socket_con = socket(AF_INET,SOCK_STREAM)
        get_socket_con.bind((ip_add,port))
        get_socket_con.listen(10)
        while 1:
            client_con,client_addr = get_socket_con.accept()
            print("Visiter found! You Have Been Attacked!. [{}]".format(client_addr[0]))
            client_con.send(b"<h1> The following activity is noted </h1>")
            data = client_con.recv(2048)
            file = open('D:\/vscode files\code files\/ransomware research\/detection_log.txt', "a")
            dtstr = now.strftime("%d/%m/%Y %H:%M:%S")
            file.write("Connection instance:  " + dtstr + "\n")
            file.write("Connection established by [{}]".format(client_addr[0]))
            file.write("\n")
            file.write(str(data))
            file.write("\n")
            print(data)
            alarm()
    except error as identifer:
        print("[+] Unspecified Error [{}]".format(identifer))
    except KeyboardInterrupt as ky:
        print("[-] Process Stopped!")
    finally:
        get_socket_con.close()
    get_socket_con.close()
if __name__ == "__main__":
    main()