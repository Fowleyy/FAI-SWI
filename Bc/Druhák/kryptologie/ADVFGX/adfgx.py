import math
import random
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

global_square = {}

def tabulka(klic, jazyk="Čeština", custom_abeceda=""):
    adfgx = "ADFGX"
    
    if jazyk == "Čeština":
        abeceda = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    elif jazyk == "Angličtina":
        abeceda = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    else:
        abeceda = ""

    if custom_abeceda:
        custom_abeceda = custom_abeceda.strip().upper()
        if len(custom_abeceda) != 25:
            messagebox.showerror("Chyba", "Vlastní abeceda musí obsahovat přesně 25 znaků.")
            return None
        abeceda = custom_abeceda
    elif abeceda == "":
        abeceda = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
        
    if abeceda_combobox.get() == "Náhodná":
        abeceda = list(abeceda)
        random.shuffle(abeceda)
        abeceda = ''.join(abeceda)
    
    square = {}
    i = 0
    for row in adfgx:
        for col in adfgx:
            if i < len(abeceda):
                square[abeceda[i]] = row + col
                i += 1
    global global_square
    global_square = square
    return square


def uprava_klice(vstup):
    znaky = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ě": "e", "ů": "u", "č": "c", "ř": "r", "š": "s",
        "ť": "t", "ň": "n", "ď": "d", "ž": "z", "ý": "y"
    }
    result = ""
    for c in vstup.lower():
        if c in znaky:
            result += znaky[c]
        elif 'a' <= c <= 'z':
            result += c
    result = result.replace(" ", "").upper()
    return result

def uprava_textu(text):
    text = text.lower()
    znaky = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ě": "e", "ů": "u", "č": "c", "ř": "r", "š": "s",
        "ť": "t", "ň": "n", "ď": "d", "ž": "z", "ý": "y",
        "0": "XNULAX", "1": "XJEDNAX", "2": "XDVAX", "3": "XTRIX",
        "4": "XCTYRIX", "5": "XPETX", "6": "XSESTX", "7": "XSEDMX",
        "8": "XOSMX", "9": "XDEVETX"
    }
    result = ""
    for c in text:
        if c in znaky:
            result += znaky[c]
        elif ('a' <= c <= 'z') or ('0' <= c <= '9'):
            result += c
        elif c == " ":
            result += "XMEZERAX"
    result = result.upper()
    return result

def sifruj(text, klic, tabulka):
    filtrovany_text = uprava_textu(text)
    substituted = ''.join(tabulka.get(char, '') for char in filtrovany_text if char in tabulka)
    sloupce = len(klic)
    radky = math.ceil(len(substituted) / sloupce)
    
    matice = [''] * sloupce
    for i, char in enumerate(substituted):
        matice[i % sloupce] += char

    serazeni = sorted(range(len(klic)), key=lambda x: klic[x])
    
    result = ''.join(matice[i] for i in serazeni)
    result = ' '.join([result[i:i + 5] for i in range(0, len(result), 5)])
    return result


def desifruj(text, klic):
    text = text.replace(" ", "")
    sloupce = len(klic)
    radky = len(text) // sloupce
    extra = len(text) % sloupce

    serazeni = sorted(range(len(klic)), key=lambda x: klic[x])

    DelkaSloupce = [radky + 1 if i < extra else radky for i in range(sloupce)]
    
    SeradMatici = [''] * sloupce
    k = 0
    for i in serazeni:
        SeradMatici[i] = text[k:k + DelkaSloupce[i]]
        k += DelkaSloupce[i]
    
    dvojice = [''] * len(text)
    idx = 0
    for i in range(radky + 1):
        for col in SeradMatici:
            if i < len(col):
                dvojice[idx] = col[i]
                idx += 1

    transpozice = {v: k for k, v in global_square.items()}
    result = ''
    for i in range(0, len(dvojice), 2):
        pair = ''.join(dvojice[i:i + 2])
        result += transpozice.get(pair, '')

    result = result.replace("XMEZERAX", " ")
    result = (result.replace("XJEDNAX", "1").replace("XDVAX", "2").replace("XTRIX", "3")
                 .replace("XNULAX", "0").replace("XCTYRIX", "4").replace("XPETX", "5")
                 .replace("XSESTX", "6").replace("XSEDMX", "7").replace("XOSMX", "8").replace("XDEVETX", "9"))
    
    return result

