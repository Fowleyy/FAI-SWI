import tkinter as tk
import subprocess


def spustit_adfgx():
    subprocess.run(["python", "ADFGX.py"])


def spustit_adfgvx():
    subprocess.run(["python", "ADFGVX.py"])

okno = tk.Tk()
okno.title("ADFG(V)X Šifra")

# Nadpis
nadpis = tk.Label(okno, text="ADFG(V)X Šifra", font=("Helvetica", 16, "bold"))
nadpis.pack(pady=10)

nadpis = tk.Label(okno, text="Vyber typ šifry, kterou chceš spustit.", font=("Helvetica", 14))
nadpis.pack(pady=10)

tlacitka_frame = tk.Frame(okno)
tlacitka_frame.pack(pady=5)

tlacitko_adfgx = tk.Button(tlacitka_frame, text="ADFGX", command=spustit_adfgx, font=("Helvetica", 12))
tlacitko_adfgx.pack(side="left", padx=10)

tlacitko_adfgvx = tk.Button(tlacitka_frame, text="ADFGVX", command=spustit_adfgvx, font=("Helvetica", 12))
tlacitko_adfgvx.pack(side="left", padx=10)


okno.mainloop()
