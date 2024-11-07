import tkinter as tk
import subprocess

# Funkce pro spuštění ADFGX.py
def spustit_adfgx():
    subprocess.run(["python", "ADFGX.py"])

# Funkce pro spuštění ADFGVX.py
def spustit_adfgvx():
    subprocess.run(["python", "ADFGVX.py"])

# Vytvoření hlavního okna
okno = tk.Tk()
okno.title("ADFG(V)X Šifra")

# Nadpis
nadpis = tk.Label(okno, text="ADFG(V)X Šifra", font=("Helvetica", 16, "bold"))
nadpis.pack(pady=10)

nadpis = tk.Label(okno, text="Vyber typ šifry, kterou chceš spustit.", font=("Helvetica", 14))
nadpis.pack(pady=10)

tlacitka_frame = tk.Frame(okno)
tlacitka_frame.pack(pady=5)
# Tlačítko pro spuštění ADFGX.py
tlacitko_adfgx = tk.Button(tlacitka_frame, text="ADFGX", command=spustit_adfgx, font=("Helvetica", 12))
tlacitko_adfgx.pack(side="left", padx=10)

# Tlačítko pro spuštění ADFGVX.py
tlacitko_adfgvx = tk.Button(tlacitka_frame, text="ADFGVX", command=spustit_adfgvx, font=("Helvetica", 12))
tlacitko_adfgvx.pack(side="left", padx=10)

# Spuštění GUI
okno.mainloop()
