import time, threading
from transitions import Machine

class TrafficLight(object):
  states = ["red", "amber-red", "amber-green", "green"]

  def __init__(self, name, initial_state="red"):

    self.name = name

    # Initialize the state machine
    self.machine = Machine(model=self, states=TrafficLight.states, initial=initial_state)

    self.machine.add_transition(trigger='change', source='red', dest='amber-green')
    self.machine.add_transition(trigger='change', source='amber-green', dest='green')
    self.machine.add_transition(trigger='change', source='green', dest='amber-red')
    self.machine.add_transition(trigger='change', source='amber-red', dest='red')

  def __repr__(self):
    current_state = self.state
    return "{} is {}".format(self.name, "amber" if current_state.startswith("amber") else current_state) 

states = [TrafficLight("North", "red"), TrafficLight("East", "green"),
TrafficLight("South", "red"), TrafficLight("West", "green")]

current_time_in_simulation = 0

def change_state(current_states):
  for state in current_states:
    state.change()

def foo(current_states, current_time):
    print(current_time)
    current_time += 1
    print(time.ctime())
    # First, we change every 10 seconds from Red
    if current_states[0].state in ["green", "red"] and current_time == 10:
      change_state(current_states)
      current_time = 0
    else:
      # We change amber if 3 seconds passed
      if current_states[0].state in ["amber-red", "amber-green"] and current_time == 3:
        change_state(current_states)
        current_time = 0
    print(states)
    threading.Timer(1, foo, [current_states, current_time]).start()

foo(states, current_time_in_simulation)