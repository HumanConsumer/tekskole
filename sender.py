import socket


# skriv pico ip her
PICO_IP = "192.168.137.124"  
PICO_PORT = 8080           #skriv pico port

# Opret UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_kommando_til_pico(tal_liste):
    try:
        # 1. Konverter listen af tal [1, 2, 255...] til en streng adskilt af mellemrum: "1 2 255..."
        kommando_streng = " ".join(str(tal) for tal in tal_liste)
        
        # 2. Opret en TCP socket (standard socket.socket() uden parametre er TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Sæt en timeout så computeren ikke hænger evigt, hvis Picoen er slukket
        sock.settimeout(5.0) 
        
        # 3. Forbind til Pico og send data
        sock.connect((PICO_IP, PICO_PORT))
        sock.sendall(kommando_streng.encode('utf-8'))
        
        # 4. Modtag svar tilbage fra Pico (cl.send(b"OK\n"))
        svar = sock.recv(1024).decode().strip()
        print(f"Succes! Sendte: [{kommando_streng}] | Svar fra Pico: {svar}")
        
        # 5. Luk forbindelsen
        sock.close()
        return svar
        
    except Exception as e:
        print(f"Fejl under kommunikation med Pico: {e}")
        return None
    



while True:
    besked = input("send en besked")
    
    if not besked.strip():
        continue
        
    try:
        #Opdel teksten ved hvert mellemrum
        tekst_liste = besked.split()
        
        #lav alle tallende til et array
        tal_array = [int(x) for x in tekst_liste]
        
        send_kommando_til_pico(tal_array)
        
    except ValueError:
        print("Fejl: Du må kun skrive tal adskilt af mellemrum! Prøv igen.")
    
