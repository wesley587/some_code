import threading
from socket import *
import argparse
import os

first_exec = True

if first_exec:
    os.system('pip install python-nmap')

import nmap

args = argparse.ArgumentParser()
args.add_argument('-h', '-H', help='Host ip to do parser', dest='host', default='127.0.0.1', action='storage')
parser = args.parse_args()
host = parser.host


def checking_port(ip, port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((ip, port))
        conn.close()
        nmScan = nmap.PortScanner()
        nmScan.scan(ip, str(port))
        print(nmScan[ip])
        host_name = nmScan[ip]['hostnames'][0]['name']
        product = nmScan[ip]['tcp'][int(port)]['product']
        reason = nmScan[ip]['status']['reason']
        print(f'{ip}/{port} - open\ninformation:\nHost name: {host_name}\nProduct: {product}\nreason: {reason}\n')
    except:
        pass


for x in range(0, 150):
    t = threading.Thread(target=checking_port, args=(host, x))
    t.start()
