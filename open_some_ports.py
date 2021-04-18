from socket import *
import threading
import argparse


def port(ip, number):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ip, int(number)))
    s.listen(1)
    s.accept()
    print(f'{number} closed')


arguments = argparse.ArgumentParser()
arguments.add_argument('-i', required=True, action='store', dest='ip', help='IP using to open ports')
arguments.add_argument('-p', required=True, action='store', dest='ports', type=str, nargs='*', help='inform the doors that will open, use the "," to separate the doors')
parser = arguments.parse_args()
host = parser.ip
ports = parser.ports
print(ports)

for x in ports:
    t = threading.Thread(target=port, args=(host, x))
    t.start()
    print(f'{x} -- open')
