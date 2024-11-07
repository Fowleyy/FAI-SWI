import random
import math
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

global_matice = {}

def tabulka(klic, custom_abeceda=""):
    adfgvx = "ADFGVX"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    if custom_abeceda:
        custom_abeceda = ''.join(sorted(set(custom_abeceda.strip().upper())))
        if len(custom_abeceda) != 36:
            messagebox.showerror("Chyba", "Vlastní abeceda musí obsahovat přesně 36 znaků.")
            return None
        alphabet = custom_abeceda

    if abeceda_combobox.get() == "Náhodná":
        alphabet = list(alphabet)
        random.shuffle(alphabet)
        alphabet = ''.join(alphabet)

    matice = {}
    i = 0
    for row in adfgvx:
        for col in adfgvx:
            if i < len(alphabet):
                matice[alphabet[i]] = row + col
                i += 1

    global global_matice
    global_matice = matice
    return matice

def uprava_klice(input):
    characters = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ě": "e", "ů": "u", "č": "c", "ř": "r", "š": "s",
        "ť": "t", "ň": "n", "ď": "d", "ž": "z", "ý": "y"
    }
    result = ""
    for c in input.lower():
        if c in characters:
            result += characters[c]
        elif 'a' <= c <= 'z':
            result += c
    result = result.replace(" ", "").upper()
    return result

def uprava_textu(text):
    text = text.lower()
    characters = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ě": "e", "ů": "u", "č": "c", "ř": "r", "š": "s",
        "ť": "t", "ň": "n", "ď": "d", "ž": "z", "ý": "y",
        "0": "XNULAX", "1": "XEDNAX", "2": "XDVAX", "3": "XTRIX",
        "4": "XCTYRIX", "5": "XPETX", "6": "XSESTX", "7": "XSEDMX",
        "8": "XOSMX", "9": "XDEVETX"
    }
    result = ""
    for c in text:
        if c in characters:
            result += characters[c]
        elif c.isalnum():
            result += c
        elif c == " ":
            result += "XMEZERAX"
    result = result.upper()
    return result

def sifruj(text, klic, matice):
    text = uprava_textu(text)
    substituted = ''.join(matice.get(char, '') for char in text if char in matice)
    sloupce = len(klic)
    radky = math.ceil(len(substituted) / sloupce)
    matice = [''] * sloupce
    for i, char in enumerate(substituted):
        matice[i % sloupce] += char
    serazeny_klic = sorted(range(len(klic)), key=lambda x: klic[x])
    result = ''.join(matice[i] for i in serazeny_klic)

    result = ' '.join([result[i:i + 5] for i in range(0, len(result), 5)])
    return result

def desifruj(text, klic):
    text = text.replace(" ", "")
    sloupce = len(klic)
    radky = len(text) // sloupce
    extra = len(text) % sloupce
    
    serazeny_klic = sorted(range(len(klic)), key=lambda x: klic[x])
    delka_sloupec = [radky + 1 if i < extra else radky for i in range(sloupce)]
    serazena_matice = [''] * sloupce
    k = 0
    for i in serazeny_klic:
        serazena_matice[i] = text[k:k + delka_sloupec[i]]
        k += delka_sloupec[i]
    
    dvojice = [''] * len(text)
    idx = 0
    for i in range(radky + 1):
        for col in serazena_matice:
            if i < len(col):
                dvojice[idx] = col[i]
                idx += 1

    transpozice = {v: k for k, v in global_matice.items()}
    result = ''
    for i in range(0, len(dvojice), 2):
        pair = ''.join(dvojice[i:i + 2])
        result += transpozice.get(pair, '')

    result = result.replace("XMEZERAX", " ")
    result = (result.replace("XEDNAX", "1").replace("XDVAX", "2").replace("XTRIX", "3")
                 .replace("XNULAX", "0").replace("XCTYRIX", "4").replace("XPETX", "5")
                 .replace("XSESTX", "6").replace("XSEDMX", "7").replace("XOSMX", "8").replace("XDEVETX", "9"))
    return result

