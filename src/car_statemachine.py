# The states for the car--"driving, coasting, and braking"--correspond to the traffic light states green, yellow, and red
from abc import ABC, abstractmethod     # this is not absolutely necessary, but it helps enforce discipline making states
import typing                           # also not absolutely necessary, but typing gives clues re types
import time

class State(ABC):
    '''This is the base class for a state. Each state holds the logic of when to transition to the next.'''
    def __init__(self):
        pass

    @abstractmethod
    def on_event(self, trafficlight:object): 
        '''When it is necessary to switch, this takes the call_to_switch and directs the light to change states.'''
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

#------- These are the concrete states:------------------
class Braking(State):
    '''This represents a car braking for a red light. When the light turns green, it should change to Driving. Else error.'''
    def on_event(self, trafficlight): 
        if str(trafficlight.state) == "Green":
            return Driving()
        else:
            return Car_ErrorState()

class Driving(State):
    '''This represents a car driving on a green light. When the light turns yellow, it should change to Coasting. Else error.'''
    def on_event(self, trafficlight): 
        if str(trafficlight.state) == "Yellow":
            return Coasting()
        else:
            return Car_ErrorState()

class Coasting(State):
    '''This represents a car coasting for yellow light. When the light turns red, it should change to Braking. Else error.'''
    def on_event(self, trafficlight): 
        if str(trafficlight.state) == "Red":
            return Braking()
        else:
            return Car_ErrorState()

class Car_ErrorState(State):
    def on_event(self, trafficlight): 
        return Braking()                # we should default to braking when the light is broken

#--------- The actual state machine itself:-----------------
class Car:             #   This is the actual Finite State Machine
    '''This is the state machine itself and this object can be called upon downstream to represent a car that
    switches to different states when the light does.

    Call this in client code as such:
    from trafficlight_statemachine import Car
    car = Car()
    car.on_event(trafficlight)'''
    def __init__(self):
        self.state = Braking() #  starting state is now set as braking

    def on_event(self, trafficlight):
        self.state = self.state.on_event(trafficlight)