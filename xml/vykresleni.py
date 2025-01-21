import tkinter as tk


class BludisteCanvas:
    def __init__(self, bludiste, velikost_bunky=50):
        """
        Inicializuje canvas pro vykreslování bludiště.
        :param bludiste: Instance třídy Bludiste.
        :param velikost_bunky: Velikost jedné buňky na canvasu (v pixelech).
        """
        self.bludiste = bludiste
        self.velikost_bunky = velikost_bunky
        self.okno = tk.Tk()
        self.okno.title("Bludiště")
        self.canvas = self._inicializuj_canvas()

    def _inicializuj_canvas(self):
        """Inicializuje a vrátí Canvas pro vykreslování."""
        sirka = self.bludiste.sirka * self.velikost_bunky
        vyska = self.bludiste.vyska * self.velikost_bunky
        canvas = tk.Canvas(self.okno, width=sirka, height=vyska)
        canvas.pack()
        return canvas

    def vykresli_bludiste(self):
        """Vykreslí celou mapu bludiště na canvas."""
        self.canvas.delete("all")  # Vyčištění předchozího obsahu
        for y, radek in enumerate(self.bludiste.mapa):
            for x, policko in enumerate(radek):
                self._vykresli_policko(x, y, policko)
    def _vykresli_policko(self, x, y, typ):
        """Vykreslí jedno políčko na základě jeho typu."""
        x1, y1, x2, y2 = self._souradnice_policka(x, y)
        barva = {
            0: "white",  # Volná cesta
            1: "black",  # Zeď
            'E': "green"  # Východ
        }.get(typ, "gray")
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=barva)

    def _vykresli_robota(self):
        """Vykreslí robota jako kruh na aktuální pozici."""
        x, y = self.bludiste.pozice
        x1, y1, x2, y2 = self._souradnice_policka(x, y)
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def _souradnice_policka(self, x, y):
        """Vrátí souřadnice (x1, y1, x2, y2) daného políčka v canvasu."""
        x1 = x * self.velikost_bunky
        y1 = y * self.velikost_bunky
        x2 = x1 + self.velikost_bunky
        y2 = y1 + self.velikost_bunky
        return x1, y1, x2, y2

    def aktualizuj_pozici(self, nova_pozice):
        """
        Aktualizuje pozici robota a překreslí bludiště.
        :param nova_pozice: Nová pozice robota (x, y).
        """
        if self.bludiste.pohnout(nova_pozice):
            self.vykresli_bludiste()
        else:
            print("Pohyb se nezdařil - narazil do zdi nebo mimo mapu.")

    def spust(self):
        """Spustí hlavní smyčku grafického rozhraní."""
        self.vykresli_bludiste()
        self.okno.mainloop()