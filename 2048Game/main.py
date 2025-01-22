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
                                                             fg=colors["fontColor24"])

    # Generate the random new 2 cell
    def randomTile(self):
        twoOrFour = random.randint(1, 10)
        newValue = 2
        if twoOrFour == 1: newValue = 4
        def genPos():
            randRow = random.randint(0, 3)
            randCol = random.randint(0, 3)
            return randRow, randCol
        row, col = genPos()
        while self.cellData[row][col] != 0:
            row, col = genPos()
        self.cellData[row][col] = newValue
        self.cells[row][col]["frame"].configure(background=colors[newValue])
        self.cells[row][col]["number"].configure(background=colors[newValue], text=str(newValue), font=colors["font"],
                                                 fg=colors["fontColor24"])

    def updateGUI(self):
        for i in range(4):
            for j in range(4):
                self.cells[i][j]["frame"].configure(background=colors[self.cellData[i][j]])
                if self.cellData[i][j] == 2 or self.cellData[i][j] == 4:
                    self.cells[i][j]["number"].configure(background=colors[self.cellData[i][j]],
                                                         text=str(self.cellData[i][j]), font=colors["font"],
                                                         fg=colors["fontColor24"])
                elif self.cellData[i][j] != 0:
                    self.cells[i][j]["number"].configure(background=colors[self.cellData[i][j]],
                                                         text=str(self.cellData[i][j]), font=colors["font"],
                                                         fg=colors["fontColorOthers"])
                else:
                    self.cells[i][j]["number"].configure(background=colors[self.cellData[i][j]], text="",
                                                         font=colors["font"], fg=colors["fontColorOthers"])

    def moveLeft(self, event):
        # Check if this move can be done
        validMove = False
        for i in range(4):
            for j in range(3):
                if self.cellData[i][j] == 0 and self.cellData[i][j + 1] != 0 or (self.cellData[i][j] != 0 and (self.cellData[i][j] == self.cellData[i][j + 1])):
                    validMove = True
                    break
            if validMove: break

        if validMove:
            for i in range(4):
                for j in range(1, 4):
                    if self.cellData[i][j] != 0:
                        moveTo = j
                        while moveTo > 0 and self.cellData[i][moveTo - 1] == 0:
                            moveTo -= 1
                        if moveTo != j:
                            self.cellData[i][moveTo] = self.cellData[i][j]
                            self.cellData[i][j] = 0
            for i in range(4):
                for j in range(3):
                    if self.cellData[i][j] == self.cellData[i][j + 1]:
                        self.cellData[i][j] *= 2
                        self.cellData[i][j + 1] = 0
                        for k in range(j + 1, 3):
                            if self.cellData[i][k] == 0:
                                self.cellData[i][k] = self.cellData[i][k + 1]
                                self.cellData[i][k + 1] = 0

            self.updateGUI()
            self.randomTile()

    def moveRight(self, event):
        # Check if this move can be done
        validMove = False
        for i in range(4):
            for j in range(3, 0, -1):
                if self.cellData[i][j] == 0 and self.cellData[i][j - 1] != 0 or (self.cellData[i][j] != 0 and (self.cellData[i][j] == self.cellData[i][j - 1])):
                    validMove = True
                    break
            if validMove: break

        if validMove:
            for i in range(4):
                for j in range(2, -1, -1):
                    if self.cellData[i][j] != 0:
                        moveTo = j
                        while moveTo < 3 and self.cellData[i][moveTo + 1] == 0:
                            moveTo += 1
                        if moveTo != j:
                            self.cellData[i][moveTo] = self.cellData[i][j]
                            self.cellData[i][j] = 0
            for i in range(4):
                for j in range(3, 0, -1):
                    if self.cellData[i][j] == self.cellData[i][j - 1]:
                        self.cellData[i][j] *= 2
                        self.cellData[i][j - 1] = 0
                        for k in range(j - 1, 0, -1):
                            if self.cellData[i][k] == 0:
                                self.cellData[i][k] = self.cellData[i][k - 1]
                                self.cellData[i][k - 1] = 0
            self.updateGUI()
            self.randomTile()

    def moveUp(self, event):
        # Check if this move can be done
        validMove = False
        for j in range(4):
            for i in range(3):
                if self.cellData[i][j] == 0 and self.cellData[i + 1][j] != 0 or (self.cellData[i][j] != 0 and (self.cellData[i][j] == self.cellData[i + 1][j])):
                    validMove = True
                    break
            if validMove: break

        if validMove:
            for j in range(4):
                for i in range(1, 4):
                    if self.cellData[i][j] != 0:
                        moveTo = i
                        while moveTo > 0 and self.cellData[moveTo - 1][j] == 0:
                            moveTo -= 1
                        if moveTo != i:
                            self.cellData[moveTo][j] = self.cellData[i][j]
                            self.cellData[i][j] = 0
            for j in range(4):
                for i in range(3):
                    if self.cellData[i][j] == self.cellData[i + 1][j]:
                        self.cellData[i][j] *= 2
                        self.cellData[i + 1][j] = 0
                        for k in range(i + 1, 3):
                            if self.cellData[k][j] == 0:
                                self.cellData[k][j] = self.cellData[k + 1][j]
                                self.cellData[k + 1][j] = 0
            self.updateGUI()
            self.randomTile()

    def moveDown(self, event):
        # Check if this move can be done
        validMove = False
        for j in range(4):
            for i in range(3, 0, -1):
                if self.cellData[i][j] == 0 and self.cellData[i - 1][j] != 0 or (self.cellData[i][j] != 0 and (self.cellData[i][j] == self.cellData[i - 1][j])):
                    validMove = True
                    break
            if validMove: break

        if validMove:
            for j in range(4):
                for i in range(2, -1, -1):
                    if self.cellData[i][j] != 0:
                        moveTo = i
                        while moveTo < 3 and self.cellData[moveTo + 1][j] == 0:
                            moveTo += 1
                        if moveTo != i:
                            self.cellData[moveTo][j] = self.cellData[i][j]
                            self.cellData[i][j] = 0
            for j in range(4):
                for i in range(3, 0, -1):
                    if self.cellData[i][j] == self.cellData[i - 1][j]:
                        self.cellData[i][j] *= 2
                        self.cellData[i - 1][j] = 0
                        for k in range(i - 1, 3):
                            if self.cellData[k][j] == 0:
                                self.cellData[k][j] = self.cellData[k - 1][j]
                                self.cellData[k - 1][j] = 0
            self.updateGUI()
            self.randomTile()


myapp = Game()
myapp.gui()
myapp.start()

myapp.master.title("2048")
myapp.master.minsize(600, 600)
myapp.master.maxsize(1200, 1200)

myapp.cellData[0][0] = 2
myapp.cellData[0][1] = 2
myapp.cellData[0][2] = 4
myapp.updateGUI()

myapp.mainloop()
