"""Knihovna pro matematicke operace."""
import math


def je_kladne(*hodnoty):
    """Funkce zjistuje, zda jsou vsechny zadane hodnoty kladne.

    Args:
        *hodnoty: Seznam hodnot k testovani.

    Returns:
        bool: True, pokud jsou vsechny hodnoty kladne, jinak False.
    """
    for hodnota in hodnoty:
        if hodnota <= 0:
            return False
    return True


def obvod_obdelniku(a, b):
    """Vypocita obvod obdelniku.

    Args:
        a (float): Delka strany a.
        b (float): Delka strany b.

    Returns:
        float: Obvod obdelniku.

    Raises:
        ValueError: Pokud jsou zaporne nebo nulove hodnoty stran.
    """
    if not je_kladne(a, b):
        raise ValueError("Neplatny vstup: Strany obdelniku musi byt kladne")
    return 2 * (a + b)


def obsah_obdelniku(a, b):
    """Vypocita obsah obdelniku.

    Args:
        a (float): Delka strany a.
        b (float): Delka strany b.

    Returns:
        float: Obsah obdelniku.

    Raises:
        ValueError: Pokud jsou zaporne nebo nulove hodnoty stran.
    """
    if not je_kladne(a, b):
        raise ValueError("Neplatny vstup: Strany obdelniku musi byt kladne")
    return a * b


def obvod_ctverce(a):
    """Vypocita obvod ctverce.

    Args:
        a (float): Delka strany.

    Returns:
        float: Obvod ctverce.

    Raises:
        ValueError: Pokud je zaporna nebo nulova delka strany.
    """
    if not je_kladne(a):
        raise ValueError("Neplatny vstup: Strana ctverce musi byt kladna")
    return 4 * a


def obsah_ctverce(a):
    """Vypocita obsah ctverce.

    Args:
        a (float): Delka strany.

    Returns:
        float: Obsah ctverce.

    Raises:
        ValueError: Pokud je zaporna nebo nulova delka strany.
    """
    if not je_kladne(a):
        raise ValueError("Neplatny vstup: Strana ctverce musi byt kladna")
    return a * a


def obvod_kruhu(r):
    """Vypocita obvod kruhu.

    Args:
        r (float): Polomer kruhu.

    Returns:
        float: Obvod kruhu.

    Raises:
        ValueError: Pokud je zaporny nebo nulovy polomer.
    """
    if not je_kladne(r):
        raise ValueError("Neplatny vstup: Polomer kruhu musi byt kladny")
    return 2 * math.pi * r


def obsah_kruhu(r):
    """Vypocita obsah kruhu.

    Args:
        r (float): Polomer kruhu.

    Returns:
        float: Obsah kruhu.

    Raises:
        ValueError: Pokud je zaporny nebo nulovy polomer.
    """
    if not je_kladne(r):
        raise ValueError("Neplatny vstup: Polomer kruhu musi byt kladny")
    return math.pi * r * r


def obvod_trojuhelniku(a, b, c):
    """Vypocita obvod trojuhelniku.

    Args:
        a (float): Delka strany a.
        b (float): Delka strany b.
        c (float): Delka strany c.

    Returns:
        float: Obvod trojuhelniku.

    Raises:
        ValueError: Zaporne hodnoty nebo neplatny trojuhelnik.
    """
    if not je_kladne(a, b, c):
        raise ValueError("Neplatny vstup: Strany trojuhelniku musi byt kladne")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Neplatny vstup: Neplatny trojuhelnik")
    return a + b + c


def obsah_trojuhelniku(a, v):
    """Vypocita obsah trojuhelniku.

    Args:
        a (float): Delka zakladny.
        v (float): Vyska na zakladnu.

    Returns:
        float: Obsah trojuhelniku.

    Raises:
        ValueError: Pokud jsou zaporne nebo nulove hodnoty.
    """
    if not je_kladne(a, v):
        raise ValueError("Neplatny vstup: Hodnoty musi byt kladne")
    return 0.5 * a * v


def obvod_lichobezniku(a, b, c, d):
    """Vypocita obvod lichobezniku.

    Args:
        a (float): Delka strany a.
        b (float): Delka strany b.
        c (float): Delka strany c.
        d (float): Delka strany d.

    Returns:
        float: Obvod lichobezniku.

    Raises:
        ValueError: Pokud jsou zaporne nebo nulove hodnoty stran.
    """
    if not je_kladne(a, b, c, d):
        raise ValueError("Neplatny vstup: Strany lichobezniku musi byt kladne")
    return a + b + c + d


