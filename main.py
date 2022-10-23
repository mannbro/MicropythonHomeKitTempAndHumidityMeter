from machine import Pin
from machine import I2C
from dht20 import DHT20
import socket
from uselect import select


i2c = I2C(scl=Pin(0), sda=Pin(2), freq=100000)
dht20 = DHT20(i2c)

#Handle an incoming request
def handleRequest(conn, address):
    request = conn.recv(1024)
    request = str(request)

    #Response in JSON format
    response='{"temperature": '+str(dht20.dht20_temperature())+', "humidity": '+str(dht20.dht20_humidity())+'}'
 
    print(response)
    conn.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
    conn.send(response)
    conn.close()

#Set up a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)

#Main Loop
while True:

    #The ESP8266 tends to drop connections, so check if wifi is connected, if not, reconnect
    if wifi.isconnected() == False:
        print('Connecting wifi...')
        connectWifi()

    #Handle incoming HTTP requests in a non-blocking way
    r, w, err = select((s,), (), (), 1)

    #Is there an incoming request? If so, handle the request
    if r:
        for readable in r:
            conn, addr = s.accept()
            try:
                handleRequest(conn, addr)
            except OSError as e:
                pass

    