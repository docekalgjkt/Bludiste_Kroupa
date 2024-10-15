import tkinter as tk


class BludisteCanvas:
    def __init__(self, bludiste, velikost_bunky=50):
        """
        Inicializace třídy pro vykreslování bludiště pomocí tkinter Canvas.

        :param bludiste: Instance třídy Bludiste
        :param velikost_bunky: Velikost jedné buňky v canvasu (v pixelech)
        """
        self.bludiste = bludiste
        self.velikost_bunky = velikost_bunky
        self.okno = tk.Tk()
        self.canvas = tk.Canvas(self.okno, width=self.bludiste.sirka * velikost_bunky,
                                height=self.bludiste.vyska * velikost_bunky)
        self.canvas.pack()

    def vykresli_bludiste(self):
        """
        Vykreslení celého bludiště na canvas.
        """
        self.canvas.delete("all")  # Smazání starých vykreslených prvků
        for y in range(self.bludiste.vyska):
            for x in range(self.bludiste.sirka):
                x1 = x * self.velikost_bunky
                y1 = y * self.velikost_bunky
                x2 = x1 + self.velikost_bunky
                y2 = y1 + self.velikost_bunky

                # Zdi
                if self.bludiste.mapa[y][x] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                # Východ
                elif self.bludiste.mapa[y][x] == 'E':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                # Volná cesta
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

        # Vykreslení robota
        x_robot, y_robot = self.bludiste.pozice
        x1 = x_robot * self.velikost_bunky
        y1 = y_robot * self.velikost_bunky
        x2 = x1 + self.velikost_bunky
        y2 = y1 + self.velikost_bunky
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")  # Robot je vykreslen jako kruh

    def aktualizuj_pozici(self, nova_pozice):
        """
        Aktualizace pozice robota v bludišti a překreslení canvasu.

        :param nova_pozice: Nová pozice robota (x, y)
        """
        if self.bludiste.pohnout(nova_pozice):
            self.vykresli_bludiste()
        else:
            print("Pohyb se nezdařil - narazil do zdi nebo mimo mapu.")

    def spust(self):
        """
        Spuštění grafického rozhraní tkinter.
        """
        self.vykresli_bludiste()  # Prvotní vykreslení bludiště
        self.okno.mainloop()
