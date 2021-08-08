import pytest
from src.trafficlight_statemachine import State, Green, Red, Yellow, ErrorState, TrafficLight

def test_base_state():
    '''This should test that the base class is abstract and trying to instantiate it yields an error with known message.'''
    with pytest.raises(Exception) as exc_info:
        state = State()  #   This should raise an exception
    exception_raised = exc_info.value
    assert type(TypeError()) == type(exception_raised)
    assert "Can't instantiate abstract class State with abstract methods on_event" in str(exc_info.__dict__)

def test_red_state_type():
    '''This tests the red state. Expectation: It should be a State--Red type.'''
    state = Red()
    assert type(Red()) == type(state)

def test_yellow_state_type():
    '''This tests the red state. Expectation: It should be a State--Yellow type.'''
    state = Yellow()
    assert type(Yellow()) == type(state)

def test_green_state_type():
    '''This tests the red state. Expectation: It should be a State--Green type.'''
    state = Green()
    assert type(Green()) == type(state)

def test_machine_init():
    '''This tests that the machine initializes correctly and has the right type'''
    machine = TrafficLight()
    assert type(TrafficLight()) == type(machine) 
    assert type(Red()) == type(machine.state)

def test_transitions():
    '''This tests the state machine transitions correctly.'''
    machine = TrafficLight()
    assert type(TrafficLight()) == type(machine) 
    assert type(Red()) == type(machine.state) 
    machine.on_event("change")
    assert type(Green()) == type(machine.state)         # red to green
    machine.on_event("change")
    assert type(Yellow()) == type(machine.state)        # green to yellow
    machine.on_event("change")
    assert type(Red()) == type(machine.state)           # yellow back to red
    machine.on_event("change")
    assert type(Green()) == type(machine.state)         # red to green
    machine.on_event("change")
    assert type(Yellow()) == type(machine.state)        # green to yellow
    machine.on_event("change")
    assert type(Red()) == type(machine.state)           # yellow back to red
    machine.on_event("invalid data")
    assert type(ErrorState()) == type(machine.state)    # proper error state transition


