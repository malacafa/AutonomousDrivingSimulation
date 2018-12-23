from Simul import Simulation

agent = DQN()
simulation = Simulation()

for episodes in range(1000):
    done = False
    state = simulation.reset()
    for steps in range(1000):
        
        action = agent.getAction(state)
        newState, reward, done = simulation.step()
        agent.saveData(state, action, reward, newState, done)
        state = newState

        if agent.epsilon > 0.05:
            agent.epsilon *= 0.9999

        if done:
            agent.updateTargetModel()
            break
    
    if episodes%10 == 0:
        agent.saveModel()
