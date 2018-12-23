from Vec import Vector
from math import sqrt

class Car:
    def __init__(self):
        self.position = [120, 720]
        self.carVector = Vector()
        self.heading = self.carVector.heading
        self.sensor = [] 
   
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
        
    def getSensor(self):
        return self.sensor
    
    def disToCar(self, i, j, xIndex, yIndex):
        return sqrt((i*40-xIndex*40)**2+(j*40-yIndex*40)**2)

    def chkGoal(self):
        if self.position == [720, 120]:
            return 1
        return 0

    def chkCollision(self, mapList):
        xIndex = self.position[0]//40
        yIndex = self.position[1]//40
        self.sensor = []

        for i in range(21):
            for j in range(21):
                distToWall = self.disToCar(i, j, xIndex, yIndex)
                if mapList[i][j] == 1:
                    if distToWall <= 40:
                        return 1
        
        return 0
    