def sifrovani():
    text = text_entry.get("1.0", tk.END)
    klic = uprava_klice(key_entry.get())
    custom_abeceda = custom_abeceda_entry.get().strip()
    vybrany_jazyk = jazyk_combobox.get()
    
    matice = tabulka(klic, jazyk=vybrany_jazyk, custom_abeceda=custom_abeceda)
    
    filtrovany_text = uprava_textu(text)
    filtrovany_text_entry.delete("1.0", tk.END)
    filtrovany_text_entry.insert(tk.END, filtrovany_text)
    
    sifrovany_text = sifruj(filtrovany_text, klic, matice)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, sifrovany_text)
    ZobrazTabulku(matice)


def desifrovani():
    text = result_entry.get("1.0", tk.END).strip()
    klic = uprava_klice(key_entry.get())
    
    if not global_square:
        custom_abeceda = custom_abeceda_entry.get().strip()
        vybrany_jazyk = jazyk_combobox.get()
        tabulka(klic, jazyk=vybrany_jazyk, custom_abeceda=custom_abeceda)
    
    desifrovany_text = desifruj(text, klic)
    result_entry.delete("1.0", tk.END)
    result_entry.insert(tk.END, desifrovany_text)
    ZobrazTabulku(global_square)



def ZobrazTabulku(square):
    tabulka = ""
    adfgx = "ADFGX"
    for row in adfgx:
        for col in adfgx:
            letter = [k for k, v in square.items() if v == row + col]
            if letter:
                tabulka += letter[0] + " "
            else:
                tabulka += "  "
        tabulka += "\n"
    matrix_label.config(text=tabulka.strip())

def zmena_abecedy(event):
    if abeceda_combobox.get() == "Náhodná":
        custom_abeceda_entry.delete(0, tk.END)
        custom_abeceda_entry.config(state="disabled")
        
    else:
        custom_abeceda_entry.config(state="normal")


root = tk.Tk()
root.title("ADFGX Šifra")
root.geometry("600x600")


header_label = tk.Label(root, text="ADFGX Šifra", font=("Helvetica", 16, "bold"))
header_label.grid(row=0, column=0, columnspan=4, pady=10)


tk.Label(root, text="Klíč:").grid(row=1, column=0, sticky="e")
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=1, column=1, sticky="w")

tk.Label(root, text="Jazyk:").grid(row=1, column=2, sticky="e")
jazyk_combobox = ttk.Combobox(root, values=["Čeština", "Angličtina"], state="readonly")
jazyk_combobox.set("Čeština")
jazyk_combobox.grid(row=1, column=3, sticky="w")


tk.Label(root, text="Typ abecedy:").grid(row=2, column=0, sticky="e")
abeceda_combobox = ttk.Combobox(root, values=["Náhodná", "Vlastní"], state="readonly")
abeceda_combobox.set("Náhodná")
abeceda_combobox.grid(row=2, column=1, sticky="w")
abeceda_combobox.bind("<<ComboboxSelected>>", zmena_abecedy)

tk.Label(root, text="Vlastní abeceda:").grid(row=2, column=2, sticky="e")
custom_abeceda_entry = tk.Entry(root, width=30)
custom_abeceda_entry.grid(row=2, column=3, sticky="w")
custom_abeceda_entry.config(state="disabled")


tk.Label(root, text="Text:").grid(row=3, column=0, columnspan=4)
text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=4, column=0, columnspan=4, pady=10)


tk.Label(root, text="Filtrovaný text:").grid(row=5, column=0, columnspan=4)
filtrovany_text_entry = tk.Text(root, height=5, width=50)
filtrovany_text_entry.grid(row=6, column=0, columnspan=4)


sifrovani_button = tk.Button(root, text="Šifrovat", command=sifrovani)
sifrovani_button.grid(row=7, column=1, pady=10)
desifrovani_button = tk.Button(root, text="Dešifrovat", command=desifrovani)
desifrovani_button.grid(row=7, column=2, pady=10)


tk.Label(root, text="Výsledek:").grid(row=8, column=0, columnspan=4)
result_entry = tk.Text(root, height=5, width=50)
result_entry.grid(row=9, column=0, columnspan=4)


tk.Label(root, text="Polybiův čtverec:").grid(row=10, column=0, columnspan=4)
matrix_label = tk.Label(root, text="", justify="left", font=("Courier", 10))
matrix_label.grid(row=11, column=0, columnspan=4)

root.mainloop()
