import tkinter as tk
import subprocess


def spustit_afinni():
    subprocess.run(["python", "./afinni/main.py"])

def spustit_playfair():
    subprocess.run(["python", "./playfare/main.py"])

def spustit_adfgx():
    subprocess.run(["python", "./ADVFGX/ADFGX.py"])

def spustit_adfgvx():
    subprocess.run(["python", "./ADVFGX/ADFGVX.py"])

def spustit_rsa():
    subprocess.run(["python", "./RSA/main.py"])

def spustit_dsa():
    subprocess.run(["python", "./DSA/main.py"])


okno = tk.Tk()
okno.title("Kryptologie")
okno.geometry("500x200")

nadpis = tk.Label(okno, text="Kryptologie", font=("Helvetica", 16, "bold"))
nadpis.pack(pady=10)

nadpis = tk.Label(okno, text="Vyber typ šifry, kterou chceš spustit.", font=("Helvetica", 14))
nadpis.pack(pady=10)

tlacitka_frame = tk.Frame(okno)
tlacitka_frame.pack(pady=5)

tlacitko_afinni = tk.Button(tlacitka_frame, text="Afinní", command=spustit_afinni, font=("Helvetica", 12))
tlacitko_afinni.pack(side="left", padx=10)

tlacitko_playfair = tk.Button(tlacitka_frame, text="PlayFair", command=spustit_playfair, font=("Helvetica", 12))
tlacitko_playfair.pack(side="left", padx=10)

tlacitko_adfgx = tk.Button(tlacitka_frame, text="ADFGX", command=spustit_adfgx, font=("Helvetica", 12))
tlacitko_adfgx.pack(side="left", padx=10)

tlacitko_adfgvx = tk.Button(tlacitka_frame, text="ADFGVX", command=spustit_adfgvx, font=("Helvetica", 12))
tlacitko_adfgvx.pack(side="left", padx=10)

tlacitko_rsa = tk.Button(tlacitka_frame, text="RSA", command=spustit_rsa, font=("Helvetica", 12))
tlacitko_rsa.pack(side="left", padx=10)

tlacitko_dsa = tk.Button(tlacitka_frame, text="DSA", command=spustit_dsa, font=("Helvetica", 12))
tlacitko_dsa.pack(side="left", padx=10)

# Spuštění GUI
okno.mainloop()
