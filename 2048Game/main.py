import tkinter as tk
from colors import colors
import random


class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.cellData = None
        self.cells = None
        self.grid()
        self.primary = tk.Frame(self, background=colors["background"], borderwidth=2, width=500, height=500)
        self.primary.grid(pady=10, padx=10, row=0, column=0)

    # Create the initial GUI of blank 4x4 grid
    def gui(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                frame = tk.Frame(self.primary, background=colors["cell"], width=100, height=100)
                number = tk.Label(self.primary, background=colors["cell"])
                number.grid(row=i, column=j)
                frame.grid(row=i, column=j, padx=10, pady=10)
                finalFrame = {"frame": frame, "number": number}
                row.append(finalFrame)
            self.cells.append(row)

    # Add the initial two cells with value 2 to the storage matrix and the display
    def start(self):
        self.cellData = [[0] * 4 for _ in range(4)]
        print(self.cellData)
        for i in range(2):
            randRow = random.randint(0, 3)
            randCol = random.randint(0, 3)
            self.cellData[randRow][randCol] = 2
            self.cells[randRow][randCol]["frame"].configure(background=colors[2])
            self.cells[randRow][randCol]["number"].configure(background=colors[2], text="2", font=colors["font"], fg=colors["fontColor"])


myapp = Game()
myapp.gui()
myapp.start()

myapp.master.title("2048")
myapp.master.minsize(600, 600)
myapp.master.maxsize(1200, 1200)

myapp.mainloop()
