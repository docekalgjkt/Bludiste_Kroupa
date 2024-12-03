import xml.etree.ElementTree as ET
from xml.dom import minidom
from bludiste import Bludiste

class MazeDAOXML:
    def __init__(self, database, filename):
        self.database = database
        self.filename = filename

    def save_maze(self, maze_object):
        """
        Uloží bludiště do XML.
        :param maze_object: Instance třídy Bludiste.
        """
        filepath = f"{self.database}/{self.filename}"
        maze_name = input("Zadejte název bludiště:\n> ")
        maze_level = input("Zadejte úroveň bludiště:\n> ")

        # Vytvoření kořenového elementu
        root = ET.Element("mazes")
        try:
            # Pokus o načtení existujícího XML
            tree = ET.parse(filepath)
            root = tree.getroot()
        except FileNotFoundError:
            pass

        # Přidání nového bludiště
        maze_elem = ET.SubElement(root, "maze", name=maze_name, level=maze_level)
        metadata = ET.SubElement(maze_elem, "metadata")
        ET.SubElement(metadata, "start").text = str(maze_object.start)
        ET.SubElement(metadata, "exit").text = str(maze_object.vychod)

        # Uložení mřížky bludiště
        grid = ET.SubElement(maze_elem, "grid")
        for row in maze_object.mapa:
            row_elem = ET.SubElement(grid, "row")
            row_elem.text = " ".join(map(str, row))

        # Zápis do souboru
        tree = ET.ElementTree(root)
        with open(filepath, "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)

    def load_maze(self, level):
        """
        Načte bludiště na základě úrovně.
        :param level: Úroveň bludiště.
        :return: Instance třídy Bludiste.
        """
        filepath = f"{self.database}/{self.filename}"
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()

            for maze_elem in root.findall("maze"):
                if maze_elem.get("level") == level:
                    # Načtení metadat
                    metadata = maze_elem.find("metadata")
                    start = eval(metadata.find("start").text)
                    exit_ = eval(metadata.find("exit").text)

                    # Načtení mřížky
                    grid = maze_elem.find("grid")
                    maze_data = [
                        [int(cell) for cell in row.text.split()]
                        for row in grid.findall("row")
                    ]

                    return Bludiste(
                        sirka=len(maze_data[0]),
                        vyska=len(maze_data),
                        start=start,
                        vychod=exit_,
                        mapa=maze_data
                    )

            raise ValueError(f"Bludiště s úrovní {level} nebylo nalezeno.")

        except FileNotFoundError:
            print("Soubor nebyl nalezen.")
        except Exception as e:
            print(f"Chyba při načítání: {e}")

    def get_all_levels(self):
        """
        Načte všechny úrovně dostupné v XML souboru.
        :return: Seznam úrovní.
        """
        filepath = f"{self.database}/{self.filename}"
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()

            levels = [maze.get("level") for maze in root.findall("maze")]
            return levels
        except FileNotFoundError:
            print("Soubor nebyl nalezen.")
        except Exception as e:
            print(f"Chyba při načítání úrovní: {e}")

        return []

if __name__ == "__main__":
    # Vytvoření instance bludiště
    maze = Bludiste(
        sirka=5,
        vyska=5,
        start=(1, 0),
        vychod=(2, 4),
        mapa=[
            [0, 1, 1, 1, 1],
            [8, 0, 0, 1, 0],
            [1, 1, 0, 1, 3],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1]
        ]
    )

    # Uloží bludiště
    dao = MazeDAOXML("saved_levels", "levels.xml")
    dao.save_maze(maze)

    # Načte bludiště podle úrovně
    loaded_maze = dao.load_maze(level="1")
    loaded_maze.zobraz_bludiste()

    # Načte všechny úrovně
    print(dao.get_all_levels())
