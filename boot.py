import config
import network
import esp
esp.osdebug(None)

import gc
gc.collect()



wifi = network.WLAN(network.STA_IF)

#Connect to WiFi
def connectWifi():
    global wifi

    wifi.active(True)
    wifi.connect(config.ssid, config.password)

    while wifi.isconnected() == False:
        pass

    print('Connection successful')
    print(wifi.ifconfig())

connectWifi()
