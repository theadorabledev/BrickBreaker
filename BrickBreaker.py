from Tkinter import *
import time
HEIGHT = 11
WIDTH = 21
BRICKHEIGHT = 2
class Application(Frame): 
    
    def moveBall(self):
        newX = self.ballPos[0] + self.ballDirection[0]
        newY = self.ballPos[1] + self.ballDirection[1]
        if newX >= HEIGHT or newX < 0: 
            self.ballDirection[0] *= -1 
        if newY >= WIDTH or newY < 0: 
            self.ballDirection[1] *= -1         
    
        self.grid[self.ballPos[0]][self.ballPos[1]] = "   "
        print self.ballPos
        self.ballPos[0] = self.ballPos[0] + self.ballDirection[0]
        self.ballPos[1] = self.ballPos[1] + self.ballDirection[1]
        print self.ballPos
        print "x"
        self.grid[self.ballPos[0]][self.ballPos[1]] = " O "
        self.createWidgets()            

        self.master.after(1000, self.moveBall)
    def movePlatform(self,event):
        move = 1
        if event.keysym == "Left":
            move = -1

        if self.selectedPos + move < 0 or self.selectedPos + move > 20:
            return False            
        self.grid[len(self.grid)-1][self.selectedPos] = "   "
        self.selectedPos += move
        self.grid[len(self.grid)-1][self.selectedPos] = "---"
        self.createWidgets()
    def updateGridAsText(self):
        self.gridAsText=""
        for row in self.grid:
            self.gridAsText += "".join(row) + "\n"
    def createWidgets(self):        
        self.updateGridAsText()
        self.game = Label(self, text=self.gridAsText, font='TkFixedFont', borderwidth=4, relief="groove")
        self.game.grid(row=1, column=1)
    def swapShowMoves(self):
        self.showMoves = not self.showMoves
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        bricks =  [["[_]"] * WIDTH for i in  range(BRICKHEIGHT)]
        space = [["   "] * WIDTH for i in  range(HEIGHT-BRICKHEIGHT-1)]
        platform = [(["   "] * (WIDTH/2)) + ["---"] + (["   "] * (WIDTH/2))]
        self.grid = bricks + space + platform 
        self.grid[HEIGHT/2] = (["   "] * (WIDTH/2)) + [" O "] + (["   "] * (WIDTH/2))
        self.bind("<Left>", self.movePlatform)
        self.bind("<Right>", self.movePlatform)
        self.focus_set()
        self.gridAsText=""
        self.createWidgets()
        self.selectedPos = 10
        self.ballPos = [HEIGHT/2, WIDTH/2]
        self.ballDirection = [1, 1]
        self.moveBall()
        

        
        


if __name__ == "__main__":
    root = Tk()   
    root.geometry="2000x1500"
    app = Application(master=root)
    app.mainloop()
    root.destroy()
