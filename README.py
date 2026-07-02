import network
import time
import socket



from neopixel import Neopixel
from utime import sleep
from farve import FARVE, REGNBUE_SEKVENS

ssid = "navn"
word = "password!!!"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, word)

trekantNum = [[0,42],[43,62],[63,82],[83,102],[103,122],]

pixels=Neopixel(trekantNum[-1][-1]+1,0,0,"GRB")

# Funktion til at lave en gradient i hver trekant
# trekant: 0-4 - valg af trekant
# farve1: hvilken farve der skal startes fra. Se farve.py for mulige farver
# farve2: hvilken farve der skal gradieres til
# lysstyrke: 0-255
def sæt_gradient_trekant(trekant, farve1, farve2, lysstyrke):
    start_pixel = trekantNum[trekant][0]
    slut_pixel = trekantNum[trekant][-1]
    pixels.set_pixel_line_gradient(start_pixel, slut_pixel, farve1, farve2, lysstyrke)
    pixels.show()
# Funktion der sætter farven i en hel trekant.
# trekant: 0-4 - valg af trekant
# farve: se filen farve.py for de farver der kan tilgås
# lysstyrke: 0-255
def sæt_farve_trekant(trekant, farve, lysstyrke):
    start_pixel = trekantNum[trekant][0]
    slut_pixel = trekantNum[trekant][-1]
    pixels.set_pixel_line(start_pixel, slut_pixel, farve, lysstyrke)
    pixels.show()


# Funktion til at lave en gradient i over hele lampen
# farve1: hvilken farve der skal startes fra. Se farve.py for mulige farver
# farve2: hvilken farve der skal gradieres til
# lysstyrke: 0-255
def sæt_gradient_lampe(farve1, farve2, lysstyrke):
    start_pixel = trekantNum[0][0]
    slut_pixel = trekantNum[-1][-1]
    pixels.set_pixel_line_gradient(start_pixel, slut_pixel, farve1, farve2, lysstyrke)
    pixels.show()
    
# Funktion der sætter farven i hele lampen.
# farve: se filen farve.py for de farver der kan tilgås
# lysstyrke: 0-255
def sæt_farve_lampe(farve, lysstyrke):
    pixels.brightness(lysstyrke)
    pixels.fill(farve)
    pixels.show()
    
# Funktion der laver en gradient i de fire foreste trekanter
# farve1: hvilken farve der skal startes fra. Se farve.py for mulige farver
# farve2: hvilken farve der skal gradieres til
# lysstyrke: 0-255
def sæt_gradient_forside(farve1, farve2, lysstyrke):
    start_pixel = trekantNum[1][0]
    slut_pixel = trekantNum[-1][-1]
    pixels.set_pixel_line_gradient(start_pixel, slut_pixel, farve1, farve2, lysstyrke)
    pixels.show()


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
