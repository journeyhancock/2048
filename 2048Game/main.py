import tkinter as tk
from colors import colors
import random
import time


class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.cellData = None
        self.cells = None
        self.grid()
        self.primary = tk.Frame(self, background=colors["background"], borderwidth=2, width=500, height=500)
        self.primary.grid(pady=10, padx=10, row=0, column=0)
        self.master.bind("<Left>", self.moveLeft)
        self.master.bind("<Right>", self.moveRight)
        self.master.bind("<Up>", self.moveUp)
        self.master.bind("<Down>", self.moveDown)

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
        def genPos():
            randRow = random.randint(0, 3)
            randCol = random.randint(0, 3)
            return randRow, randCol
        for i in range(2):
            row, col = genPos()
            while self.cellData[row][col] != 0:
                row, col = genPos()
            self.cellData[row][col] = 2
            self.cells[row][col]["frame"].configure(background=colors[2])
            self.cells[row][col]["number"].configure(background=colors[2], text="2", font=colors["font"],
                                                             fg=colors["fontColor"])

    def updateGUI(self):
        for i in range(4):
            for j in range(4):
                self.cells[i][j]["frame"].configure(background=colors[self.cellData[i][j]])
                if self.cellData[i][j] != 0:
                    self.cells[i][j]["number"].configure(background=colors[self.cellData[i][j]],
                                                         text=str(self.cellData[i][j]), font=colors["font"],
                                                         fg=colors["fontColor"])
                else:
                    self.cells[i][j]["number"].configure(background=colors[self.cellData[i][j]], text="",
                                                         font=colors["font"], fg=colors["fontColor"])

    def moveLeft(self, event):
        for i in range(4):
            for j in range(1, 4):
                if self.cellData[i][j] != 0:
                    moveTo = j
                    while self.cellData[i][moveTo - 1] == 0 and moveTo > 0:
                        moveTo -= 1
                    if moveTo != j:
                        self.cellData[i][moveTo] = self.cellData[i][j]
                        self.cellData[i][j] = 0
                    if self.cellData[i][moveTo] == self.cellData[i][moveTo - 1]:
                        self.cellData[i][moveTo - 1] *= 2
                        self.cellData[i][moveTo] = 0
                        print(self.cellData)
        self.updateGUI()

    def moveRight(self, event):
        return

    def moveUp(self, event):
        return

    def moveDown(self, event):
        return


myapp = Game()
myapp.gui()
myapp.start()

myapp.master.title("2048")
myapp.master.minsize(600, 600)
myapp.master.maxsize(1200, 1200)

myapp.mainloop()
