class Bludiste:
    def __init__(self, sirka, vyska, zacatek, konec, mapa):

        self.sirka = sirka
        self.vyska = vyska
        self.zacatek = zacatek
        self.konec = konec
        self.mapa = mapa
        self.pozice = zacatek

    def lze_se_pohnout(self, x, y):

        if 0 <= x < self.sirka and 0 <= y < self.vyska:
            return self.mapa[y][x] in (0, 'E')  # Volná cesta nebo východ
        return False

    def presun(self, x, y):

        if self.lze_se_pohnout(x, y):
            self.pozice = (x, y)
            return True
        return False

    def u_konecu(self):

        return self.pozice == self.konec
    def vykresli_bludiste(self):

        for y, radek in enumerate(self.mapa):
            for x, bunka in enumerate(radek):
                if (x, y) == self.pozice:
                    print("R", end=" ")
                elif bunka == 1:
                    print("1", end=" ")
                elif bunka == 'E':
                    print("E", end=" ")
                else:
                    print("0", end=" ")
            print()  # Další řádek
        print()