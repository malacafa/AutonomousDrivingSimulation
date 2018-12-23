import pygame
from DrawMap import DrawMap
from Car import Car
from math import sin,cos

class Simulation:
    def __init__(self):
        self.window = pygame.display.set_mode((840,840))
        pygame.display.set_caption("Autonomous Driving Simulation")
        self.fps = pygame.time.Clock()
        self.car = Car()
        self.drawmap = DrawMap()
        self.END = False
        self.drawmap.setMap()
        pygame.font.init() 
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
    
    def calcEndPoint(self):
        endX = int(self.car.position[0] - 100*sin(self.car.heading))
        endY = int(self.car.position[1] - 100*cos(self.car.heading))
        return [endX, endY]
        
    def run(self):
        while self.END != True:
            action = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.END = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        action = 3
                    if event.key == pygame.K_UP:
                        action = 0
                    if event.key == pygame.K_LEFT:
                        action = 2
                    if event.key == pygame.K_DOWN:
                        action = 1

            if self.car.move(action,[760, 120]) == 1:
                self.END = True
            
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
                self.END = True

            textState = self.myfont.render('heading:%.2f Xpos:%d Ypos:%d'%(self.car.heading,self.car.position[0],self.car.position[1]), False, (255, 255, 255))
            textState2 = self.myfont.render('XVec:%.2f YVec:%.2f'%(self.car.carVector.xVector,self.car.carVector.yVector), False, (255, 255, 255))
            self.window.blit(textState,(250,700))
            self.window.blit(textState2,(250,730))
            pygame.display.flip()
            self.fps.tick(10)

if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()            
