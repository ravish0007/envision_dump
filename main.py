
#import usocket as socket
import socket
import machine 
import dht
import time
d = dht.DHT22(machine.Pin(14))

'''
def sendudp(host, port):
    address = ("127.0.0.1", 6969)
    data = b'hello udp'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("data is type {}".format(type(data)))

    sock.sendto(data, address)
'''
def sendtcp(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
         d.measure()
         data = 'temp: '+str(d.temperature())+' humid:'+str(d.humidity())+'\n'
         time.sleep(0.1)
         sock.send(data)
         time.sleep(5)
         print("data is type {}".format(type(data)))



    sock.close()

if __name__ == "__main__":
    sendtcp("192.168.31.213", 12345)

