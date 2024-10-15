from bludiste import Bludiste
from zobrazeni import BludisteCanvas
# Příklad bludiště (0 = cesta, 1 = zeď, 'E' = východ)
mapa = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 'E']
]

# Inicializace bludiště
bludiste = Bludiste(4, 4, (0, 0), (3, 3), mapa)

# Inicializace třídy s canvasem
vizualizace = BludisteCanvas(bludiste)

# Spuštění aplikace s vizualizací
vizualizace.spust()

# Aktualizace pozice robota (může být volána externě nebo interaktivně)
vizualizace.aktualizuj_pozici((1, 0))  # Pokus o pohyb doprava
vizualizace.aktualizuj_pozici((2, 0))  # Pokus o pohyb dál
