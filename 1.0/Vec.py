from math import cos,sin,pi,sqrt

class Vector:
    def __init__(self):
        self.xVector = 0
        self.yVector = -5
        self.heading = 0 # 0 ~ 2pi

    def changeVector(self, action):
        if action == 0: # 0: go forward
            self.heading = self.heading # heading is same
            self.xVector = self.xVector # xVector is same
            self.yVector = self.yVector # yVector is same

        if action == 1: # 1: go backward
            self.heading = self.heading + pi
            if self.heading > 2*pi:
                self.heading = self.heading - 2*pi
            self.xVector = -1*self.xVector # xVector reverse
            self.yVector = -1*self.yVector # yVector reverse

        if action == 2: # 2: turn left a bit 
            self.heading += pi/20 # dtheta is pi/20
            if self.heading < 0:
                self.heading = 2*pi-abs(self.heading)
            
            vec = -1*sqrt(self.xVector**2+self.yVector**2)
            self.xVector = vec*sin(self.heading)
            self.yVector = vec*cos(self.heading)

        if action == 3: # 3: turn right a bit
            self.heading -= pi/20
            if self.heading > 2*pi:
                self.heading = self.heading - 2*pi

            vec = -1*sqrt(self.xVector**2+self.yVector**2)
            self.xVector = vec*sin(self.heading)
            self.yVector = vec*cos(self.heading)

    def getVector(self):
        return [self.xVector, self.yVector]
