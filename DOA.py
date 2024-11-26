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
        self.vychod  vychod
        self.mapa = mapa
        self.pozice = start


class BludisteDAO:
    def uloz_do_textu(self, bludiste, nazev_souboru):
        """
        Uloží objekt Bludiste do textového souboru.

        :param bludiste: Instance třídy Bludiste
        :param nazev_souboru: Název textového souboru pro uložení
        """
        with open(nazev_souboru, 'w') as file:
            # Uložení základních parametrů
            file.write(f"{bludiste.sirka}\n")
            file.write(f"{bludiste.vyska}\n")
            file.write(f"{bludiste.start[0]},{bludiste.start[1]}\n")
            file.write(f"{bludiste.vychod[0]},{bludiste.vychod[1]}\n")

            # Uložení mapy bludiště
            for radek in bludiste.mapa:
                file.write(','.join(map(str, radek)) + "\n")

    def nacti_z_textu(self, nazev_souboru):
        """
        Načte objekt Bludiste z textového souboru.

        :param nazev_souboru: Název textového souboru pro načtení
        :return: Instance třídy Bludiste
        """
        with open(nazev_souboru, 'r') as file:
            # Načtení základních parametrů
            sirka = int(file.readline().strip())
            vyska = int(file.readline().strip())

            # Načtení počáteční a výstupní pozice
            start = tuple(map(int, file.readline().strip().split(',')))
            vychod = tuple(map(int, file.readline().strip().split(',')))

            # Načtení mapy bludiště
            mapa = []
            for radek in file:
                mapa.append([int(x) if x.isdigit() else x for x in radek.strip().split(',')])

        # Vytvoření a vrácení instance bludiště
        return Bludiste(sirka, vyska, start, vychod, mapa)


# Příklad bludiště (0 = cesta, 1 = zeď, 'E' = východ)
mapa = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 'E']
]

# Inicializace objektu Bludiste
bludiste = Bludiste(4, 4, (0, 0), (3, 3), mapa)

# Inicializace DAO třídy
bludiste_dao = BludisteDAO()

# Uložení bludiště do textového souboru
nazev_souboru = "bludiste.txt"
bludiste_dao.uloz_do_textu(bludiste, nazev_souboru)
print(f"Bludiště bylo uloženo do souboru '{nazev_souboru}'.")

# Načtení bludiště z textového souboru
nactene_bludiste = bludiste_dao.nacti_z_textu(nazev_souboru)
print(f"Bludiště bylo načteno ze souboru '{nazev_souboru}':")
print("Šířka:", nactene_bludiste.sirka)
print("Výška:", nactene_bludiste.vyska)
print("Startovní pozice:", nactene_bludiste.start)
print("Východ:", nactene_bludiste.vychod)
print("Mapa:")
for radek in nactene_bludiste.mapa:
    print(radek)
