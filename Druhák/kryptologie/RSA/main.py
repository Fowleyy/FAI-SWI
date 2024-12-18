import tkinter as tk
from tkinter import scrolledtext
import random
import math


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


def vytvorPrvo(min, max):
    while True:
        cislo = random.randint(min, max)
        if checkPrvo(cislo):
            return cislo


def vytvorKlic():
    global e, d, n

    min_cislice, max_cislice = 10**6, 10**7 - 1

    while True:
        p, q = vytvorPrvo(min_cislice, max_cislice), vytvorPrvo(min_cislice, max_cislice)
        if p != q:
            n = p * q
            if 10**12 <= n < 10**13:
                break

    fi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, fi)
        if math.gcd(e, fi) == 1:
            break

    d = pow(e, -1, fi)

    e_str = f"{e:013d}"
    d_str = f"{d:013d}"

    public_key_text.delete("1.0", tk.END)
    public_key_text.insert(tk.END, f"e: {e_str}\nn: {n}")

    private_key_text.delete("1.0", tk.END)
    private_key_text.insert(tk.END, f"d: {d_str}\nn: {n}")


def sifruj(text):
    global e, n

    block_size = 6  # Velikost bloku (počet znaků v každém bloku)
    bloky = [text[i:i + block_size] for i in range(0, len(text), block_size)]

    sifrovane_bloky = []
    for block in bloky:
        # Převeďte každý znak na 3-místný kód (ASCII), aby každé písmeno mělo 3 číslice
        block_num = ''.join(f"{ord(c):03}" for c in block)  # Převeďte na číslo jako řetězec
        # Zasifrujte blok pomocí RSA
        zasifrovany_block = pow(int(block_num), e, n)
        sifrovane_bloky.append(str(zasifrovany_block))

    # Spojte všechny šifrované bloky
    result = ' '.join(sifrovane_bloky)

    sifruj_text.delete("1.0", tk.END)
    sifruj_text.insert(tk.END, result)


def desifruj(text):
    global d, n

    sifrovane_bloky = text.split()
    block_size = 6  # Velikost bloku (počet znaků v každém bloku)

    desifrovane_bloky = []
    for block in sifrovane_bloky:
        # Dešifrujeme blok číslem
        decrypted_block_num = pow(int(block), d, n)

        # Převeďte číslo zpět na text
        decrypted_block_str = str(decrypted_block_num)

        # Ujistíme se, že číslo je dostatečně dlouhé pro všechny bloky
        decrypted_block_str = decrypted_block_str.zfill(block_size * 3)

        # Rozdělte číslo na části po třech číslicích (každé představuje jeden znak)
        desifrovany_block = ''.join(chr(int(decrypted_block_str[i:i + 3])) for i in range(0, len(decrypted_block_str), 3))

        desifrovane_bloky.append(desifrovany_block)

    # Spojte všechny dešifrované bloky do výsledné zprávy
    result = ''.join(desifrovane_bloky)

    desifruj_text_output.delete("1.0", tk.END)
    desifruj_text_output.insert(tk.END, result)



root = tk.Tk()
root.title("RSA Šifrovací Nástroj")
root.geometry("600x600")

title_label = tk.Label(root, text="RSA Šifra", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

vytvorKlic_button = tk.Button(menu_frame, text="Generovat Klíč", command=vytvorKlic)
vytvorKlic_button.grid(row=0, column=0, padx=5)

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

desifruj_label = tk.Label(root, text="Dešifrováná Zpráva:")
desifruj_label.pack(pady=10)

desifruj_text_output = scrolledtext.ScrolledText(root, height=5, width=60)
desifruj_text_output.pack(pady=5)

root.mainloop()
