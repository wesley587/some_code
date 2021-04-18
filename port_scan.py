from socket import *
from threading import Thread
import argparse


def checking_port(host, port):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        print(f'{host}/{port} - Open')
    except:
        pass


arguments = argparse.ArgumentParser()
arguments.add_argument('-i', required=True, action='store', dest='ip', help='IP using to scan port')
parse = arguments.parse_args()
host = parse.ip
for port in range(0, 65535):
    t = Thread(target=checking_port, args=(host, port))
    t.start()
