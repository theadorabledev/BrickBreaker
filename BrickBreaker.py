from Tkinter import *
HEIGHT=11
class Application(Frame):                    
    def movePlatform(self,event):
        move = 1
        if event.keysym == "Left":
            move = -1

        if self.selectedPos + move < 0 or self.selectedPos + move > 20:
            return False            
        self.grid[len(self.grid)-1][self.selectedPos] = "   "
        self.selectedPos += move
        self.grid[len(self.grid)-1][self.selectedPos] = "---"

        self.updateGridAsText()
        self.createWidgets()
    def updateGridAsText(self):
        self.gridAsText=""
        for row in self.grid:
            self.gridAsText += "".join(row) + "\n"
    def createWidgets(self):        
        self.game = Label(self, text=self.gridAsText, font='TkFixedFont', borderwidth=4, relief="groove",)
        self.game.grid(row=1, column=1)
    def swapShowMoves(self):
        self.showMoves = not self.showMoves
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        reduce(list.__add__, [["   "] * 21] * 10, [])
        self.grid= [["   "] * 21] * (HEIGHT-1)
        self.grid.append ((["   "] * 10) + ["---"] + (["   "] * 10) )
        self.bind("<Left>", self.movePlatform)
        self.bind("<Right>", self.movePlatform)
        self.focus_set()
        self.gridAsText=""
        self.updateGridAsText()
        self.master.title="Thud!"
        self.createWidgets()
        self.selectedPos=10
        
        


if __name__ == "__main__":
    root = Tk()   
    root.geometry="2000x1500"
    app = Application(master=root)
    app.mainloop()
    root.destroy()
