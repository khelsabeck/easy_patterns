import pytest
from src.car_statemachine import State, Braking, Driving, Coasting, Car_ErrorState, Car
from src.trafficlight_statemachine import State, Green, Red, Yellow, ErrorState, TrafficLight

def test_base_state_car():
    '''This should test that the base class is abstract and trying to instantiate it yields an error with known message.'''
    with pytest.raises(Exception) as exc_info:
        state = State()  #   This should raise an exception
    exception_raised = exc_info.value
    assert type(TypeError()) == type(exception_raised)
    assert "Can't instantiate abstract class State with abstract methods on_event" in str(exc_info.__dict__)

def test_base_state_abstractmethod_car():
    '''This should test that the base class method.'''
    with pytest.raises(Exception) as exc_info:
        class TestState(State):
            pass
        state = TestState()  #   This should raise an exception because there is no implementation of the on_event method
    exception_raised = exc_info.value
    assert type(TypeError()) == type(exception_raised)
    assert "Can't instantiate abstract class TestState with abstract methods on_event" in str(exc_info.__dict__)

def test_braking_state_type():
    '''This tests the braking state. Expectation: It should be a State--Braking type with str "Braking.'''
    state = Braking()
    assert type(Braking()) == type(state)
    assert "Braking" == str(state)

def test_driving_state_type():
    '''This tests the driving state. Expectation: It should be a State--Driving type and its str should be "Driving".'''
    state = Driving()
    assert type(Driving()) == type(state)
    assert "Driving" == str(state)

def test_coasting_state_type():
    '''This tests the coasting state. Expectation: It should be a State--Coasting type with an str value of "Coasting".'''
    state = Coasting()
    assert type(Coasting()) == type(state)
    assert "Coasting" == str(state)

def test_error_state_type():
    '''This tests the error state. Expectation: It should be a State--Car_ErrorState type and the str should be "Car_ErrorState.'''
    state = Car_ErrorState()
    assert type(Car_ErrorState()) == type(state)
    assert "Car_ErrorState" == str(state)

def test_car_init():
    '''This tests that the machine initializes correctly and has the right type'''
    car = Car()
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)

def test_machine_startstates():
    '''This tests initialization and starting states of the traffic light and car'''
    car = Car()
    light = TrafficLight()
    assert type(TrafficLight()) == type(light) 
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)

def test_transition_braking_toDriving():
    '''This tests transitions from braking to driving.'''
    car = Car()
    light = TrafficLight()
    assert type(TrafficLight()) == type(light) 
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Driving()) == type(car.state)
    assert type(Green()) == type(light.state)

def test_transition_braking_to_error():
    '''This tests transitions from braking to error.'''
    car = Car()
    light = TrafficLight()
    assert type(TrafficLight()) == type(light) 
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)
    light.on_event("bad data")
    car.on_event(light)
    assert type(ErrorState()) == type(light.state)
    assert type(Car_ErrorState()) == type(car.state)

def test_transition_driving_to_coasting():
    '''This tests transitions from driving to coasting.'''
    car = Car()
    light = TrafficLight()
    assert type(TrafficLight()) == type(light) 
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Driving()) == type(car.state)
    assert type(Green()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Coasting()) == type(car.state)
    assert type(Yellow()) == type(light.state)    

def test_transition_driving_to_error():
    '''This tests transitions from driving to coasting.'''
    car = Car()
    light = TrafficLight()
    assert type(TrafficLight()) == type(light) 
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Driving()) == type(car.state)
    assert type(Green()) == type(light.state)
    light.on_event("bad data")
    car.on_event(light)
    assert type(ErrorState()) == type(light.state)   
    assert type(Car_ErrorState()) == type(car.state)

def test_transition_coasting_to_braking():
    '''This tests transitions from coasting to braking.'''
    car = Car()
    light = TrafficLight()
    assert type(TrafficLight()) == type(light) 
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Driving()) == type(car.state)
    assert type(Green()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Coasting()) == type(car.state)
    assert type(Yellow()) == type(light.state)        
    light.on_event("change")
    car.on_event(light)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)            

def test_transition_coasting_to_error():
    '''This tests transitions from coasting to error.'''
    car = Car()
    light = TrafficLight()
    assert type(TrafficLight()) == type(light) 
    assert type(Car()) == type(car)
    assert type(Braking()) == type(car.state)
    assert type(Red()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Driving()) == type(car.state)
    assert type(Green()) == type(light.state)
    light.on_event("change")
    car.on_event(light)
    assert type(Coasting()) == type(car.state)
    assert type(Yellow()) == type(light.state)        
    light.on_event("bad data")
    car.on_event(light)
    assert type(Car_ErrorState()) == type(car.state)
    assert type(ErrorState()) == type(light.state) 