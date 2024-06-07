import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import paho.mqtt.client as mqtt
import json
from time import sleep
from threading import Thread

topic = "dxc/ls/#"
mqtt_server = "mqtt.iz3mez.it"
porta = 1883
cont = 1


# FONT
carattere = "Helvetica"
#carattere = "Helvetica"

# COLORI
colore_team = "#06B5C3"
colore_punti = "#E85811"
colore_tempo = "#31A745"

#------------------------Creo il testo da stampare nella tabella
# dizionario Tipo 
dizionario = {
  "spot_datetime_utc": "04/06/2024 11:30:08",
  "spot_time": "1130Z",
  "band": "6",
  "frequency": "50313.0",
  "spotted": "BG9MM",
  "spotted_dxcc": "318",
  "spotted_country": "CHINA",
  "spotted_continent": "AS",
  "spotter": "LZ2CC",
  "spotter_dxcc": "212",
  "spotter_country": "BULGARIA",
  "spotter_continent": "EU",
  "spotter_comment": "FT8 -17 dB 2014 Hz"
}

testo = "Data UTC: {}\nBanda: {} - Frequenza: {}\nNominativo: {}\nDXcc: {} - Country: {} - {}\nAscolto di: {} in {} - {}\nNote: {}".format(dizionario["spot_datetime_utc"], dizionario["band"], dizionario["frequency"], dizionario["spotted"], dizionario["spotted_dxcc"], dizionario["spotted_country"], dizionario["spotted_continent"], dizionario["spotter"], dizionario["spotter_country"], dizionario["spotter_continent"], dizionario["spotter_comment"])

#-------------------------------  CREAZIONE GUI  --------------------------
#--------------------------------  Geastione GUI  --------------------------

# Funzione che si occupa di aggiornare il testo pubblicato    
def aggiornaGUI():
    global cont       
    # aggiorno i dati sulla GUI
    text1.config(text="w")
    text2.config(text="2")
    text3.config(text="3")
    text4.config(text="4")
    text5.config(text="5")
    text6.config(text="6")
    text7.config(text="7")
    text8.config(text="8")
    cont = 1
    #cerca_messaggio()
    root.after(1000, aggiornaGUI)
# root window
root = tk.Tk()
root.geometry("1200x800")
root.title('Spots DXcluster by IK5JAM')
root.resizable(0, 0)
root['bg'] = 'black'
#root.configure(bg="#87CEEB")


# Creare i riquadri
frame1 = tk.Frame(root, bg="#87CEEB")
frame1.pack(side="left", fill="both", expand=True)

frame2 = tk.Frame(root, bg="#87CEEB")
frame2.pack(side="right", fill="both", expand=True)

# Creare i riquadri interni
r1 = tk.Frame(frame1, bg="#87CEEB")
r1.pack(side="top", fill="both", expand=True)

r2 = tk.Frame(frame1, bg="#87CEEB")
r2.pack(side="bottom", fill="both", expand=True)

r3 = tk.Frame(frame2, bg="#87CEEB")
r3.pack(side="top", fill="both", expand=True)

r4 = tk.Frame(frame2, bg="#87CEEB")
r4.pack(side="bottom", fill="both", expand=True)

# Creare i testi
text1 = tk.Label(r1, text="Testo 1", font=tkfont.Font(family="Helvetica", size=24))
text1.pack(side="left", fill="both", expand=True)

text2 = tk.Label(r1, text="Testo 2", font=tkfont.Font(family="Helvetica", size=24))
text2.pack(side="right", fill="both", expand=True)

text3 = tk.Label(r2, text="Testo 3", font=tkfont.Font(family="Helvetica", size=24))
text3.pack(side="left", fill="both", expand=True)

text4 = tk.Label(r2, text="Testo 4", font=tkfont.Font(family="Helvetica", size=24))
text4.pack(side="right", fill="both", expand=True)

text5 = tk.Label(r3, text="Testo 5", font=tkfont.Font(family="Helvetica", size=24))
text5.pack(side="left", fill="both", expand=True)

text6 = tk.Label(r3, text="Testo 6", font=tkfont.Font(family="Helvetica", size=24))
text6.pack(side="right", fill="both", expand=True)

text7 = tk.Label(r4, text="Testo 7", font=tkfont.Font(family="Helvetica", size=24))
text7.pack(side="left", fill="both", expand=True)

text8 = tk.Label(r4, text="Testo 8", font=tkfont.Font(family="Helvetica", size=24))
text8.pack(side="right", fill="both", expand=True)


# ******************************************  GUI END *********************************



#--------------------------------   FUNZIONI X CONNESSION AL FLUSSO MQTT  -------------

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global cont
    global dizionario
    messaggio = str(msg.payload.decode("utf-8"))
    dizionario = json.loads(messaggio)
    print(dizionario)
    print("sono dopo dictionary")
    cont = 0
    

#------------------------ LETTURA DEI MESSAGGI MQTT -------------
def cerca_messaggio():
    global cont
    while cont:
        cont = 1
        # Leggere i messaggi MQTT
        client.loop_read()
        client.message_callback()
        print("sono dentro while")
        sleep(1)
        


def modif_tabella(dizionario):
    # aggiorno i dati sulla GUI
    print("sono dentro tabella")
    text1.config(text="w")
    text2.config(text="2")
    text3.config(text="3")
    text4.config(text="4")
    text5.config(text="5")
    text6.config(text="6")
    text7.config(text="7")
    text8.config(text="8")
    
#-----------------------CREAZIONE CONNESSIONE MQTT  -----------------------
# Creare un oggetto MqttClient
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# Connessione al broker
client.connect(mqtt_server, porta)
# Sottoscrizione al topic
client.subscribe(topic)
# Processare i messaggi MQTT
client.on_message = on_message
#cerca_messaggio()
#client.loop_forever()
client.loop_start()
while True:
    cerca_messaggio()
    modif_tabella(dizionario)


# Fermare il loop
client.loop_stop()


"""
print("sono passato da qui")
aggiornaGUI()
print("NON crwedo che passera mai da qui - e invece ci passa tie!")
root.mainloop()
"""





