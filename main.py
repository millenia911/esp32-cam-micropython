from machine import Pin
p = Pin(0, Pin.IN)
if p.value():
    import webcam
    webcam.run()
else:
    print('serial mode on, skip webcam')
    pass
'''
import camera
import machine
from config import app_config
from webserver import webcam

server = webcam()
server.run(app_config)
'''