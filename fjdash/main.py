from abstract_factory import XMLBludisteFactory
from zobrazeni import BludisteCanvas

# Načteme bludiště z XML souboru pomocí továrny
factory = XMLBludisteFactory("bludiste.xml")
bludiste = factory.vytvor_bludiste()
vizualizace = factory.vytvor_zobrazeni(bludiste)

# Spustíme aplikaci
vizualizace.spust()

# Pohyb robota
vizualizace.aktualizuj_pozici((1, 0))  # Pokus o pohyb doprava
vizualizace.aktualizuj_pozici((2, 0))  # Pokus o pohyb dál
