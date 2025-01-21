class Robot:
    def __init__(self, bludiste):
        """
        Inicializace robota.
        :param bludiste: Instance třídy Bludiste.
        """
        self.bludiste = bludiste
        self.pozice = bludiste.zacatek
        self.cesta = []

    def pohni_se(self, smer):
        """
        Posune robota podle zadaného směru.
        :param smer: Smer pohybu (např. (0, 1) dolů).
        :return: True, pokud se pohyb povedl, jinak False.
        """
        nova_pozice = (self.pozice[0] + smer[0], self.pozice[1] + smer[1])
        if self.bludiste.presun(*nova_pozice):
            self.pozice = nova_pozice
            self.cesta.append(nova_pozice)
            return True
        return False

    def hledej_cestu(self):
        """
        Hledání cesty bludištěm pomocí jednoduchého algoritmu (DFS).
        :return: Seznam kroků.
        """
        navstivene = set()
        stack = [(self.pozice, [])]

        while stack:
            aktualni_pozice, cesta = stack.pop()
            if aktualni_pozice in navstivene:
                continue
            navstivene.add(aktualni_pozice)

            if aktualni_pozice == self.bludiste.konec:
                return cesta

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nova_pozice = (aktualni_pozice[0] + dx, aktualni_pozice[1] + dy)
                if self.bludiste.lze_se_pohnout(*nova_pozice):
                    stack.append((nova_pozice, cesta + [nova_pozice]))
        return []