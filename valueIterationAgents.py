import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0




    "*** YOUR CODE HERE ***"
    for i in range(len(mdp.getStates())):
        self.values[mdp.getStates()[i]] = 0.0

    values_tmp = self.values


    #exclusion = ['TERMINAL_STATE', (3, 2), (3, 1)]
    exclusion = []
    for it in range(self.iterations):
        for i in range(len(mdp.getStates())):
            if mdp.getStates()[i] in exclusion:
                continue
            actions = mdp.getPossibleActions(mdp.getStates()[i])
            V_s = []
            for j in range(len(actions)):
                summation = 0.0
                next_states = mdp.getTransitionStatesAndProbs(mdp.getStates()[i], actions[j])

                for ns in next_states:
                    summation += ns[1] * (mdp.getReward(mdp.getStates()[i], actions[j], ns[0]) + self.discount * self.values[ns[0]])
                    if mdp.getReward(mdp.getStates()[i], actions[j], ns[0]) != 0.0:
                        print "hererer"
                V_s.append(summation)




            #assert(len(V_s) > 0)
            maximum = V_s[0]
            for k in range(len(V_s)):
                maximum = max(maximum, V_s[k])
            values_tmp[mdp.getStates()[i]] = maximum
        self.values = values_tmp



    "*** YOUR CODE HERE -END- ***"




    
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  
