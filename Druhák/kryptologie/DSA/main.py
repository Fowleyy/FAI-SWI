import os
import base64
import hashlib
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import math
import platform

output_directory = None


def generate_prime(bits):
    def is_prime(n, k=5):
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        def check_composite(a, d, n, s):
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
            if check_composite(a, d, n, s):
                return False
        return True

    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << bits - 1) | 1
        if is_prime(candidate):
            return candidate

def generate_keypair(p, q):
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

def encrypt(message, public_key):
    e, n = public_key
    message_bytes = message.encode('utf-8')
    message_int = bytes_to_int(message_bytes)
    encrypted_int = pow(message_int, e, n)
    return encrypted_int

def decrypt(cipher, private_key):
    d, n = private_key
    decrypted_int = pow(cipher, d, n)
    decrypted_bytes = int_to_bytes(decrypted_int)
    return decrypted_bytes.decode('utf-8')

def select_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory(title="Vyberte Výstupní Složku")
    if output_directory:
        output_directory_label.config(text=output_directory)
        messagebox.showinfo("Úspěch", f"Výstupní složka byla nastavena na: {output_directory}")
        open_folder(output_directory)  # Otevře složku po výběru
    else:
        messagebox.showwarning("Varování", "Nebyla vybrána žádná složka!")

def open_folder(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {path}")
    else:  # Linux
        os.system(f"xdg-open {path}")

def generate_keypair_ui():
    if not output_directory:
        messagebox.showerror("Chyba", "Výstupní složka není nastavena. Vyberte složku.")
        return


    p = generate_prime(1024)
    q = generate_prime(1024)
    public_key, private_key = generate_keypair(p, q)

    priv_path = os.path.join(output_directory, "private_key.priv")
    pub_path = os.path.join(output_directory, "public_key.pub")

    with open(priv_path, 'w') as f:
        priv_base64 = base64.b64encode(str(private_key).encode()).decode()
        f.write(f"RSA {priv_base64}")

    with open(pub_path, 'w') as f:
        pub_base64 = base64.b64encode(str(public_key).encode()).decode()
        f.write(f"RSA {pub_base64}")

    messagebox.showinfo("Úspěch", "Klíčový pár byl vygenerován a uložen.")

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        filename_label.config(text=os.path.basename(selected_file))
        filesize_label.config(text=f"{os.path.getsize(selected_file)} bytes")
        filepath_label.config(text=selected_file)
    else:
        filename_label.config(text="---")
        filesize_label.config(text="---")
        filepath_label.config(text="---")

def sign_file_ui():
    if not selected_file:
        messagebox.showwarning("Varování", "Nejprve vyberte soubor.")
        return

    priv_path = filedialog.askopenfilename(title="Vyberte privátní klíč", filetypes=[("Private Key", "*.priv")])
    if not priv_path:
        return

    with open(priv_path, 'r') as f:
        priv_key_data = f.read().split()[1]
        private_key = eval(base64.b64decode(priv_key_data).decode())

    with open(selected_file, 'rb') as f:
        file_hash = hashlib.sha3_512(f.read()).digest()

    signature = encrypt(file_hash.hex(), private_key)
    signature_base64 = base64.b64encode(int_to_bytes(signature)).decode()

    if not output_directory:
        messagebox.showwarning("Varování", "Vyberte výstupní složku.")
        return

    output_path = os.path.join(output_directory, os.path.basename(selected_file) + '.zip')
    with zipfile.ZipFile(output_path, 'w') as zf:
        zf.write(selected_file, arcname=os.path.basename(selected_file))

        with zf.open('podpis.sign', 'w') as sign_file:
            sign_content = f"RSA_SHA3-512 {signature_base64}"
            sign_file.write(sign_content.encode())

    file_info = os.stat(selected_file)
    info_text = f"""Podepsaný soubor:
Název: {os.path.basename(selected_file)}
Cesta: {selected_file}
Typ: {os.path.splitext(selected_file)[1]}
Velikost: {file_info.st_size} bytes"""
    messagebox.showinfo("Informace o souboru", info_text)

def verify_signature_ui():
    zip_path = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    if not zip_path:
        return

    pub_path = filedialog.askopenfilename(title="Vyberte veřejný klíč", filetypes=[("Public Key", "*.pub")])
    if not pub_path:
        return

    with open(pub_path, 'r') as f:
        pub_key_data = f.read().split()[1]
        public_key = eval(base64.b64decode(pub_key_data).decode())

    with zipfile.ZipFile(zip_path, 'r') as zf:
        signed_file_name = [name for name in zf.namelist() if not name.endswith('.sign')][0]
        signature_file_name = [name for name in zf.namelist() if name.endswith('.sign')][0]

        with zf.open(signed_file_name, 'r') as signed_file:
            file_content = signed_file.read()

        with zf.open(signature_file_name, 'r') as sign_file:
            signature_line = sign_file.read().decode()
            signature_base64 = signature_line.split()[1]

    file_hash = hashlib.sha3_512(file_content).digest().hex()
    signature_int = bytes_to_int(base64.b64decode(signature_base64))
    decrypted_hash = decrypt(signature_int, public_key)

    if decrypted_hash == file_hash:
        messagebox.showinfo("Ověření Podpisu", "Podpis je PLATNÝ!")
    else:
        messagebox.showerror("Ověření Podpisu", "Podpis je NEPLATNÝ!")

# GUI setup
root = tk.Tk()
root.title("DSA Šifra")
root.geometry("600x450")

# Label for DSA Šifra (bold title)
tk.Label(root, text="DSA Šifra", font=("Helvetica", 32, "bold")).pack(pady=10)

# Frame for Output Directory and path
output_frame = tk.Frame(root)
output_frame.pack(pady=9)

tk.Button(output_frame, text="Vybrat Výstupní Složku", command=select_output_directory).pack(side=tk.TOP, padx=4)
output_directory_label = tk.Label(output_frame, text="Není vybrána žádná složka")
output_directory_label.pack(side=tk.TOP, padx=5)

# Buttons and file info frames
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Generovat Klíčový Pár", command=generate_keypair_ui).pack(side=tk.LEFT, padx=5)

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

tk.Button(root, text="Vybrat Soubor", command=select_file).pack(pady=10)
tk.Button(root, text="Podepsat Soubor", command=sign_file_ui).pack(pady=10)
tk.Button(root, text="Kontrola Podpisu", command=verify_signature_ui).pack(pady=10)

root.mainloop()
