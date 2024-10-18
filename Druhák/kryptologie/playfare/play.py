import tkinter as tk
from tkinter import messagebox

# Vytvoření matice 5x5 bez písmena W, ale s písmenem J
def create_matrix(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVXYZ"  # Vynecháme W, J zůstane
    matrix = []
    used_chars = set()

    for char in key.upper():
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

# Rozdělení textu na digramy
def prepare_text(text):
    text = text.upper().replace(" ", "")  # Odstranění mezer a převod na velká písmena
    digrams = []
    i = 0

    while i < len(text):
        if i == len(text) - 1:
            digrams.append(text[i] + 'X')  # Pokud je lichý počet znaků, přidá X
            i += 1
        elif text[i] == text[i + 1]:
            digrams.append(text[i] + 'X')  # Pokud jsou dva stejné znaky, přidá X
            i += 1
        else:
            digrams.append(text[i] + text[i + 1])
            i += 2
    return digrams

# Získání pozice písmena v matici
def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    raise ValueError(f"Character {char} not found in matrix.")

# Šifrování digramu
def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Dešifrování digramu
def decrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Funkce pro šifrování textu
def encrypt(text, key):
    matrix = create_matrix(key)
    digrams = prepare_text(text)
    encrypted_text = ''
    for digram in digrams:
        encrypted_text += encrypt_pair(digram, matrix)
    return encrypted_text

# Funkce pro dešifrování textu
def decrypt(text, key):
    matrix = create_matrix(key)
    # Ověříme, že text má sudý počet znaků
    if len(text) % 2 != 0:
        raise ValueError("Encrypted text must have an even number of characters.")
    
    digrams = [text[i:i + 2].upper() for i in range(0, len(text), 2)]  # Převod na velká písmena
    decrypted_text = ''
    for digram in digrams:
        decrypted_text += decrypt_pair(digram, matrix)
    return decrypted_text

# GUI aplikace
def create_gui():
    def encrypt_message():
        text = entry_text.get()
        key = entry_key.get()
        if not text or not key:
            messagebox.showerror("Chyba", "Prosím, vyplňte text a klíč.")
            return
        encrypted = encrypt(text, key)
        result_label.config(text="Šifrovaný text: " + encrypted)

    def decrypt_message():
        text = entry_text.get()
        key = entry_key.get()
        if not text or not key:
            messagebox.showerror("Chyba", "Prosím, vyplňte text a klíč.")
            return
        try:
            decrypted = decrypt(text, key)
            result_label.config(text="Dešifrovaný text: " + decrypted)
        except ValueError as e:
            messagebox.showerror("Chyba", str(e))

    root = tk.Tk()
    root.title("Playfair Šifra")

    # Vstup pro text
    tk.Label(root, text="Text:").grid(row=0, column=0)
    entry_text = tk.Entry(root)
    entry_text.grid(row=0, column=1)

    # Vstup pro klíč
    tk.Label(root, text="Klíč:").grid(row=1, column=0)
    entry_key = tk.Entry(root)
    entry_key.grid(row=1, column=1)

    # Tlačítka pro šifrování a dešifrování
    encrypt_button = tk.Button(root, text="Šifrovat", command=encrypt_message)
    encrypt_button.grid(row=2, column=0)

    decrypt_button = tk.Button(root, text="Dešifrovat", command=decrypt_message)
    decrypt_button.grid(row=2, column=1)

    # Výsledný text
    result_label = tk.Label(root, text="Výsledek: ")
    result_label.grid(row=3, column=0, columnspan=2)

    root.mainloop()

# Spuštění GUI
create_gui()