def sifrovani():
    text = text_entry.get("1.0", "end-1c")
    klic = uprava_klice(klic_entry.get())
    custom_abeceda = custom_abeceda_entry.get().strip()
    matice = tabulka(klic, custom_abeceda=custom_abeceda)
    
    upraveny_text = uprava_textu(text)
    sifrujed_text = sifruj(upraveny_text, klic, matice)

    filtered_text = uprava_textu(text)
    ffiltrovany_text.delete("1.0", tk.END)
    ffiltrovany_text.insert(tk.END, filtered_text)
    
    result_entry.delete("1.0", "end")
    result_entry.insert("1.0", sifrujed_text)
    zobraz_tabulku(matice)

def desifrovani():
    result = result_entry.get("1.0", "end-1c")
    klic = uprava_klice(klic_entry.get())
    matice = global_matice
    
    desifrovany_text = desifruj(result, klic)
    
    result_entry.delete("1.0", "end")
    result_entry.insert("1.0", desifrovany_text)
    zobraz_tabulku(matice)

def zobraz_tabulku(matice):
    matice_display = ""
    adfgvx = "ADFGVX"
    for row in adfgvx:
        for col in adfgvx:
            letter = [k for k, v in matice.items() if v == row + col]
            if letter:
                matice_display += letter[0] + " "
            else:
                matice_display += "  "
        matice_display += "\n"
    matice_label.config(text=matice_display.strip())


def zmena_abecedy(event):
    if abeceda_combobox.get() == "Náhodná":
        custom_abeceda_entry.delete(0, tk.END)  # Smazat text
        custom_abeceda_entry.config(state="disabled")  # Zakázat vstup
        
    else:
        custom_abeceda_entry.config(state="normal")  # Povolit vstup



root = tk.Tk()
root.title("ADFGVX šifra")
root.geometry("600x600")

header_label = tk.Label(root, text="ADFGVX Šifra", font=("Helvetica", 16, "bold"))
header_label.grid(row=0, column=0, columnspan=4, pady=10)

tk.Label(root, text="Klíč:").grid(row=1, column=0, sticky="e")
klic_entry = tk.Entry(root, width=30)
klic_entry.grid(row=1, column=1, sticky="w")


tk.Label(root, text="Typ abecedy:").grid(row=2, column=0, sticky="e")
abeceda_combobox = ttk.Combobox(root, values=["Náhodná", "Vlastní"], state="readonly")
abeceda_combobox.set("Náhodná")
abeceda_combobox.grid(row=2, column=1, sticky="w")
abeceda_combobox.bind("<<ComboboxSelected>>", zmena_abecedy) # Přidání události pro změnu abecedy

tk.Label(root, text="Vlastní abeceda:").grid(row=2, column=2, sticky="e")
custom_abeceda_entry = tk.Entry(root, width=30)
custom_abeceda_entry.config(state="disabled")
custom_abeceda_entry.grid(row=2, column=3, sticky="w")

tk.Label(root, text="Text:").grid(row=3, column=0, columnspan=4)
text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=4, column=0, columnspan=4, pady=10)

sifruj_button = tk.Button(root, text="Šifrovat", command=sifrovani)
sifruj_button.grid(row=7, column=1, pady=10)
desifruj_button = tk.Button(root, text="Dešifrovat", command=desifrovani)
desifruj_button.grid(row=7, column=2, pady=10)

tk.Label(root, text="Filtrovaný text:").grid(row=9, column=0, columnspan=4)
ffiltrovany_text = tk.Text(root, height=5, width=50)  # Adjusted to match the size of other text fields
ffiltrovany_text.grid(row=10, column=0, columnspan=4)

result_text = tk.StringVar()
tk.Label(root, text="Výsledek:").grid(row=11, column=0, columnspan=4)
result_entry = tk.Text(root, height=5, width=50)
result_entry.grid(row=12, column=0, columnspan=4)

tk.Label(root, text="Polybiův čtverec:").grid(row=13, column=0, columnspan=4)
matice_label = tk.Label(root, text="", justify="left", font=("Courier", 10))
matice_label.grid(row=14, column=0, columnspan=4)



root.mainloop()
