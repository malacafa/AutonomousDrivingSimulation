import pygame
from pygame.locals import *
from DrawMap import DrawMap
from Car import Car
from math import sin,cos

class Simulation:
    def __init__(self):
        pygame.display.set_caption("Autonomous Driving Simulation")
        pygame.font.init() 
        self.window = pygame.display.set_mode((840,840))
        self.fps = pygame.time.Clock()
        self.car = Car()
        self.drawmap = DrawMap()
        self.END = False
        self.drawmap.setMap()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.goalPos = [760, 120]
    
    def reset(self):
        self.car.position = [120,720]
        self.car.heading = 0

        self.car.carVector.heading = 0
        self.car.carVector.xVector = 0
        self.car.carVector.yVector = -5

    def calcEndPoint(self):
        endX = int(self.car.position[0] - 100*sin(self.car.heading))
        endY = int(self.car.position[1] - 100*cos(self.car.heading))
        return [endX, endY]
    
    def getState(self):
        state = []
        state.append(self.car.heading)
        sensor = self.car.getSensor()
        return state, done
    
    def getReward(self):
        reward = 0

        if self.car.position == self.goalPos:
            reward += 1000
        
        

        return reward
        
    def step(self,action):
        done = False

        if self.car.move(action,self.goalPos) == 1:
            done = True
        
        newState = self.getState()
        reward = self.getReward()
            
        self.window.fill(pygame.Color(225, 225, 225))
        pygame.draw.circle(self.window, pygame.Color(0, 0, 255), self.car.position, 40)
        endPoint = self.calcEndPoint()
        pygame.draw.line(self.window, pygame.Color(255,0,0), self.car.position, endPoint, 1)
        maplist = self.drawmap.getMap()
        for i in range(21):
            for j in range(21):
                if maplist[i][j] == 1:
                    pygame.draw.rect(self.window, pygame.Color(0, 0, 0), pygame.Rect(i*40, j*40, 40, 40))

        if self.car.chkCollision(maplist) == 1:
            reward -= 1000
            done = True

        textState = self.myfont.render('heading:%f Xpos:%d Ypos:%d XVec:%.2f YVec:%.2f'%(self.car.heading,self.car.position[0],self.car.position[1],self.car.carVector.xVector,self.car.carVector.yVector), False, (255, 255, 255))
        self.window.blit(textState,(250,700))
        pygame.display.flip()
        self.fps.tick(10)

        return newState, reward, done      