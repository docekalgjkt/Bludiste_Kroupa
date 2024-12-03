import csv
import numpy as np
from bludiste import Bludiste  # Import vaší třídy Bludiste

class MazeDAOCSV:
    def __init__(self, database, filename):
        self.database = database
        self.filename = filename

    def save_maze(self, maze_object):
        """
        Uloží bludiště do CSV.
        :param maze_object: Instance třídy Bludiste.
        """
        filepath = f"{self.database}/{self.filename}"
        maze_name = input("Zadejte název bludiště:\n> ")
        maze_level = input("Zadejte úroveň bludiště:\n> ")

        with open(filepath, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Uložení metadat
            writer.writerow([f"maze_name={maze_name}", f"level={maze_level}"])
            writer.writerow([f"start={maze_object.start}", f"exit={maze_object.vychod}"])

            # Uložení buněk bludiště
            for row in maze_object.mapa:
                writer.writerow(row)

            # Prázdný řádek pro oddělení bludišť
            writer.writerow([])

    def load_maze(self, level):
        """
        Načte bludiště na základě úrovně.
        :param level: Úroveň bludiště.
        :return: Instance třídy Bludiste.
        """
        filepath = f"{self.database}/{self.filename}"
        try:
            with open(filepath, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                maze_found = False
                maze_data = []
                start = None
                exit_ = None

                for row in reader:
                    # Přeskakuje prázdné řádky
                    if not row:
                        continue

                    # Najde bludiště s odpovídající úrovní
                    if row[0].startswith("maze_name=") and row[1] == f"level={level}":
                        maze_found = True
                        continue
                    elif row[0].startswith("maze_name=") and maze_found:
                        break  # Ukončení při nalezení dalšího bludiště

                    # Načte metadata
                    if maze_found and row[0].startswith("start="):
                        start = eval(row[0].split('=')[1])
                        exit_ = eval(row[1].split('=')[1])
                        continue

                    # Načte buňky bludiště
                    if maze_found:
                        maze_data.append([int(cell) for cell in row])

                if maze_data and start and exit_:
                    return Bludiste(
                        sirka=len(maze_data[0]),
                        vyska=len(maze_data),
                        start=start,
                        vychod=exit_,
                        mapa=maze_data
                    )
                else:
                    raise ValueError(f"Bludiště s úrovní {level} nebylo nalezeno.")

        except FileNotFoundError:
            print("Soubor nebyl nalezen.")

    def get_all_levels(self):
        """
        Načte všechny úrovně dostupné v CSV souboru.
        :return: Seznam úrovní.
        """
        filepath = f"{self.database}/{self.filename}"
        try:
            with open(filepath, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                levels = [row[1].split('=')[1] for row in reader if row and row[1].startswith("level=")]
                return levels
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
    dao = MazeDAOCSV("saved_levels", "levels.csv")
    dao.save_maze(maze)

    # Načte bludiště podle úrovně
    loaded_maze = dao.load_maze(level="1")
    loaded_maze.zobraz_bludiste()

    # Načte všechny úrovně
    print(dao.get_all_levels())
