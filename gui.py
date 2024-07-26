import tkinter as tk
from tkinter import font as tkfont
import json

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # Apri il file di input in modalità lettura
        with open('spot.txt', 'r') as input_file:
            i = 0
            lista_spot= []
            for line in input_file:
                if i == 8:
                    break 
                dizionario = json.loads(line)
                testo = "Data UTC: {}\nBanda: {} - Frequenza: {}\nNominativo: {}\nDXcc: {} - Country: {} - {}\nAscolto di: {} in {} - {}\nNote: {}".format(dizionario["spot_datetime_utc"], dizionario["band"], dizionario["frequency"], dizionario["spotted"], dizionario["spotted_dxcc"], dizionario["spotted_country"], dizionario["spotted_continent"], dizionario["spotter"], dizionario["spotter_country"], dizionario["spotter_continent"], dizionario["spotter_comment"])
                lista_spot.append(testo)
                i = i + 1

        # Creare la finestra principale
        self.window = tk.Tk()
        self.window.title("Applicazione Tkinter")
        self.window.geometry("800x600")
        self.window.configure(bg="#87CEEB")

        # Creare i riquadri
        self.frame1 = tk.Frame(self.window, bg="#87CEEB")
        self.frame1.pack(side="left", fill="both", expand=True)

        self.frame2 = tk.Frame(self.window, bg="#87CEEB")
        self.frame2.pack(side="right", fill="both", expand=True)

        # Creare i riquadri interni
        self.r1 = tk.Frame(self.frame1, bg="#87CEEB")
        self.r1.pack(side="top", fill="both", expand=True)

        self.r2 = tk.Frame(self.frame1, bg="#87CEEB")
        self.r2.pack(side="bottom", fill="both", expand=True)

        self.r3 = tk.Frame(self.frame2, bg="#87CEEB")
        self.r3.pack(side="top", fill="both", expand=True)

        self.r4 = tk.Frame(self.frame2, bg="#87CEEB")
        self.r4.pack(side="bottom", fill="both", expand=True)

        # Creare i testi
        self.text1 = tk.Label(self.r1, text=lista_spot[0], font=tkfont.Font(family="Helvetica", size=24))
        self.text1.pack(side="left", fill="both", expand=True)

        self.text2 = tk.Label(self.r1, text=lista_spot[1], font=tkfont.Font(family="Helvetica", size=24))
        self.text2.pack(side="right", fill="both", expand=True)

        self.text3 = tk.Label(self.r2, text=lista_spot[2], font=tkfont.Font(family="Helvetica", size=24))
        self.text3.pack(side="left", fill="both", expand=True)

        self.text4 = tk.Label(self.r2, text=lista_spot[3], font=tkfont.Font(family="Helvetica", size=24))
        self.text4.pack(side="right", fill="both", expand=True)

        self.text5 = tk.Label(self.r3, text=lista_spot[4], font=tkfont.Font(family="Helvetica", size=24))
        self.text5.pack(side="left", fill="both", expand=True)

        self.text6 = tk.Label(self.r3, text=lista_spot[5], font=tkfont.Font(family="Helvetica", size=24))
        self.text6.pack(side="right", fill="both", expand=True)

        self.text7 = tk.Label(self.r4, text=lista_spot[6], font=tkfont.Font(family="Helvetica", size=24))
        self.text7.pack(side="left", fill="both", expand=True)

        self.text8 = tk.Label(self.r4, text=lista_spot[7], font=tkfont.Font(family="Helvetica", size=24))
        self.text8.pack(side="right", fill="both", expand=True)

        # Avviare la finestra
        self.window.mainloop()

if __name__ == "__main__":
    app = Application()
