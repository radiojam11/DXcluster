import paho.mqtt.client as mqtt


topic = "dxc/ls/#"
mqtt_server = "mqtt.iz3mez.it"
porta = 1883

#--------------------------------   FUNZIONI X CONNESSION AL FLUSSO MQTT  -------------

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    messaggio = str(msg.payload.decode("utf-8"))
    #dizionario = json.loads(messaggio)
    #print(dizionario)
    with open('spot.txt', 'a') as spot_file:
        #spot_file.write(f'"{dizionario}"'+ '\n')
        spot_file.write(messaggio + '\n')
    
#-----------------------CREAZIONE CONNESSIONE MQTT  -----------------------
# Creare un oggetto MqttClient
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# Connessione al broker
client.connect(mqtt_server, porta)
# Sottoscrizione al topic
client.subscribe(topic)
# Processare i messaggi MQTT
client.on_message = on_message
client.loop_forever()


