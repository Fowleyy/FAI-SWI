import os

def uprav_soubory(root_path):
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(".robot"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    obsah = file.read()

                if "Zaloguj a Zkontroluj" in obsah:
                    novy_obsah = obsah.replace("Zaloguj a Zkontroluj", "Kontroluj")
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(novy_obsah)
                    print(f"Upraveno: {file_path}")

if __name__ == "__main__":
    slozka = r"C:\Users\Daniel\Desktop\testování\Automaticke"  # Pozor na r"" kvůli zpětným lomítkům
    uprav_soubory(slozka)
