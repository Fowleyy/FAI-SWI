"""Vožení knihoven a funkcí pro testy."""
from io import StringIO
import unittest
from unittest.mock import patch
from kalkulacka import (
    je_kladne,
    obvod_obdelniku,
    obsah_obdelniku,
    obvod_ctverce,
    obsah_ctverce,
    obvod_kruhu,
    obsah_kruhu,
    obvod_lichobezniku,
    obsah_lichobezniku,
    obvod_trojuhelniku,
    obsah_trojuhelniku,
    main
)


class TestMathLibrary(unittest.TestCase):
    """Třídá, pro vzorce."""

    def test_je_kladne(self):
        """Testování funkce je_kladne."""
        self.assertTrue(je_kladne(1))
        self.assertFalse(je_kladne(-1))
        self.assertFalse(je_kladne(0))

    def test_obvod_obdelniku(self):
        """Testování funkce obvod_obdelniku."""
        self.assertEqual(obvod_obdelniku(3, 4), 14)
        self.assertEqual(obvod_obdelniku(5, 5), 20)
        with self.assertRaises(ValueError):
            obvod_obdelniku(-3, 4)  # záporná hodnota strany
            obvod_obdelniku(0, 4)  # nulová hodnota strany

    def test_obsah_obdelniku(self):
        """Testování funkce obsah_obdelniku."""
        self.assertEqual(obsah_obdelniku(3, 4), 12)
        self.assertEqual(obsah_obdelniku(5, 5), 25)
        with self.assertRaises(ValueError):
            obsah_obdelniku(-3, 4)  # záporná hodnota strany
            obsah_obdelniku(0, 4)  # nulová hodnota strany

    def test_obvod_ctverce(self):
        """Testování funkce obvod_ctverce."""
        self.assertEqual(obvod_ctverce(3), 12)
        self.assertEqual(obvod_ctverce(5), 20)
        with self.assertRaises(ValueError):
            obvod_ctverce(-3)  # záporná hodnota strany
            obvod_ctverce(0)  # nulová hodnota strany

    def test_obsah_ctverce(self):
        """Testování funkce obsah_ctverce."""
        self.assertEqual(obsah_ctverce(3), 9)
        self.assertEqual(obsah_ctverce(5), 25)
        with self.assertRaises(ValueError):
            obsah_ctverce(-3)  # záporná hodnota strany
            obsah_ctverce(0)  # nulová hodnota strany

    def test_obvod_kruhu(self):
        """Testování funkce obvod_kruhu."""
        self.assertAlmostEqual(obvod_kruhu(3), 18.84955592, places=6)
        self.assertAlmostEqual(obvod_kruhu(5), 31.41592654, places=6)
        with self.assertRaises(ValueError):
            obvod_kruhu(-3)  # záporný poloměr
            obvod_kruhu(0)  # nulový poloměr

    def test_obsah_kruhu(self):
        """Testování funkce obsah_kruhu."""
        self.assertAlmostEqual(obsah_kruhu(3), 28.27433388, places=6)
        self.assertAlmostEqual(obsah_kruhu(5), 78.53981634, places=6)
        with self.assertRaises(ValueError):
            obsah_kruhu(-3)  # záporný poloměr
            obsah_kruhu(0)  # nulový poloměr

    def test_obvod_trojuhelniku(self):
        """Testování funkce obvod_trojuhelnik."""
        # Testování správných vstupů
        self.assertEqual(obvod_trojuhelniku(3, 4, 5), 12)
        self.assertEqual(obvod_trojuhelniku(5, 5, 5), 15)

        # Testování neplatných vstupů
        with self.assertRaises(ValueError):
            obvod_trojuhelniku(1, 2, 6)  # neplatný trojúhelník

    def test_obsah_trojuhelniku(self):
        """Testování funkce obsah_trojuhelniku."""
        # Testování správných vstupů
        self.assertEqual(obsah_trojuhelniku(4, 6), 12)
        self.assertEqual(obsah_trojuhelniku(10, 5), 25)

        # Testování neplatných vstupů
        with self.assertRaises(ValueError):
            obsah_trojuhelniku(-4, 6)  # záporná hodnota strany
            obsah_trojuhelniku(0, 5)  # nulová hodnota strany

    def test_obvod_lichobezniku(self):
        """Testování funkce obvod_lichobezniku."""
        # Testování správných vstupů
        self.assertEqual(obvod_lichobezniku(4, 6, 4, 6), 20)
        self.assertEqual(obvod_lichobezniku(8, 8, 5, 5), 26)

        # Testování neplatných vstupů
        with self.assertRaises(ValueError):
            obvod_lichobezniku(-4, 6, 4, 6)  # záporná hodnota strany
            obvod_lichobezniku(0, 5, 4, 6)  # nulová hodnota strany

    def test_obsah_lichobezniku(self):
        """Testování funkce obsah_lichobezniku."""
        # Testování správných vstupů
        self.assertEqual(obsah_lichobezniku(4, 6, 8), 40)
        self.assertEqual(obsah_lichobezniku(8, 8, 5), 40)

        # Testování neplatných vstupů
        with self.assertRaises(ValueError):
            obsah_lichobezniku(-4, 6, 8)  # záporná hodnota strany
            obsah_lichobezniku(0, 5, 8)  # nulová hodnota strany


class TestMainFunction(unittest.TestCase):
    """Třída pro testování funkce main."""

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4', '3', '4', '5', '6'])
    def test_main(self, mock_input, mock_stdout):
        """Testování funkce main."""
        main()


if __name__ == '__main__':
    unittest.main()
