from Vec import Vector
from math import sqrt

class Car:
    def __init__(self):
        self.position = [120,720]
        self.carVector = Vector()
        self.heading = self.carVector.heading
   
    def move(self, action, goalPos):
        self.carVector.changeVector(action)
        xVector, yVector = self.carVector.getVector()
        self.heading = self.carVector.heading
        xPos, yPos = self.position
        xPos += xVector
        yPos += yVector
        self.position = [int(xPos),int(yPos)]
        if self.position == goalPos:
            return 1
        else:
            return 0
    
    def disToCar(self, i, j, xIndex, yIndex):
        return sqrt((i*40-xIndex*40)**2+(j*40-yIndex*40)**2)

    def chkCollision(self, mapList):
        xIndex = self.position[0]//40
        yIndex = self.position[1]//40

        for i in range(21):
            for j in range(21):
                if mapList[i][j] == 1:
                    if self.disToCar(i, j, xIndex, yIndex) <= 40:
                        return 1
        
        return 0