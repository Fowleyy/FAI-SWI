import os
import base64
import hashlib
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import math
import platform

output_slozka = None


def vytvorPrvo(bits):
    def checkPrvo(n, k=5):
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        def jeSlozene(a, d, n, s):
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                return False
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    return False
            return True

        s = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            s += 1

        for _ in range(5):
            a = random.randint(2, n - 2)
            if jeSlozene(a, d, n, s):
                return False
        return True

    while True:
        cislo = random.getrandbits(bits)
        cislo |= (1 << bits - 1) | 1
        if checkPrvo(cislo):
            return cislo


def vytvorKlice(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(1, phi)

    d = pow(e, -1, phi)

    return ((e, n), (d, n))


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def bytes_to_int(xbytes):
    return int.from_bytes(xbytes, 'big')


def sifruj(text, public_key):
    e, n = public_key
    text_bytes = text.encode('utf-8')
    text_int = bytes_to_int(text_bytes)
    result = pow(text_int, e, n)
    return result


def desifruj(text, private_key):
    d, n = private_key
    desifrovany_int = pow(text, d, n)
    result = int_to_bytes(desifrovany_int)
    return result.decode('utf-8')


def vyberSlozku():
    global output_slozka
    output_slozka = filedialog.askdirectory(title="Vyberte Výstupní Složku")
    if output_slozka:
        output_slozka_label.config(text=output_slozka)
        messagebox.showinfo("Úspěch", f"Výstupní složka byla nastavena na: {output_slozka}")
        otevriSlozku(output_slozka)
    else:
        messagebox.showwarning("Varování", "Nebyla vybrána žádná složka!")


def otevriSlozku(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        os.system(f"open {path}")
    else:
        os.system(f"xdg-open {path}")


def vytvorKlice_ui():
    if not output_slozka:
        messagebox.showerror("Chyba", "Výstupní složka není nastavena. Vyberte složku.")
        return


    p = vytvorPrvo(1024)
    q = vytvorPrvo(1024)

    public_key, private_key = vytvorKlice(p, q)

    priv_path = os.path.join(output_slozka, "private_key.priv")
    pub_path = os.path.join(output_slozka, "public_key.pub")

    with open(priv_path, 'w') as f:
        priv_base64 = base64.b64encode(str(private_key).encode()).decode()
        f.write(f"RSA {priv_base64}")

    with open(pub_path, 'w') as f:
        pub_base64 = base64.b64encode(str(public_key).encode()).decode()
        f.write(f"RSA {pub_base64}")

    messagebox.showinfo("Úspěch", "Klíčový pár byl vygenerován a uložen.")

def vyberSoubor():
    global vybranySoubor

    vybranySoubor = filedialog.askopenfilename()
    
    if vybranySoubor:
        filename_label.config(text=os.path.basename(vybranySoubor))
        filesize_label.config(text=f"{os.path.getsize(vybranySoubor)} bytes")
        filepath_label.config(text=vybranySoubor)

    else:
        filename_label.config(text="---")
        filesize_label.config(text="---")
        filepath_label.config(text="---")

def podpis():
    if not vybranySoubor:
        messagebox.showwarning("Varování", "Nejprve vyberte soubor.")
        return

    priv_path = filedialog.askopenfilename(title="Vyberte privátní klíč", filetypes=[("Private Key", "*.priv")])
    if not priv_path:
        return

    with open(priv_path, 'r') as f:
        priv_key_data = f.read().split()[1]
        private_key = eval(base64.b64decode(priv_key_data).decode())

    with open(vybranySoubor, 'rb') as f:
        file_hash = hashlib.sha3_512(f.read()).digest()

    podpis = sifruj(file_hash.hex(), private_key)
    podpis_base64 = base64.b64encode(int_to_bytes(podpis)).decode()

    if not output_slozka:
        messagebox.showwarning("Varování", "Vyberte výstupní složku.")
        return

    output_path = os.path.join(output_slozka, os.path.basename(vybranySoubor) + '.zip')
    with zipfile.ZipFile(output_path, 'w') as zf:
        zf.write(vybranySoubor, arcname=os.path.basename(vybranySoubor))

        with zf.open('podpis.sign', 'w') as sign_file:
            sign_content = f"RSA_SHA3-512 {podpis_base64}"
            sign_file.write(sign_content.encode())

    soubor_info = os.stat(vybranySoubor)
    info_text = f"""Podepsaný soubor:
Název: {os.path.basename(vybranySoubor)}
Cesta: {vybranySoubor}
Typ: {os.path.splitext(vybranySoubor)[1]}
Velikost: {soubor_info.st_size} bytes"""
    messagebox.showinfo("Informace o souboru", info_text)


def overeni():
    zip_path = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    if not zip_path:
        return

    klic_path = filedialog.askopenfilename(title="Vyberte veřejný klíč", filetypes=[("Public Key", "*.pub")])
    if not klic_path:
        return

    with open(klic_path, 'r') as f:
        klic_key_data = f.read().split()[1]
        public_key = eval(base64.b64decode(klic_key_data).decode())

    with zipfile.ZipFile(zip_path, 'r') as zf:
        podepsany_soubor = [name for name in zf.namelist() if not name.endswith('.sign')][0]
        podpis = [name for name in zf.namelist() if name.endswith('.sign')][0]

        with zf.open(podepsany_soubor, 'r') as signed_file:
            file_content = signed_file.read()

        with zf.open(podpis, 'r') as sign_file:
            podpis = sign_file.read().decode()
            podpis_base64 = podpis.split()[1]

    file_hash = hashlib.sha3_512(file_content).digest().hex()
    podpis_int = bytes_to_int(base64.b64decode(podpis_base64))
    desifrovany_hash = desifruj(podpis_int, public_key)

    if desifrovany_hash == file_hash:
        messagebox.showinfo("Ověření Podpisu", "Podpis je PLATNÝ!")
    else:
        messagebox.showerror("Ověření Podpisu", "Podpis je NEPLATNÝ!")


root = tk.Tk()
root.title("DSA Šifra")
root.geometry("600x450")

tk.Label(root, text="DSA Šifra", font=("Helvetica", 32, "bold")).pack(pady=10)

output_frame = tk.Frame(root)
output_frame.pack(pady=9)

tk.Button(output_frame, text="Vybrat Výstupní Složku", command=vyberSlozku).pack(side=tk.TOP, padx=4)
output_slozka_label = tk.Label(output_frame, text="Není vybrána žádná složka")
output_slozka_label.pack(side=tk.TOP, padx=5)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Generovat Klíčový Pár", command=vytvorKlice_ui).pack(side=tk.LEFT, padx=5)

file_info_frame = tk.Frame(root)
file_info_frame.pack(pady=10)

tk.Label(file_info_frame, text="Název souboru:").grid(row=0, column=0, padx=5, sticky="e")
filename_label = tk.Label(file_info_frame, text="---")
filename_label.grid(row=0, column=1, padx=5)

tk.Label(file_info_frame, text="Velikost souboru:").grid(row=1, column=0, padx=5, sticky="e")
filesize_label = tk.Label(file_info_frame, text="---")
filesize_label.grid(row=1, column=1, padx=5)

tk.Label(file_info_frame, text="Cesta k souboru:").grid(row=2, column=0, padx=5, sticky="e")
filepath_label = tk.Label(file_info_frame, text="---")
filepath_label.grid(row=2, column=1, padx=5)

tk.Button(root, text="Vybrat Soubor", command=vyberSoubor).pack(pady=10)
tk.Button(root, text="Podepsat Soubor", command=podpis).pack(pady=10)
tk.Button(root, text="Kontrola Podpisu", command=overeni).pack(pady=10)


root.mainloop()
