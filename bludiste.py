class Bludiste:
    def __init__(self, sirka, vyska, start, vychod, mapa):
        """
        Inicializace bludiště.

        :param sirka: šířka bludiště (počet sloupců)
        :param vyska: výška bludiště (počet řádků)
        :param start: počáteční pozice robota (x, y)
        :param vychod: pozice východu (x, y)
        :param mapa: 2D pole reprezentující bludiště (0 = volná cesta, 1 = zeď, 'E' = východ)
        """
        self.sirka = sirka
        self.vyska = vyska
        self.start = start
        self.vychod = vychod
        self.mapa = mapa
        self.pozice = start

    def muzu_se_pohnout(self, nova_pozice):
        """
        Kontrola, jestli je možné se na danou pozici pohnout (tj. není tam zeď a je v rozsahu mapy).

        :param nova_pozice: nová pozice (x, y)
        :return: True, pokud se může robot pohnout, False jinak
        """
        x, y = nova_pozice
        if 0 <= x < self.sirka and 0 <= y < self.vyska:
            # Kontrola, zda na dané pozici není zeď (1)
            if self.mapa[y][x] == 0 or self.mapa[y][x] == 'E':
                return True
        return False

    def pohnout(self, nova_pozice):
        """
        Pokus o přesun na novou pozici. Vrátí informaci, zda se přesun povedl.

        :param nova_pozice: nová pozice (x, y)
        :return: True, pokud přesun proběhl, False jinak
        """
        if self.muzu_se_pohnout(nova_pozice):
            self.pozice = nova_pozice
            return True
        return False

    def je_u_vychodu(self):
        """
        Kontrola, zda je robot u východu.

        :return: True, pokud je robot na pozici východu, False jinak
        """
        return self.pozice == self.vychod

    def zobraz_bludiste(self):
        """
        Zobrazí bludiště s aktuální pozicí robota.
        """
        for y in range(self.vyska):
            radek = ""
            for x in range(self.sirka):
                if (x, y) == self.pozice:
                    radek += "R "  # Robot
                elif self.mapa[y][x] == 1:
                    radek += "1 "  # Zeď
                elif self.mapa[y][x] == 'E':
                    radek += "E "  # Východ
                else:
                    radek += "0 "  # Volná cesta
            print(radek)
        print()
