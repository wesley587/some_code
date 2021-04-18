from socket import *
import threading


def port(ip, number):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ip, int(number)))
    s.listen(1)
    s.accept()
    print(f'{number} closed')


ports = [800, 801, 802, 803]
ip = '192.168.15.5'

for x in ports:
    t = threading.Thread(target=port, args=(ip, x))
    t.start()
    print(f'{x} -- open')
