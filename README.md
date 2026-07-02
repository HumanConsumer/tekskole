
import network
import time
import socket



from neopixel import Neopixel
from utime import sleep
from farve import FARVE, REGNBUE_SEKVENS

ssid = "wifinavn"
word = "wifipassword"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, word)
if not wlan.isconnected():
    sæt_farve_lampe(FARVE['lilla'],255)
    time.sleep(1)

    netværk = wlan.scan()
    for n in netværk:
        ssid = n[0].decode('utf-8')
        signal_styrke = n[3] # RSSI (jo tættere på 0, jo bedre. F.eks. -50 er godt, -90 er dårligt)
        print(f"Netværk: {ssid} | Signalstyrke: {signal_styrke} dBm")

    sæt_farve_lampe(FARVE['grøn'],255)
    time.sleep(1)
sæt_farve_lampe(FARVE['rød'],255)

while not wlan.isconnected():
    print("Connecting...")
    time.sleep(1)

print("Connected, IP:", wlan.ifconfig()[0])
sæt_farve_lampe(FARVE['blå'],255)

while True:
    while not wlan.isconnected():
        print("Connecting...")
        time.sleep(1)
