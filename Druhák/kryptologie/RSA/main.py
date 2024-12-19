import tkinter as tk
from tkinter import messagebox
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


def text_to_blocks(text, block_size=7):
    return [text[i:i + block_size] for i in range(0, len(text), block_size)]


def blocks_to_text(blocks):
    return ''.join(blocks)


def sifruj():
    try:
        n = int(public_key_text.get("1.0", tk.END).split("\n")[1].split(": ")[1])
        e = int(public_key_text.get("1.0", tk.END).split("\n")[0].split(": ")[1])
        text = message_entry.get()

        block_size = 3
        blocks = text_to_blocks(text, block_size)

        result = []
        for block in blocks:
            block_value = int(''.join(f"{ord(char):03d}" for char in block))
            sifrovany_block = pow(block_value, e, n)
            result.append(sifrovany_block)

        sifrovany_text.delete("1.0", tk.END)
        sifrovany_text.insert(tk.END, " ".join(map(str, result)))

    except Exception as ex:
        messagebox.showerror("Chyba", f"Šifrování selhalo: {ex}")


def desifruj():
    try:
        n = int(private_key_text.get("1.0", tk.END).split("\n")[1].split(": ")[1])
        d = int(private_key_text.get("1.0", tk.END).split("\n")[0].split(": ")[1])
        text = list(map(int, sifrovany_text.get("1.0", tk.END).split()))

        deisfrovany_blocks = []
        for block in text:
            deisfrovana_hodnota = pow(block, d, n)
            block_str = str(deisfrovana_hodnota).zfill(18)

            chars = [chr(int(block_str[i:i + 3])) for i in range(0, len(block_str), 3)]
            
            deisfrovany_blocks.append(''.join(chars))

        result = ''.join(deisfrovany_blocks)
        
        result = result.replace('\x00', '')

        deisfrovany_text.delete("1.0", tk.END)
        deisfrovany_text.insert(tk.END, result)

    except Exception as ex:
        messagebox.showerror("Chyba", f"Dešifrování selhalo: {ex}")


root = tk.Tk()
root.title("RSA Šifrovací Nástroj")
root.geometry("600x450")

tk.Label(root, text="RSA Šifra", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Button(root, text="Generovat Klíče", command=vytvorKlic).pack()

# Frame pro klíče
frame_keys = tk.Frame(root)
frame_keys.pack(pady=5)

# Veřejný klíč
tk.Label(frame_keys, text="Veřejný Klíč:").pack(side=tk.LEFT, padx=5)
public_key_text = tk.Text(frame_keys, height=2, width=20)
public_key_text.pack(side=tk.LEFT, padx=5)

# Soukromý klíč
tk.Label(frame_keys, text="Soukromý Klíč:").pack(side=tk.LEFT, padx=5)
private_key_text = tk.Text(frame_keys, height=2, width=20)
private_key_text.pack(side=tk.LEFT, padx=5)

frame_keys.pack(anchor="center")

# Zpráva k zašifrování
tk.Label(root, text="Zpráva k zašifrování:").pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

# Frame pro tlačítka "Zašifrovat" a "Dešifrovat"
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

# Tlačítka
tk.Button(frame_buttons, text="Zašifrovat", command=sifruj).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Dešifrovat", command=desifruj).pack(side=tk.LEFT, padx=10)

frame_buttons.pack(anchor="center")

# Šifrovaná zpráva
tk.Label(root, text="Šifrovaná Zpráva:").pack()
sifrovany_text = tk.Text(root, height=5, width=60)
sifrovany_text.pack()

# Dešifrovaná zpráva
tk.Label(root, text="Dešifrovaná Zpráva:").pack()
deisfrovany_text = tk.Text(root, height=5, width=60)
deisfrovany_text.pack()

root.mainloop()

