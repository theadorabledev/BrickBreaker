from Tkinter import *
import time
HEIGHT = 11
WIDTH = 64
BRICKHEIGHT = 2
PLATFORMLENGTH = 3
SPEED = 4
class Application(Frame): 
    def collisionHandle(self, newX, newY):
        if self.grid[newY][newX] == "-":
            self.ballDirection[1] *= -1 
        if self.grid[newY][newX] == "[":
            self.ballDirection[1] *= -1 
            self.grid[newY][newX] = " "
            self.grid[newY][newX + 1] = " "
            self.grid[newY][newX + 2] = " "
            self.playerPoints += 1
        if self.grid[newY][newX] == "_":
            self.ballDirection[1] *= -1 
            self.grid[newY][newX - 1] = " "
            self.grid[newY][newX] = " "
            self.grid[newY][newX + 1] = " "                    
        if self.grid[newY][newX] == "]":
            self.ballDirection[1] *= -1    
            self.grid[newY][newX - 2] = " "
            self.grid[newY][newX - 1] = " "
            self.grid[newY][newX] = " "           
    def moveBall(self):
        self.grid[self.ballPos[1]][self.ballPos[0]] = "O"
        newX = self.ballPos[0] + (self.ballDirection[0] * self.ballSlope[0]) 
        newY = self.ballPos[1] + (self.ballDirection[1] * self.ballSlope[1])
        print newY, HEIGHT
        if newX >= WIDTH or newX <= 0: 
            self.ballDirection[0] *= -1 
        if newY <= 0: 
            self.ballDirection[1] *= -1       
        try:
            if newY  >= (HEIGHT):
                self.playerLives -= 1
                self.grid[self.platformPos[1]][self.platformPos[0] - 1] = " "
                self.grid[self.platformPos[1]][self.platformPos[0]] = " "
                self.grid[self.platformPos[1]][self.platformPos[0] + 1] = " "
                self.platformPos = self.origPlatformPos[:]
                self.grid[self.platformPos[1]][self.platformPos[0] - 1] = "-"
                self.grid[self.platformPos[1]][self.platformPos[0]] = "-"
                self.grid[self.platformPos[1]][self.platformPos[0] + 1] = "-" 
                
                self.grid[self.ballPos[1]][self.ballPos[0]] = " "
                self.ballPos = self.origBallPos[:]
                self.grid[self.ballPos[1]][self.ballPos[0]] = "O"
                               
        except IndexError:
            pass
        
        else:
            try:
                if self.grid[newY][newX] != " ":
                    self.collisionHandle(newX, newY)
            except IndexError:
                pass
            self.grid[self.ballPos[1]][self.ballPos[0]] = " "
           # print "orig", str(self.ballPos)
            #print self.platformPos[0]
            self.ballPos[0] = self.ballPos[0] + (self.ballDirection[0] * self.ballSlope[0]) 
            self.ballPos[1] = self.ballPos[1] + (self.ballDirection[1] * self.ballSlope[1])
            print "new", str(self.ballPos)
            print "x"
            self.grid[self.ballPos[1]][self.ballPos[0]] = "O"
            self.createWidgets()            
        if self.playerLives > 0:
            self.master.after(1000/SPEED, self.moveBall)
        else:
            self.game["text"] = "GAME OVER!"
            self.game["bg"] = "red"
    def changeBallDirection(self):
        pass
    def movePlatform(self,event):
        move = 1
        if event.keysym == "Left":
            move = -1

        if self.platformPos[0] - 1 + move < 0 or self.platformPos[0] + 1 + move > WIDTH:
            return False            
        self.grid[self.platformPos[1]][self.platformPos[0] - 1] = " "
        self.grid[self.platformPos[1]][self.platformPos[0]] = " "
        self.grid[self.platformPos[1]][self.platformPos[0] + 1] = " "
        self.platformPos[0] += move
        self.grid[self.platformPos[1]][self.platformPos[0] - 1] = "-"
        self.grid[self.platformPos[1]][self.platformPos[0]] = "-"
        self.grid[self.platformPos[1]][self.platformPos[0] + 1] = "-"
        self.createWidgets()
    def updateGridAsText(self):
        self.gridAsText=""
        for row in self.grid:
            self.gridAsText += "".join(row) + "\n"
    def createWidgets(self):        
        self.updateGridAsText()
        self.playerInfo = "Lives : " + str(self.playerLives) + "\n Points : " + str(self.playerPoints)
        self.game = Label(self, text=self.gridAsText, font='TkFixedFont', borderwidth=4, relief="groove")
        self.game.grid(row=1, column=1)
        self.playerInfo = Label(self, text=self.playerInfo, font='TkFixedFont', borderwidth=4, relief="groove")
        self.playerInfo.grid(row=2, column=1)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        bricks =  [["[","_","]"] * (WIDTH/3) for i in  range(BRICKHEIGHT)]
        space = [[" "] * WIDTH for i in  range(HEIGHT-BRICKHEIGHT-2)]
        platform = [([" "] * ((WIDTH/2))) + ["-"] * PLATFORMLENGTH + ([" "] * ((WIDTH/2) - 2))]
        abyss = [[" "] * WIDTH ]
        self.grid = bricks + space + platform + abyss
        self.grid[HEIGHT/2] = ([" "] * (WIDTH/2)) + ["O"] + ([" "] * (WIDTH/2))
        
        self.bind("<Left>", self.movePlatform)
        self.bind("<Right>", self.movePlatform)
        self.focus_set()
        self.gridAsText=""
        self.platformPos = [(WIDTH/2) + 1, len(self.grid)-2]
        self.origPlatformPos = [(WIDTH/2) + 1, len(self.grid)-2]
        self.ballPos = [WIDTH/2, HEIGHT/2]
        self.origBallPos = [WIDTH/2, HEIGHT/2]
        self.playerLives = 3
        self.playerPoints = 0
        self.ballDirection = [1, 1]
        self.ballSlope = [1,1]#run, rise
        self.createWidgets()
        
        self.moveBall()
        

        
        


if __name__ == "__main__":
    root = Tk()   
    root.geometry="2000x1500"
    app = Application(master=root)
    app.mainloop()
    root.destroy()
