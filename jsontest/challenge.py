import datetime as dt
import socket

today = dt.datetime.today()
ipaddress = socket.gethostbyname(socket.gethostname())
hosts = list()

def main():
    print(today)
    print(ipaddress)

    with open('myservers.txt','r') as f:
        hosts = f.readlines()

    dictionary = {"json":{"time":today, "ip":ipaddress, "mysvrs":hosts}}
    print(dictionary)

if __name__ == '__main__':
    main()


