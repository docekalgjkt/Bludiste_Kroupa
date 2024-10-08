import tkinter as tk
from tkinter import messagebox
import random

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bludiště - Nastavení")

        # Inicializace proměnných pro řádky a sloupce (musí být liché pro správnou strukturu bludiště)
        self.rows = tk.IntVar(value=21)  # Doporučeno liché číslo
        self.cols = tk.IntVar(value=21)  # Doporučeno liché číslo
        self.cell_size = 20  # Velikost buňky v pixelech

        # Vytvoření rámce pro vstupní data
        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack()

        # Vstup pro počet řádků
        tk.Label(frame, text="Počet řádků (liché číslo):").grid(row=0, column=0, sticky="e")
        self.entry_rows = tk.Entry(frame, textvariable=self.rows)
        self.entry_rows.grid(row=0, column=1)

        # Vstup pro počet sloupců
        tk.Label(frame, text="Počet sloupců (liché číslo):").grid(row=1, column=0, sticky="e")
        self.entry_cols = tk.Entry(frame, textvariable=self.cols)
        self.entry_cols.grid(row=1, column=1)

        # Tlačítko pro generování a vykreslení bludiště
        self.btn_generate = tk.Button(frame, text="Generovat bludiště", command=self.generate_maze)
        self.btn_generate.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_maze(self):
        try:
            rows = self.rows.get()
            cols = self.cols.get()

            if rows < 5 or cols < 5:
                raise ValueError("Počet řádků a sloupců musí být alespoň 5.")
            if rows % 2 == 0 or cols % 2 == 0:
                raise ValueError("Počet řádků a sloupců musí být liché číslo.")

            # Generování perfektního bludiště pomocí DFS
            maze = self.create_perfect_maze(rows, cols)

            # Zavření nastavení okna a otevření bludiště
            self.open_maze_window(maze, rows, cols)
        except Exception as e:
            messagebox.showerror("Chyba", str(e))

    def create_perfect_maze(self, rows, cols):
        # Inicializace bludiště s veškerými stěnami
        maze = [[1 for _ in range(cols)] for _ in range(rows)]

        # Startovní bod
        start_row, start_col = 1, 1
        maze[start_row][start_col] = 0

        # Stack pro DFS
        stack = [(start_row, start_col)]

        # Směry: N, S, E, W
        directions = [(-2, 0), (2, 0), (0, 2), (0, -2)]

        while stack:
            current_cell = stack[-1]
            row, col = current_cell
            neighbors = []

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 1 <= nr < rows-1 and 1 <= nc < cols-1 and maze[nr][nc] == 1:
                    neighbors.append((nr, nc))

            if neighbors:
                # Náhodně vybereme sousední buňku
                next_cell = random.choice(neighbors)
                nr, nc = next_cell

                # Odstraníme zeď mezi aktuální a sousední buňkou
                wall_row, wall_col = (row + nr) // 2, (col + nc) // 2
                maze[wall_row][wall_col] = 0
                maze[nr][nc] = 0

                # Přidáme sousední buňku do stacku
                stack.append((nr, nc))
            else:
                # Zpět do předchozí buňky
                stack.pop()

        # Nastavení startovní a cílové pozice
        maze[1][1] = 0  # Start (může být upraveno dle potřeby)
        maze[rows-2][cols-2] = 0  # Cíl (může být upraveno dle potřeby)

        return maze

    def open_maze_window(self, maze, rows, cols):
        # Vytvoření nového okna pro vykreslení bludiště
        maze_window = tk.Toplevel(self.root)
        maze_window.title("Bludiště")

        canvas_width = cols * self.cell_size
        canvas_height = rows * self.cell_size

        canvas = tk.Canvas(maze_window, width=canvas_width, height=canvas_height)
        canvas.pack()

        self.draw_maze(canvas, maze, rows, cols)

    def draw_maze(self, canvas, maze, rows, cols):
        for row in range(rows):
            for col in range(cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                if maze[row][col] == 1:
                    color = "black"
                elif (row, col) == (1, 1):
                    color = "green"  # Startovní bod
                elif (row, col) == (rows-2, cols-2):
                    color = "red"    # Cíl
                else:
                    color = "white"
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

def main():
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
