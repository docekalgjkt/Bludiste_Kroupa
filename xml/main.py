from robot_factory import BasicRobotFactory
from vykresleni import BludisteCanvas
from xml_loader import nacti_bludiste_z_xml
import time


def pohybuj_robotem(robot, robot_view, kroky, vizualizace, prodleva=0.5):
    """Posouvá robota po naplánované cestě."""
    for krok in kroky:
        dx = krok[0] - robot.pozice[0]
        dy = krok[1] - robot.pozice[1]

        if robot.pohni_se((dx, dy)):
            robot_view.aktualizuj()
            vizualizace.okno.update()  # Aktualizuje GUI
            time.sleep(prodleva)  # Zpoždění mezi pohyby


if __name__ == "__main__":
    # Načtení bludiště z XML souboru
    bludiste = nacti_bludiste_z_xml("bludiste.xml")

    # Vytvoření továrny pro robota a jeho zobrazení
    robot_factory = BasicRobotFactory()
    robot = robot_factory.create_robot(bludiste)
    vizualizace = BludisteCanvas(bludiste)
    robot_view = robot_factory.create_robot_view(vizualizace, robot)

    # Vykreslení počátečního stavu
    vizualizace.vykresli_bludiste()
    robot_view.vykresli()

    # Vyhledání cesty a pohyb robota
    kroky = robot.hledej_cestu()
    pohybuj_robotem(robot, robot_view, kroky, vizualizace)

    vizualizace.okno.mainloop()