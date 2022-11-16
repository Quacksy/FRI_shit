def stevilo_ovir(s):
    return len(s)


def dolzina_ovir(a):
    b = 0
    for i in range(len(a)):
        b += a[i][1] - a[i][0] + 1
    return (b)


def sirina(ovire):
    sirina = None
    for _, x1, _ in ovire:
        if sirina == None or x1 > sirina:
            sirina = x1
    return (sirina)


def pretvori_vrstico(ovire):
    ovire = "." + ovire + "."
    bloki = []

    for i, znak in enumerate(ovire):
        if znak == "#":
            if ovire[i - 1] == ".":
                zacetek = i
            if ovire[i + 1] == ".":
                bloki.append((zacetek, i))
    return (bloki)


def dodaj_vrstico(bloki, y):
    bloki1 = []
    b = bloki1
    for i in range(len(bloki)):
        bloki1.append((bloki[i][0], bloki[i][1], y))
    return (b)


def pretvori_zemljevid(zemljevid):
    lokacija = []
    l = lokacija
    for y, ovire in enumerate(zemljevid):
        a = dodaj_vrstico(pretvori_vrstico(ovire), y + 1)
        for znaki in a:
            l.append(znaki)
    return l


def globina(ovire, x):
    ymin = None
    for x0, x1, yn in ovire:
        if x0 <= x <= x1 and (ymin == None or yn < ymin):
            ymin = yn
    return (ymin)


def naj_stolpec(ovire):
    naj_y = naj_x = 0

    for x in range(1, sirina(ovire) + 1):
        ymin = None
        for x0, x1, yn in ovire:
            if x0 <= x <= x1 and (ymin == None or yn < ymin):
                ymin = yn
        if ymin == None or ymin > naj_y:
            naj_y = ymin
            naj_x = x
            if ymin == None:
                break
    return (naj_x, naj_y)


def senca(ovire):
    seznam = []
    s = seznam
    stolpec = 0
    for ovira in ovire:
        if ovira[1] > stolpec:
            s += [True] * (ovira[1] - stolpec)
            stolpec = ovira[1]
        for i in range(ovira[0] - 1, ovira[1]):
            s[i] = False
    return s

print('zakaj noce updejtat zanimivo')
print('kako sploh deluje to sranje')


import unittest

ovire1 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

ovire2 = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]

ovire3 = [(1, 3, 6), (2, 4, 3),
          (3, 4, 9), (9, 10, 2), (9, 10, 8)]


class Test(unittest.TestCase):
    def test_stevilo_ovir(self):
        self.assertEqual(7, stevilo_ovir(ovire1))
        self.assertEqual(6, stevilo_ovir(ovire2))
        self.assertEqual(0, stevilo_ovir([]))

    def test_dolzina_ovir(self):
        self.assertEqual(19, dolzina_ovir(ovire1))
        self.assertEqual(15, dolzina_ovir(ovire2))
        self.assertEqual(0, dolzina_ovir([]))

    def test_sirina(self):
        self.assertEqual(10, sirina(ovire1))
        self.assertEqual(9, sirina(ovire1[:-2]))
        self.assertEqual(6, sirina(ovire1[:-3]))
        self.assertEqual(3, sirina(ovire1[:1]))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_dodaj_vrstico(self):
        self.assertEqual([(3, 4, 3), (6, 8, 3), (11, 11, 3)], dodaj_vrstico([(3, 4), (6, 8), (11, 11)], 3))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)],
                         pretvori_zemljevid(zemljevid))

        global pretvori_vrstico
        pretvori = pretvori_vrstico
        try:
            def pretvori_vrstico(vrstica):
                return [(i, i) for i, c in enumerate(vrstica) if c == "#"]

            self.assertEqual([(2, 2, 2), (3, 3, 2), (1, 1, 3), (2, 2, 3), (4, 4, 3), (3, 3, 4), (4, 4, 4),
                              (5, 5, 4), (0, 0, 5), (1, 1, 5), (2, 2, 5), (4, 4, 5), (5, 5, 5)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi pretvori_vrstico")
        finally:
            pretvori_vrstico = pretvori

        global dodaj_vrstico
        dodaj = dodaj_vrstico
        try:
            def dodaj_vrstico(ovire, vrstica):
                return [(*o, 2 * vrstica) for o in ovire]

            self.assertEqual([(3, 4, 4), (2, 3, 6), (5, 5, 6), (4, 6, 8), (1, 3, 10), (5, 6, 10)],
                             pretvori_zemljevid(zemljevid),
                             "Funkcija pretvori_zemljevid naj kar lepo uporabi dodaj_vrstico")
        finally:
            dodaj_vrstico = dodaj

    def test_globina(self):
        self.assertEqual(3, globina(ovire1, 3))
        self.assertEqual(5, globina(ovire1, 6))
        self.assertEqual(7, globina(ovire2, 6))
        self.assertIsNone(globina(ovire3, 6))

    def test_naj_stolpec(self):
        self.assertEqual((5, 7), naj_stolpec(ovire1))
        self.assertEqual((7, None), naj_stolpec(ovire2))
        self.assertEqual((5, None), naj_stolpec(ovire3))

    def test_senca(self):
        self.assertEqual([False] * 10, senca(ovire1))
        self.assertEqual([False, False, False, False, False, False, True, True, False, False], senca(ovire2))
        self.assertEqual([False, False, False, False, True, True, True, True, False, False], senca(ovire3))
        self.assertEqual([False] * 6, senca(ovire2[:-3]))
        self.assertEqual([False] * 3, senca(ovire3[:1]))


if __name__ == "__main__":
    unittest.main()


