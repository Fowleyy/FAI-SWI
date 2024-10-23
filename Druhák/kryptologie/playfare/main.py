import tkinter as tk
from tkinter import scrolledtext, ttk


def uprava_klice(input, jazyk):
    znaky = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "ě": "e", "ů": "u", "č": "c", "ř": "r", "š": "s",
        "ť": "t", "ň": "n", "ď": "d", "ž": "z", "ý": "y"
    }
    result = ""
    for c in input.lower():
        if c in znaky:
            result += znaky[c]
        elif 'a' <= c <= 'z':
            result += c
    result = result.replace(" ", "").upper()
    
    if jazyk == "Čeština":
        result = result.replace("W", "V")
    elif jazyk == "Angličtina":
        result = result.replace("J", "I")

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


def tabulka(klic, jazyk):
    abeceda_cz = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    abeceda_en = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    klic = uprava_klice(klic, jazyk).upper()
    
    abeceda = abeceda_cz if jazyk == "Čeština" else abeceda_en

    klic = ''.join(sorted(set(klic), key=klic.index))
    zbytek = ''.join([char for char in abeceda if char not in klic])
    
    tabulka_sifry = klic + zbytek
    return [list(tabulka_sifry[i:i + 5]) for i in range(0, len(tabulka_sifry), 5)]


def najdi_prvek(arr, input):
    input = input.upper()
    for i, row in enumerate(arr):
        for j, val in enumerate(row):
            if val == input:
                return i, j
    return None, None


def sifruj(tabulka, text):
    if len(text) % 2 == 1:
        text += 'X'

    dvojice = [text[i:i + 2] for i in range(0, len(text), 2)]
    result = ""

    for par in dvojice:
        r1, c1 = najdi_prvek(tabulka, par[0])
        r2, c2 = najdi_prvek(tabulka, par[1])

        if r1 is None or r2 is None:
            return None

        if r1 == r2:
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        elif c1 == c2:
            r1 = (r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else:
            c1, c2 = c2, c1

        result += tabulka[r1][c1] + tabulka[r2][c2]

    result = ' '.join([result[i:i + 5] for i in range(0, len(result), 5)])
    return result


def desifruj(tabulka, text):
    text = text.replace(" ", "")
    splittext = ["".join(text[i:i+2]) for i in range(0, len(text), 2)]
    result = ""

    for doubleChar in splittext:
        pos1 = najdi_prvek(tabulka, doubleChar[0])
        pos2 = najdi_prvek(tabulka, doubleChar[1])

        if pos1 is None or pos2 is None:
            return None

        r1, c1 = pos1
        r2, c2 = pos2

        if r1 == r2:
            c1 = (c1 - 1) % 5
            c2 = (c2 - 1) % 5
        elif c1 == c2:
            r1 = (r1 - 1) % 5
            r2 = (r2 - 1) % 5
        else:
            c1, c2 = c2, c1

        result += tabulka[r1][c1] + tabulka[r2][c2]

    result = result.replace("XMEZERAX", " ")
    result = result.replace("XJEDNAX", "1").replace("XDVAX", "2").replace("XTRIX", "3")
    result = result.replace("XNULAX", "0").replace("XCTYRIX", "4").replace("XPETX", "5")
    result = result.replace("XSESTX", "6").replace("XSEDMX", "7").replace("XOSMX", "8").replace("XDEVETX", "9")
    result = result.rstrip('X')

    return result



def sifrovani():
    klic = klic_entry.get()
    vstup_text = vstup_textbox.get("1.0", tk.END).strip()
    jazyk = jazyk_combobox.get()
    
    upraveny_text = uprava_textu(vstup_text)
    tabulka_sifry = tabulka(klic, jazyk)
    
    zasifrovany_text = sifruj(tabulka_sifry, upraveny_text)
    if zasifrovany_text is not None:
        vystup_textbox.delete("1.0", tk.END)
        vystup_textbox.insert(tk.END, zasifrovany_text)

        tabulka_textbox.delete("1.0", tk.END)
        for row in tabulka_sifry:
            tabulka_textbox.insert(tk.END, ' '.join(row) + '\n')

    else:
        vystup_textbox.delete("1.0", tk.END)
        vystup_textbox.insert(tk.END, "Chyba při šifrování.")



def desifrovani():
    klic = klic_entry.get()
    vstup_text = vystup_textbox.get("1.0", tk.END).strip()
    jazyk = jazyk_combobox.get()
    
    tabulka_sifry = tabulka(klic, jazyk)
    
    desifrovany_text = desifruj(tabulka_sifry, vstup_text)
    if desifrovany_text is not None:
        vystup_textbox.delete("1.0", tk.END)
        vystup_textbox.insert(tk.END, desifrovany_text)

    else:
        vystup_textbox.delete("1.0", tk.END)
        vystup_textbox.insert(tk.END, "Chyba při dešifrování.")


root = tk.Tk()
root.title("PlayFair Šifra")
root.geometry("600x500")

nadpis = tk.Label(root, text="PlayFair šifra", font=("Helvetica", 18, "bold"))
nadpis.pack(pady=10)

pole_key = tk.Frame(root)
pole_key.pack(pady=5)

klic_label = tk.Label(pole_key, text="Zadejte klic:")
klic_label.pack(side=tk.LEFT)

klic_entry = tk.Entry(pole_key)
klic_entry.pack(side=tk.LEFT)

jazyk_label = tk.Label(pole_key, text="Jazyk:")
jazyk_label.pack(side=tk.LEFT, padx=(10, 0))

jazyk_combobox = ttk.Combobox(pole_key, values=["Čeština", "Angličtina"], state='readonly')  # Nastavení na readonly
jazyk_combobox.pack(side=tk.LEFT)
jazyk_combobox.current(0)  # Výchozí hodnota

pole_input = tk.Frame(root)
pole_input.pack(pady=5)

vstup_label = tk.Label(pole_input, text="Zadejte text:")
vstup_label.pack()

vstup_textbox = scrolledtext.ScrolledText(pole_input, wrap=tk.WORD, width=70, height=5)
vstup_textbox.pack()

tlacitka = tk.Frame(root)
tlacitka.pack(pady=5)

sifrovat_button = tk.Button(tlacitka, text="Šifrovat", command=sifrovani)
sifrovat_button.pack(side=tk.LEFT, padx=5)

desifrovat_button = tk.Button(tlacitka, text="Dešifrovat", command=desifrovani)
desifrovat_button.pack(side=tk.LEFT, padx=5)


pole_output = tk.Frame(root)
pole_output.pack(pady=5)

vystup_label = tk.Label(pole_output, text="Výstup:")
vystup_label.pack()

vystup_textbox = scrolledtext.ScrolledText(pole_output, wrap=tk.WORD, width=70, height=5)
vystup_textbox.pack()

pole_tabulka = tk.Frame(root)
pole_tabulka.pack(pady=5)

tabulka_label = tk.Label(pole_tabulka, text="Tabulka šifry:")
tabulka_label.pack()


tabulka_textbox = scrolledtext.ScrolledText(pole_tabulka, wrap=tk.WORD, width=10, height=5)
tabulka_textbox.pack()


root.mainloop()