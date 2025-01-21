class RobotView:
    def __init__(self, canvas, robot, barva="red"):
        """
        Inicializace zobrazení robota.
        :param canvas: Instance třídy BludisteCanvas.
        :param robot: Instance třídy Robot.
        :param barva: Barva robota.
        """
        self.canvas = canvas
        self.robot = robot
        self.barva = barva
        self.sprite = None

    def vykresli(self):
        """Vykreslí robota na aktuální pozici."""
        x, y = self.robot.pozice
        x1, y1, x2, y2 = self.canvas._souradnice_policka(x, y)
        if self.sprite:
            self.canvas.canvas.delete(self.sprite)  # Odstraň starý obraz robota
        self.sprite = self.canvas.canvas.create_oval(x1, y1, x2, y2, fill=self.barva)
    def aktualizuj(self):
        """Aktualizuje pozici robota a překreslí jeho sprite."""
        self.vykresli()