def obsah_lichobezniku(a, b, v):
    """Vypocita obsah lichobezniku.

    Args:
        a (float): Delka zakladny a.
        b (float): Delka zakladny b.
        v (float): Vyska na zakladnu.

    Returns:
        float: Obsah lichobezniku.

    Raises:
        ValueError: Pokud jsou zaporne nebo nulove hodnoty.
    """
    if not je_kladne(a, b, v):
        raise ValueError("Neplatny vstup: Hodnoty musi byt kladne")
    return 0.5 * (a + b) * v

# Funkce uzivatelskeho rozhrani


def obdelnik_ui():
    """Uzivatelske rozhrani pro vypocet obvodu a obsahu obdelniku."""
    try:
        a = float(input("Zadejte delku strany a: "))
        b = float(input("Zadejte delku strany b: "))
        print("Obvod obdelniku je:", obvod_obdelniku(a, b))
        print("Obsah obdelniku je:", obsah_obdelniku(a, b))
    except ValueError as e:
        print("Chyba:", e)


def ctverec_ui():
    """Uzivatelske rozhrani pro vypocet obvodu a obsahu ctverce."""
    try:
        a = float(input("Zadejte delku strany a: "))
        print("Obvod ctverce je:", obvod_ctverce(a))
        print("Obsah ctverce je:", obsah_ctverce(a))
    except ValueError as e:
        print("Chyba:", e)


def kruh_ui():
    """Uzivatelske rozhrani pro vypocet obvodu a obsahu kruhu."""
    try:
        r = float(input("Zadejte polomer kruhu: "))
        print("Obvod kruhu je:", obvod_kruhu(r))
        print("Obsah kruhu je:", obsah_kruhu(r))
    except ValueError as e:
        print("Chyba:", e)


def trojuhelnik_ui():
    """Uzivatelske rozhrani pro vypocet obvodu a obsahu trojuhelniku."""
    try:
        a = float(input("Zadejte delku strany a: "))
        b = float(input("Zadejte delku strany b: "))
        c = float(input("Zadejte delku strany c: "))
        print("Obvod trojuhelniku je:", obvod_trojuhelniku(a, b, c))
        v = float(input("Zadejte vysku na stranu a: "))
        print("Obsah trojuhelniku je:", obsah_trojuhelniku(a, v))
    except ValueError as e:
        print("Chyba:", e)


def lichobeznik_ui():
    """Uzivatelske rozhrani pro vypocet obvodu a obsahu lichobezniku."""
    try:
        a = float(input("Zadejte delku strany a: "))
        b = float(input("Zadejte delku strany b: "))
        c = float(input("Zadejte delku strany c: "))
        d = float(input("Zadejte delku strany d: "))
        v = float(input("Zadejte vysku na stranu a nebo b: "))
        print("Obvod lichobezniku je:", obvod_lichobezniku(a, b, c, d))
        print("Obsah lichobezniku je:", obsah_lichobezniku(a, b, v))
    except ValueError as e:
        print("Chyba:", e)


def main():
    """Hlavni funkce programu."""
    print("Program pro vypocet obvodu a obsahu geometrickych tvaru")
    while True:
        print("\nVyberte geometricky tvar:")
        print("1. Obdelnik")
        print("2. Ctverec")
        print("3. Kruh")
        print("4. Trojuhelnik")
        print("5. Lichobeznik")
        print("6. Konec programu")

        volba = input("Zadejte cislo odpovidajici geometrickemu tvaru: ")

        if volba == "1":  # Obdelnik
            obdelnik_ui()
        elif volba == "2":  # Ctverec
            ctverec_ui()
        elif volba == "3":  # Kruh
            kruh_ui()
        elif volba == "4":  # Trojuhelnik
            trojuhelnik_ui()
        elif volba == "5":  # Lichobeznik
            lichobeznik_ui()
        elif volba == "6":  # Konec programu
            print("Dekuji za pouziti programu. Ukoncuji...")
            break
        else:
            print("Neplatna volba! Zadejte prosim cislo od 1 do 6.")


if __name__ == "__main__":
    main()
