import tkinter as tk
from tkinter import messagebox
from math import gcd
import string


def odstranit_diakritiku(text):
    # Odstraní diakritiku a ponechá pouze alfanumerické znaky a mezery
    text_bez_diakritiky = ''.join(c for c in text if c.isalnum() or c.isspace())
    return text_bez_diakritiky


def sifruj(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Hodnoty klíčů musí být nesoudělné s 26.")

    abeceda = string.ascii_uppercase
    cisla = string.digits
    text = odstranit_diakritiku(text).upper()

    sifrovany_text = []

    for znak in text:
        if znak in abeceda:
            index = abeceda.index(znak)
            sifrovany_znak = abeceda[(a * index + b) % 26]
            sifrovany_text.append(sifrovany_znak)

        elif znak in cisla:
            index = cisla.index(znak)
            sifrovany_znak = cisla[(a * index + b) % 10]
            sifrovany_text.append(sifrovany_znak)

        elif znak == " ":
            sifrovany_text.append("XMEZERAX")  # Šifrujeme mezeru jako "XMEZERAX"

    # Rozdělení na bloky po 5 znacích
    bloky = [''.join(sifrovany_text[i:i + 5]) for i in range(0, len(sifrovany_text), 5)]
    return ''.join(bloky)


def desifruj(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Hodnoty klíčů musí být nesoudělné s 26.")

    abeceda = string.ascii_uppercase
    cisla = string.digits
    inverzni = pow(a, -1, 26)

    desifrovany_text = []

    # Nahrazení "XMEZERAX" zpět na mezeru
    text = text.replace("XMEZERAX", " ")

    for znak in text:
        if znak in abeceda:
            index = abeceda.index(znak)
            desifrovany_znak = abeceda[(inverzni * (index - b)) % 26]
            desifrovany_text.append(desifrovany_znak)

        elif znak in cisla:
            index = cisla.index(znak)
            desifrovany_znak = str((inverzni * (index - b)) % 10)
            desifrovany_text.append(desifrovany_znak)

    return ''.join(desifrovany_text)


def zpracuj_text(typ):
    try:
        text = vstup_text.get("1.0", tk.END).strip()
        a = int(vstup_a.get())
        b = int(vstup_b.get())

        if typ == "sifruj":
            vysledek = sifruj(text, a, b)
        else:
            vysledek = desifruj(text, a, b)

        vystup_text.delete("1.0", tk.END)
        vystup_text.insert(tk.END, vysledek)

    except ValueError as e:
        messagebox.showerror("Chyba", str(e))


root = tk.Tk()
root.title("Šifra")

label_vstup = tk.Label(root, text="Zadejte text:")
label_vstup.pack()
vstup_text = tk.Text(root, height=5, width=30)
vstup_text.pack()

label_a = tk.Label(root, text="Zadejte klíč a:")
label_a.pack()
vstup_a = tk.Entry(root)
vstup_a.pack()

label_b = tk.Label(root, text="Zadejte klíč b:")
label_b.pack()
vstup_b = tk.Entry(root)
vstup_b.pack()

button_sifrovat = tk.Button(root, text="Zašifrovat", command=lambda: zpracuj_text("sifruj"))
button_sifrovat.pack()

button_desifrovat = tk.Button(root, text="Dešifrovat", command=lambda: zpracuj_text("desifruj"))
button_desifrovat.pack()

label_vystup = tk.Label(root, text="Výsledek:")
label_vystup.pack()
vystup_text = tk.Text(root, height=5, width=30)
vystup_text.pack()

root.mainloop()
