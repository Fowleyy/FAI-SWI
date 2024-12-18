import tkinter as tk
from tkinter import scrolledtext
import random
import math


# Funkce pro zjištění prvočíselnosti
def checkPrvo(n, k=40):
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Funkce pro generování prvočísel
def vytvorPrvo(min, max):
    while True:
        cislo = random.randint(min, max)
        if checkPrvo(cislo):
            return cislo
        

# Funkce pro generování klíčů
def vytvorKlic():
    global e, d, n

    min, max = 10**6, 10**7 - 1
    p, q = vytvorPrvo(min, max), vytvorPrvo(min, max)
    while p == q:
        q = vytvorPrvo(min, max)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Generování veřejného exponentu e
    while True:
        e = random.randint(2, phi_n)
        if math.gcd(e, phi_n) == 1:
            break

    d = pow(e, -1, phi_n)

    public_key = f"{str(e)[-13:]}"
    private_key = f"{str(d)[-13:]}"

    public_key_text.delete("1.0", tk.END)
    public_key_text.insert(tk.END, public_key)

    private_key_text.delete("1.0", tk.END)
    private_key_text.insert(tk.END, private_key)


# Funkce pro šifrování
def sifruj(text):
    global e, n

    result = [pow(ord(c), e, n) for c in text]
    max_block_size = len(str(n))
    result_strings = [f"{c:0{max_block_size}d}" for c in result]
    full_result = ''.join(result_strings)
    
    # Zobrazení šifrované zprávy
    sifruj_text.delete("1.0", tk.END)
    sifruj_text.insert(tk.END, ' '.join(full_result[i:i+6] for i in range(0, len(full_result), 6)))


# Funkce pro dešifrování
# Funkce pro dešifrování
def desifruj(text):
    global d, n

    full_text = ''.join(text.split())
    max_block_size = len(str(n))
    text_numbers = [int(full_text[i:i+max_block_size]) for i in range(0, len(full_text), max_block_size)]
    
    result = ''.join(chr(pow(c, d, n)) for c in text_numbers)
    
    # Zobrazení dešifrováné zprávy
    desifruj_text_output.delete("1.0", tk.END)  # Zde použijeme správnou proměnnou
    desifruj_text_output.insert(tk.END, result)  # a ne desifruj_text



# Vytvoření hlavního okna GUI
root = tk.Tk()
root.title("RSA Šifrovací Nástroj")
root.geometry("600x600")

title_label = tk.Label(root, text="RSA Šifra", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Menu tlačítka a textového pole vedle sebe
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

vytvorKlic_button = tk.Button(menu_frame, text="Generovat Klíč", command=vytvorKlic)
vytvorKlic_button.grid(row=0, column=0, padx=5)

# Rámec pro klíče vedle tlačítka
key_frame = tk.Frame(root)
key_frame.pack(pady=10)

public_key_label = tk.Label(key_frame, text="Veřejný Klíč:")
public_key_label.grid(row=0, column=0, padx=5)

public_key_text = scrolledtext.ScrolledText(key_frame, height=3, width=20)
public_key_text.grid(row=0, column=1, padx=5)

private_key_label = tk.Label(key_frame, text="Soukromý Klíč:")
private_key_label.grid(row=0, column=2, padx=5)

private_key_text = scrolledtext.ScrolledText(key_frame, height=3, width=20)
private_key_text.grid(row=0, column=3, padx=5)

# Pole pro šifrování
message_label = tk.Label(root, text="Zpráva k zašifrování:")
message_label.pack(pady=5)

message_input = tk.Entry(root, width=40)
message_input.pack(pady=5)

# Rámec pro tlačítka "Zašifrovat" a "Dešifrovat"
sifruj_frame = tk.Frame(root)
sifruj_frame.pack(pady=10)

sifruj_button = tk.Button(sifruj_frame, text="Zašifrovat", command=lambda: sifruj(message_input.get()))
sifruj_button.grid(row=0, column=0, padx=5)

desifruj_button = tk.Button(sifruj_frame, text="Dešifrovat", command=lambda: desifruj(sifruj_text.get("1.0", tk.END)))
desifruj_button.grid(row=0, column=1, padx=5)

sifruj_label = tk.Label(root, text="Šifrovaná Zpráva:")
sifruj_label.pack(pady=5)

sifruj_text = scrolledtext.ScrolledText(root, height=5, width=60)
sifruj_text.pack(pady=5)

# Pole pro dešifrování
desifruj_label = tk.Label(root, text="Dešifrováná Zpráva:")
desifruj_label.pack(pady=10)

desifruj_text_output = scrolledtext.ScrolledText(root, height=5, width=60)
desifruj_text_output.pack(pady=5)

# Spuštění aplikace
root.mainloop()
