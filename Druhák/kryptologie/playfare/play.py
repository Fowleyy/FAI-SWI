import tkinter as tk
from tkinter import messagebox

# Funkce pro vytvoření mřížky (tabulky) Playfair šifry
def create_playfair_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(key.upper().replace("W", "V")))  # Odeber duplicitní a zaměň W za V
    table = []
    used = set()

    for char in key:
        if char not in used and char in alphabet:
            table.append(char)
            used.add(char)

    for char in alphabet:
        if char not in used:
            table.append(char)
            used.add(char)

    return [table[i:i+5] for i in range(0, len(table), 5)]

# Funkce pro aktualizaci tabulky šifry v GUI
def update_table_gui(table):
    for widget in table_frame.winfo_children():
        widget.destroy()  # Vymazání staré tabulky

    for row in table:
        row_frame = tk.Frame(table_frame)
        row_frame.pack()
        for char in row:
            char_label = tk.Label(row_frame, text=char, width=4, borderwidth=2, relief="solid", font=('Arial', 14))
            char_label.pack(side=tk.LEFT)

# Funkce pro šifrování
def encrypt_playfair(plain_text, key):
    table = create_playfair_square(key)
    update_table_gui(table)  # Zobrazit tabulku v GUI
    plain_text = plain_text.upper().replace("W", "V").replace(" ", "")
    cipher_text = ""

    # Přidání "X" mezi dvojice stejných písmen
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'

        if a == b:
            b = 'X'

        # Najít pozice znaků v mřížce
        row_a, col_a = find_position(table, a)
        row_b, col_b = find_position(table, b)

        if row_a == row_b:  # Stejný řádek
            cipher_text += table[row_a][(col_a + 1) % 5]
            cipher_text += table[row_b][(col_b + 1) % 5]
        elif col_a == col_b:  # Stejný sloupec
            cipher_text += table[(row_a + 1) % 5][col_a]
            cipher_text += table[(row_b + 1) % 5][col_b]
        else:  # Obdélník
            cipher_text += table[row_a][col_b]
            cipher_text += table[row_b][col_a]

        i += 2

    return cipher_text

# Funkce pro dešifrování
def decrypt_playfair(cipher_text, key):
    table = create_playfair_square(key)
    update_table_gui(table)  # Zobrazit tabulku v GUI
    cipher_text = cipher_text.upper().replace("W", "V").replace(" ", "")
    plain_text = ""

    i = 0
    while i < len(cipher_text):
        a = cipher_text[i]
        b = cipher_text[i + 1] if i + 1 < len(cipher_text) else 'X'

        row_a, col_a = find_position(table, a)
        row_b, col_b = find_position(table, b)

        if row_a == row_b:  # Stejný řádek
            plain_text += table[row_a][(col_a - 1) % 5]
            plain_text += table[row_b][(col_b - 1) % 5]
        elif col_a == col_b:  # Stejný sloupec
            plain_text += table[(row_a - 1) % 5][col_a]
            plain_text += table[(row_b - 1) % 5][col_b]
        else:  # Obdélník
            plain_text += table[row_a][col_b]
            plain_text += table[row_b][col_a]

        i += 2

    return plain_text

# Najde pozici znaku v mřížce
def find_position(table, char):
    char = char.upper().replace('W', 'V')
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return row, col
    return None

# GUI Funkce
def encrypt_message():
    plain_text = plain_entry.get()
    key = key_entry.get()
    if not plain_text or not key:
        messagebox.showwarning("Chyba", "Zadejte text a klíč!")
        return
    encrypted = encrypt_playfair(plain_text, key)
    result_label.config(text=f"Zašifrovaný text: {encrypted}")

def decrypt_message():
    cipher_text = cipher_entry.get()
    key = key_entry.get()
    if not cipher_text or not key:
        messagebox.showwarning("Chyba", "Zadejte text a klíč!")
        return
    decrypted = decrypt_playfair(cipher_text, key)
    result_label.config(text=f"Dešifrovaný text: {decrypted}")

# Hlavní okno aplikace
root = tk.Tk()
root.title("Playfair šifra")

# Popis pro klíč
key_label = tk.Label(root, text="Klíč:")
key_label.pack()

# Vstupní pole pro klíč
key_entry = tk.Entry(root)
key_entry.pack()

# Popis pro text k zašifrování
plain_label = tk.Label(root, text="Text k zašifrování:")
plain_label.pack()

# Vstupní pole pro zašifrování
plain_entry = tk.Entry(root)
plain_entry.pack()

# Tlačítko pro zašifrování
encrypt_button = tk.Button(root, text="Zašifrovat", command=encrypt_message)
encrypt_button.pack()

# Popis pro zašifrovaný text
cipher_label = tk.Label(root, text="Text k dešifrování:")
cipher_label.pack()

# Vstupní pole pro dešifrování
cipher_entry = tk.Entry(root)
cipher_entry.pack()

# Tlačítko pro dešifrování
decrypt_button = tk.Button(root, text="Dešifrovat", command=decrypt_message)
decrypt_button.pack()

# Tabulka pro zobrazení Playfair šifry
table_frame = tk.Frame(root)
table_frame.pack()

# Popisek pro výsledek
result_label = tk.Label(root, text="")
result_label.pack()

# Spuštění aplikace
root.mainloop()
