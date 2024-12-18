import tkinter as tk
from tkinter import messagebox
import random
import math

# Kontrola prvočísel - Miller-Rabinův test
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

# Generování náhodného prvočísla v daném rozsahu
def vytvorPrvo(min, max):
    while True:
        cislo = random.randint(min, max)
        if checkPrvo(cislo):
            return cislo

# Generování veřejného a soukromého klíče
def vytvorKlic():
    global e, d, n

    min_cislice, max_cislice = 10**6, 10**7 - 1

    while True:
        p, q = vytvorPrvo(min_cislice, max_cislice), vytvorPrvo(min_cislice, max_cislice)
        if p != q:
            n = p * q
            if 10**12 <= n < 10**13:  # n má 13 číslic
                break

    fi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, fi)
        if math.gcd(e, fi) == 1:
            break

    d = pow(e, -1, fi)  # Invertuje e mod fi

    # Uložení klíčů do textových polí
    e_str = f"{e:013d}"
    d_str = f"{d:013d}"

    public_key_text.delete("1.0", tk.END)
    public_key_text.insert(tk.END, f"e: {e_str}\nn: {n}")

    private_key_text.delete("1.0", tk.END)
    private_key_text.insert(tk.END, f"d: {d_str}\nn: {n}")

# Rozdělení textu na bloky
def text_to_blocks(text, block_size=7):
    return [text[i:i + block_size] for i in range(0, len(text), block_size)]

# Spojení bloků zpět do textu
def blocks_to_text(blocks):
    return ''.join(blocks)


# Funkce pro šifrování zprávy (bloky po 3 znacích)
def encrypt():
    try:
        n = int(public_key_text.get("1.0", tk.END).split("\n")[1].split(": ")[1])
        e = int(public_key_text.get("1.0", tk.END).split("\n")[0].split(": ")[1])
        text = message_entry.get()

        # Rozdělení textu na malé bloky (3 znaky)
        block_size = 3
        blocks = text_to_blocks(text, block_size)

        ciphertext = []
        for block in blocks:
            block_value = int(''.join(f"{ord(char):03d}" for char in block))  # ASCII -> číslo
            encrypted_block = pow(block_value, e, n)
            ciphertext.append(encrypted_block)

        encrypted_text.delete("1.0", tk.END)
        encrypted_text.insert(tk.END, " ".join(map(str, ciphertext)))
    except Exception as ex:
        messagebox.showerror("Chyba", f"Šifrování selhalo: {ex}")


def decrypt():
    try:
        n = int(private_key_text.get("1.0", tk.END).split("\n")[1].split(": ")[1])
        d = int(private_key_text.get("1.0", tk.END).split("\n")[0].split(": ")[1])
        ciphertext = list(map(int, encrypted_text.get("1.0", tk.END).split()))

        decrypted_blocks = []
        for block in ciphertext:
            decrypted_value = pow(block, d, n)
            block_str = str(decrypted_value).zfill(18)  # 6 characters, each 3 digits

            # Convert each 3-digit segment back to a character
            chars = [chr(int(block_str[i:i + 3])) for i in range(0, len(block_str), 3)]
            
            # Join characters to form the decrypted block
            decrypted_blocks.append(''.join(chars))

        plaintext = ''.join(decrypted_blocks)
        
        # Remove any potential null characters that might have been added as padding
        plaintext = plaintext.replace('\x00', '')

        decrypted_text.delete("1.0", tk.END)
        decrypted_text.insert(tk.END, plaintext)
    except Exception as ex:
        messagebox.showerror("Chyba", f"Dešifrování selhalo: {ex}")


# GUI
root = tk.Tk()
root.title("RSA Šifrovací Nástroj")
root.geometry("600x700")

# Nadpis
tk.Label(root, text="RSA Šifra", font=("Helvetica", 16, "bold")).pack(pady=10)

# Generování klíčů
tk.Button(root, text="Generovat Klíče", command=vytvorKlic).pack()

tk.Label(root, text="Veřejný Klíč:").pack()
public_key_text = tk.Text(root, height=3, width=60)
public_key_text.pack()

tk.Label(root, text="Soukromý Klíč:").pack()
private_key_text = tk.Text(root, height=3, width=60)
private_key_text.pack()

# Zpráva k šifrování
tk.Label(root, text="Zpráva k zašifrování:").pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

# Tlačítka šifrování a dešifrování
tk.Button(root, text="Zašifrovat", command=encrypt).pack(pady=5)
tk.Button(root, text="Dešifrovat", command=decrypt).pack()

# Výsledky
tk.Label(root, text="Šifrovaná Zpráva:").pack()
encrypted_text = tk.Text(root, height=5, width=60)
encrypted_text.pack()

tk.Label(root, text="Dešifrovaná Zpráva:").pack()
decrypted_text = tk.Text(root, height=5, width=60)
decrypted_text.pack()

root.mainloop()
