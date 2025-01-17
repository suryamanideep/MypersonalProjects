from cell import states
import pygame
import drawfn

ACTION_EAST=0
ACTION_SOUTH=1
ACTION_WEST=2
ACTION_NORTH=3


TRANSITION_SUCCEED=0.8 #The probability that by taking action A, it moves to the expected destination state S'. Here the state S' represents the new state that the action A aims to move to.
TRANSITION_FAIL=0.2 #The probability that by taking action A, it moves to an unexpected destination state S'. For example, by taking action East, you may moves to the neighboring direction North or South. So the probability of going to North or South is 0.1. We assume the two directions evenly split the value of TRANSITION_FAIL 0.2
GAMMA=0.9 #the discount factor
ACTION_REWARD=0.1 #The instantaneous for taking each action (we assume the four actions (N/E/W/S) has the same reward)
CONVERGENCE=0.000000001 #The threshold for convergence to determine a stop sign
cur_convergence=100

#####Implement the below functions ############################
def compute_s_prime(s, a):
    row, col = s.location
    s_prime = s

    if (col == 0 and a == 3) or (col == 2 and a == 1) or (row == 0 and a == 2) or (row == 3 and a == 0):
        # If the action hits the edge, it remains in the same state (bouncing back)
        s_prime = s
    elif a == 0:
        if col + 1 < 3:  # Check if the new column index is within bounds
            s_prime = states[col + 1][row]
    elif a == 1:
        if row + 1 < 4:  # Check if the new row index is within bounds
            s_prime = states[col][row + 1]
    elif a == 2:
        if col - 1 >= 0:  # Check if the new column index is within bounds
            s_prime = states[col - 1][row]
    elif a == 3:
        if row - 1 >= 0:  # Check if the new row index is within bounds
            s_prime = states[col][row - 1]

    if s_prime.location == (1, 1):
        # The next landing state can't be a blocked state; it bounces and lands on the sand
        s_prime = s

    return s_prime

def computeQValue(s, action):
    row, col = s.location
    s_prime = compute_s_prime(s, action)

    # If the next state is a blocked state, it bounces back to the current state (sand)
    if (s_prime.location == (1, 1)) or (s_prime.location == (3, 0)) or (s_prime.location == (3, 1)):
        s_prime = s

    q_value = ACTION_REWARD + GAMMA * (
        TRANSITION_SUCCEED * s_prime.state_value +
        TRANSITION_FAIL * (s.state_value if action == s.policy else s_prime.state_value)
    )

    return q_value

def initialize_state_values():
    for row in range(len(states)):
        for col in range(len(states[row])):
            states[row][col].state_value = 0.0

def valueIteration(max_iterations=100):
    global cur_convergence
    iteration_count = 0
    while iteration_count < max_iterations:
        cur_convergence = 0.0  # Reset convergence for each iteration
        initialize_state_values()
        for row in range(len(states)):
            for col in range(len(states[row])):
                cell = states[row][col]
                old_state_value = cell.state_value

                q_values = []  # Initialize a list to store Q-values for all actions
                for action in range(4):
                    q_value = computeQValue(cell, action)
                    q_values.append(q_value)  # Append the Q-value for each action

                cell.q_values = q_values  # Update the q_values list for the cell

                max_q_value = max(q_values)  # Find the maximum Q-value
                cell.state_value = max_q_value
                cur_convergence = max(cur_convergence, abs(old_state_value - max_q_value))

        if cur_convergence < CONVERGENCE:
            break

        iteration_count += 1
        #print(iteration_count, cur_convergence)

def policyEvaluation():
    while True:
        delta = 0.0
        for row in range(len(states)):
            for col in range(len(states[row])):
                cell = states[row][col]
                old_state_value = cell.state_value

                q_value = computeQValue(cell, cell.policy)
                cell.state_value = q_value

                delta = max(delta, abs(old_state_value - cell.state_value))
        print(f"delta = {delta}")
        if delta < CONVERGENCE:
            break

def policyImprovement():
    global states
    policy_stable = True

    for row in range(len(states)):
        for col in range(len(states[row])):
            cell = states[row][col]
            old_policy = cell.policy
            max_q_value = -float('inf')
            new_policy = None

            for action in range(4):  # 0: East, 1: South, 2: West, 3: North
                q_value = computeQValue(cell, action)
                if q_value is not None and q_value > max_q_value:
                    max_q_value = q_value
                    new_policy = action

            if new_policy is not None:
                cell.policy = new_policy

            if old_policy != new_policy:
                policy_stable = False

    return policy_stable

################################# Dont modify the code below ###########################
def policyIteration():
    drawfn.check2=True
    drawfn.radio1=False
    drawfn.radio2=True
    policies={}
    for s in states:
        for cell in s:
            policies[cell.location]=cell.policy
    #policies should be a dictionary with states[][].location as it's key and states[][].policy as value
    i=0
    while True:
        i+=1
        oldPolicy=policies.copy()
        policyEvaluation()
        policyImprovement()
        for s in states:
            for cell in s:
                if ((cell.location[0] == 1 and cell.location[1] == 1) or (cell.location[0] == 3 and cell.location[1] == 0) or  (cell.location[0] == 3 and cell.location[1] == 1)):
                    continue
                else:
                    policies[cell.location]=cell.policy

        drawfn.draw()
        pygame.time.delay(200)
        drawfn.screen.fill(pygame.Color(255,255,255),pygame.Rect(300,580,150,20))
        fnt = pygame.font.SysFont("Bahnschrift", 20)
        iterText = fnt.render("Iterations: "+str(i), 1, (0,0,0))
        drawfn.screen.blit(iterText, (300,580))
        pygame.display.update()
        
        if all(oldPolicy[key] == policies[key] for key in policies):
            print('Ideal Policy Obtained.')
            break
  
def onGo(idx):
        # global idx
        if(idx<=100 and cur_convergence>CONVERGENCE):
            valueIteration()
            drawfn.screen.fill(pygame.Color(255,255,255),pygame.Rect(300,580,150,20))
            fnt = pygame.font.SysFont("Bahnschrift", 20)
            iterText = fnt.render("Iterations: "+str(idx), 1, (0,0,0))
            drawfn.screen.blit(iterText, (300,580))
            return True
        else:
            return False
