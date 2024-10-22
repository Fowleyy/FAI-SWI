from math import gcd
import tkinter as tk
from tkinter import messagebox
import string

def editText(vstup):
    vstup = vstup.lower()
    result = ""
    znaky = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ě": "e", "ů": "u", "č": "c", "ř": "r", "š": "s",
        "ť": "t", "ň": "n", "ď": "d", "ž": "z", "ý": "y",
        "0": "xnulax", "1": "xjednax", "2": "xdvax", "3": "xtrix",
        "4": "xctyrix", "5": "xpetx", "6": "xsestx", "7": "xsedmx",
        "8": "xosmx", "9": "xdevetx"
    }
    
    for znak in vstup:
        if znak in znaky:
            result += znaky[znak]
        elif 'a' <= znak <= 'z' or znak == ' ':  # Kontrola, zda je znak písmeno nebo mezera
            result += znak
    
    result = result.upper()
    result = result.replace(" ", "XMEZERAX")
    return result


def sifrovani(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Hodnoty klíčů musí být nesoudělné s 26.")

    source = string.ascii_uppercase
    result = ""

    for znak in text:
        if znak in source:
            c = source.index(znak)
            r = (a * c + b) % 26
            result += source[r]
    

    return ' '.join([result[i:i+5] for i in range(0, len(result), 5)])


def desifrovani(text, a, b, vstup):
    if gcd(a, 26) != 1:
        raise ValueError("Hodnoty klíčů musí být nesoudělné s 26.")

    source = string.ascii_uppercase
    result = ""
    inverzni = pow(a, -1, 26)
    text = text.replace(" ", "")

    for znak in text:
        c = source.index(znak)
        r = (inverzni * (c - b)) % 26
        result += source[r]

    result = result.replace("XMEZERAX", " ").replace("XNULAX", "0")
    result = result.replace("XJEDNAX", "1").replace("XDVAX", "2").replace("XTRIX","3")
    result = result.replace("XCTYRIX", "4").replace("XPETX", "5").replace("XSESTX", "6")
    result = result.replace("XSEDMX", "7").replace("XOSMX", "8").replace("XDEVETX", "9")
    return result


def sifruj_zprava():
    try:
        a = int(a_vstup.get())
        b = int(b_vstup.get())
        vstup = editText(text_entry.get())
        sifrovany_text = sifrovani(vstup, a, b)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, sifrovany_text)
    except ValueError as e:
        messagebox.showerror("Chyba", str(e))

def desifruj_zprava():
    try:
        a = int(a_vstup.get())
        b = int(b_vstup.get())
        vstup = editText(text_entry.get())
        desifrovany_text = desifrovani(result_text.get(1.0, tk.END).strip(), a, b, vstup)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, desifrovany_text)
    except ValueError as e:
        messagebox.showerror("Chyba", str(e))

root = tk.Tk()
root.title("Afinní šifra")
root.geometry("600x400")

font_title = ('Arial', 20, 'bold')
font_small = ('Arial', 12)
bg_color = "#f0f0f0"

root.configure(bg=bg_color)

nadpis_label = tk.Label(root, text="Afinní šifra", font=font_title, bg=bg_color)
nadpis_label.pack(pady=20)

tk.Label(root, text="Zadejte text:", font=font_small, bg=bg_color).pack(pady=5)
text_entry = tk.Entry(root, width=50, font=font_small)
text_entry.pack(pady=5)

klice_tlac = tk.Frame(root, bg=bg_color)
klice_tlac.pack(pady=10)

tk.Label(klice_tlac, text="Klíč A:", font=font_small, bg=bg_color).grid(row=0, column=0, padx=10)
a_vstup = tk.Entry(klice_tlac, font=font_small, width=5)
a_vstup.grid(row=0, column=1, padx=10)

tk.Label(klice_tlac, text="Klíč B:", font=font_small, bg=bg_color).grid(row=0, column=2, padx=10)
b_vstup = tk.Entry(klice_tlac, font=font_small, width=5)
b_vstup.grid(row=0, column=3, padx=10)

tlacitka_sif = tk.Frame(root, bg=bg_color)
tlacitka_sif.pack(pady=10)

sifruj_tlac = tk.Button(tlacitka_sif, text="Šifrovat", command=sifruj_zprava, font=font_small, width=10)
sifruj_tlac.grid(row=0, column=0, padx=10)

desifruj_tlac = tk.Button(tlacitka_sif, text="Dešifrovat", command=desifruj_zprava, font=font_small, width=10)
desifruj_tlac.grid(row=0, column=1, padx=10)

tk.Label(root, text="Výsledek:", font=font_small, bg=bg_color).pack(pady=10)
result_text = tk.Text(root, height=5, width=50, font=font_small)
result_text.pack(pady=5)

root.mainloop()
