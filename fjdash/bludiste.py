import xml.etree.ElementTree as ET


class Bludiste:
    def __init__(self, sirka, vyska, start, vychod, mapa):
        self.sirka = sirka
        self.vyska = vyska
        self.start = start
        self.vychod = vychod
        self.mapa = mapa
        self.pozice = start

    @classmethod
    def z_nacist_z_xml(cls, soubor):
        """
        Načte bludiště z XML souboru.
        """
        tree = ET.parse(soubor)
        root = tree.getroot()

        sirka = int(root.find('sirka').text)
        vyska = int(root.find('vyska').text)
        start = tuple(map(int, root.find('start').text.split(',')))
        vychod = tuple(map(int, root.find('vychod').text.split(',')))

        mapa = []
        for row in root.findall('radek'):
            mapa.append([int(cell.text) if cell.text.isdigit() else cell.text for cell in row])

        return cls(sirka, vyska, start, vychod, mapa)

    def muzu_se_pohnout(self, nova_pozice):
        x, y = nova_pozice
        if 0 <= x < self.sirka and 0 <= y < self.vyska:
            if self.mapa[y][x] == 0 or self.mapa[y][x] == 'E':
                return True
        return False

    def pohnout(self, nova_pozice):
        if self.muzu_se_pohnout(nova_pozice):
            self.pozice = nova_pozice
            return True
        return False

    def je_u_vychodu(self):
        return self.pozice == self.vychod

    def zobraz_bludiste(self):
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
