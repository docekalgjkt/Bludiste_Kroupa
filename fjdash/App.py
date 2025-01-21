import tkinter as tk
from AbstractDAO import XMLBludisteFactory
from zobrazeni import BludisteCanvas


def spust_aplikaci(xml_soubor):
    """
    Funkce pro spuštění celé aplikace s načítáním bludiště z XML souboru.

    :param xml_soubor: cesta k XML souboru s popisem bludiště
    """
    # Vytvoření továrny pro načtení bludiště z XML
    factory = XMLBludisteFactory(xml_soubor)

    # Vytvoření instance bludiště a vizualizace
    bludiste = factory.vytvor_bludiste()
    vizualizace = factory.vytvor_zobrazeni(bludiste)

    # Spuštění aplikace
    vizualizace.spust()

    # Příklad aktualizace pozice robota - můžete to volat i interaktivně
    vizualizace.aktualizuj_pozici((1, 0))  # Pokus o pohyb doprava
    vizualizace.aktualizuj_pozici((2, 0))  # Pokus o pohyb dál


# Volání funkce pro spuštění aplikace s konkrétním XML souborem
if __name__ == "__main__":
    xml_soubor = "bludiste.xml"  # Cesta k souboru s mapou bludiště
    spust_aplikaci(xml_soubor)
