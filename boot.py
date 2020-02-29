
#try:
 

# import usocket as socket
#except:
import socket

import time
#import webrepl
#webrepl.start()

import machine 

p = machine.Pin(2,machine.Pin.OUT)

import dht
d = dht.DHT22(machine.Pin(14))

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Envision Lab'
password = 'envision'

sp = network.WLAN(network.STA_IF)
sp.active(True)
sp.connect(ssid, password)

while sp.isconnected() == False:
	p.value(0);time.sleep(0.1);p.value(1)
  

p.value(1)
host, port = ("192.168.31.213", 12345)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
while True:
         d.measure()
         tem,hum = d.temperature(),d.humidity()
         data = 'temperature: '+str(tem)+'humidity: '+str(hum)+'\n'
         sock.send(data); time.sleep(5)
