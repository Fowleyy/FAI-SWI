import tkinter as tk
from tkinter import messagebox
from math import gcd
import unicodedata
import string


def odstranit_diakritiku(text):
    text_bez_diakritiky = ''.join(
        (c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    )
    text_bez_znaku = ''.join(c for c in text_bez_diakritiky if c.isalnum() or c.isspace())
    
    return text_bez_znaku


def sifruj(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Hodnoty klíčů musí být nesoudělné s 26.")

    abeceda = string.ascii_uppercase
    cisla = string.digits
    text = odstranit_diakritiku(text).upper()

    sifrovany_text = []
    mezery_pozice = []
    
    for i, znak in enumerate(text):
        if znak in abeceda:
            index = abeceda.index(znak)
            sifrovany_znak = abeceda[(a * index + b) % 26]
            sifrovany_text.append(sifrovany_znak)

        elif znak in cisla:
            index = cisla.index(znak)
            sifrovany_znak = cisla[(a * index + b) % 10]
            sifrovany_text.append(sifrovany_znak)

        elif znak == " ":
            mezery_pozice.append(i)

        else:
            sifrovany_text.append(znak)


    sifrovany_text_str = ''.join(sifrovany_text)
    
    rozdeleny_text = ' '.join([sifrovany_text_str[i:i+5] for i in range(0, len(sifrovany_text_str), 5)])

    return rozdeleny_text, mezery_pozice



def desifruj(text, a, b, mezery_pozice):
    if gcd(a, 26) != 1:
        raise ValueError("Hodnoty klíčů musí být nesoudělné s 26.")

    abeceda = string.ascii_uppercase
    cisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #Tady nemůže být string.digits, jinak to nefungovalo. Nevím proč.
    inverzni = pow(a, -1, 26)

    desifrovany_text = []
    
    text = text.replace(" ", "")

    for znak in text:
        if znak in abeceda:
            index = abeceda.index(znak)
            desifrovany_znak = abeceda[(inverzni * (index - b)) % 26]
            desifrovany_text.append(desifrovany_znak)

        elif znak in cisla:
            index = cisla.index(znak)
            desifrovany_znak = (a * index + b) % 10
            desifrovany_text.append(desifrovany_znak)

        else:
            desifrovany_text.append(znak)

    desifrovany_text_str = ''.join(desifrovany_text)
    
    for pozice in mezery_pozice:
        desifrovany_text_str = desifrovany_text_str[:pozice] + " " + desifrovany_text_str[pozice:]

    return desifrovany_text_str


def zpracuj_text(typ):
    try:
        text = vstup_text.get("1.0", tk.END).strip()
        a = int(vstup_a.get())
        b = int(vstup_b.get())

        if typ == "sifruj":
            vysledek, mezery_pozice = sifruj(text, a, b)
            global posledni_mezery  # Uložíme pozice mezer globálně pro dešifrování
            posledni_mezery = mezery_pozice
        else:
            vysledek = desifruj(text, a, b, posledni_mezery)

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


pismena = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
indexy = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25"

label_nezasifrovana = tk.Label(root, text=f"\nNezašifrovaná:\n{pismena}")
label_nezasifrovana.pack()

label_zasifrovana = tk.Label(root, text=f"Zašifrovaná:\n{indexy}")
label_zasifrovana.pack()

root.mainloop()
