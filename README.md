# MicropythonHomeKitTempAndHumidityMeter
HomeKit-enabled Temperature and Humidity sensor using ESP8266-01S, DHT20, Micropython and Homebridge

# YouTube Video
To learn more, check out the YouTube video I made about the Garage Door Opener

[![YouTube Video](https://img.youtube.com/vi/e1oZVVdQ5Jg/0.jpg)](https://www.youtube.com/watch?v=e1oZVVdQ5Jg)

# Setting up the hardware
The circuit is quite simple.

* Connect IO0 on the ESP to SCL on the DHT20
* Connect IO2 on the ESP to SDA on the DHT20

* Connect 3V3 on the ESP and + on the DHT20 to +3.3V
* Connect GND on the ESP and - on the DHT20 to Ground

# Installation on the ESP8266
Make sure that you have a recent Micropython firmware installed on your ESP8266.

Edit the wifi setting in the config.py and upload it together with boot.py, dht20.py and main.py to the ESP9266 using your favourite tool such as Thonny.

# Connecting to Homebridge

In order to connect the Pi Pico to Homebridge, I'm using the HTTP Advanced Accessory plugin by staromeste.

You can find the plugin here: https://github.com/staromeste/homebridge-http-advanced-accessory

This plugin is very powerful, but not very user friendly as it needs to be configured using JSON to talk to and understand accessories.

But that's ok, because I have provided config files for both temperature and humidity in the "homebridge-http-advanced-accessory config" folder.

Just change the IP address in the URL and add them to homebridge-http-advanced-accessory.
