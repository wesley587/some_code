from socket import *
from threading import Thread
import argparse


def connect(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        print(f'{ip}/{port} -- open')
    except:
        print(f'{ip}/{port} -- closed')


parser = argparse.ArgumentParser()
parser.add_argument('-i', required=True, action='store', dest='ip', help='')
parser.add_argument('-p', required=True, action='append', dest='ports', help='', nargs='*')
values = parser.parse_args()
print(values)
ports = values.ports

for x in ports:
    for port in x:
        t = Thread(target=connect, args=(values.ip, port))
        t.start()
