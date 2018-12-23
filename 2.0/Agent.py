from keras.models import load_model, Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np
from random import random, randrange, sample

class DQN:
    def __init__(self, inputSize, outputSize, memorySize, learningRate, batchSize):
        self.inputSize = inputSize
        self.outputSize = outputSize
        self.memorySize = memorySize
        self.learningRate = learningRate
        self.batchSize = batchSize
        self.epsilon = 1
        self.trainStart = batchSize
        self.mainModel = self.makeModel()
        self.targetModel = self.makeModel()
        self.updateTargetModel()
        self.memory = []
        self.learnStart = 1000
    
    def updateTargetModel(self):
        self.targetModel.set_weights(self.mainModel.get_weights())
    
    def makeModel(self):
        model=Sequential()
        model.add(Dense(50, input_dim= self.inputSize, activation= 'relu')) # input layer
        model.add(Dense(50, activation='relu')) # hidden layer
        model.add(Dense(50, activation='relu')) # hidden layer
        model.add(Dense(self.outputSize)) # output layer
        model.compile(loss = "mean_squared_error", optimizer = Adam(lr = self.learningRate))
        return model
    
        def getAction(self,state):
        if random()<self.epsilon:
            action = randrange(self.outputSize)
            return action
        else:
            self.q_value = self.mainModel.predict(state.reshape(1, len(state)))
            return np.argmax(self.q_value[0])

    def getQvalue(self, reward, nextTarget, done):
        if done:
            return reward
        else:
            return reward + 0.99*np.amax(nextTarget)

    def saveData(self, state, action, reward, newState, done):
        if len(self.memory)>self.memorySize:
            self.memory.pop(0)
        self.memory.append((state, action, reward, newState, done))

    def trainModel(self):
        miniBatch = sample(self.memory, self.batchSize)
        X_batch = np.empty((0, self.inputSize), dtype=np.float64)
        Y_batch = np.empty((0, self.outputSize), dtype=np.float64)

        for i in range(self.batchSize):
            states = miniBatch[i][0]
            actions = miniBatch[i][1]
            rewards = miniBatch[i][2]
            nextStates = miniBatch[i][3]
            dones = miniBatch[i][4]

            q_value = self.mainModel.predict(states.reshape(1, len(states)))
            self.q_value = q_value

            nextTarget = self.targetModel.predict(nextStates.reshape(1, len(nextStates)))
            next_q_value = self.getQvalue(rewards, nextTarget, dones)

            X_batch = np.append(X_batch, np.array([states.copy()]), axis=0)
            Y_sample = q_value.copy()
            Y_sample[0][actions] = next_q_value
            Y_batch = np.append(Y_batch, np.array([Y_sample[0]]), axis=0)

            if dones:
                X_batch = np.append(X_batch, np.array([nextStates.copy()]), axis=0)
                Y_batch = np.append(Y_batch, np.array([[rewards]*self.outputSize]), axis=0)

        self.mainModel.fit(X_batch, Y_batch, batchSize=self.batchSize, epochs=1, verbose=0)

    def saveModel(self):
        self.mainModel.save('model.h5')

    def loadModel(self):
        self.mainModel = load_model('model.h5')
        self.targetModel = load_model('model.h5')
