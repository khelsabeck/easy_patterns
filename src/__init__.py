"""
This package has the module crosswalk, with the principal function 'simulate_crosswalk()' for running two statemachines (Car and TrafficLight). 
It also has the state machines themselves and their respective states Car: [ CarState, Braking, Driving, Coasting, Car_ErrorState ], 
and TrafficLight: [ State, Red, Green, Yellow, ErrorState ]. Feel free to poke around in the source code or fork it if you want a basic state
machine for your own project.
"""
from src.car_statemachine import Car, CarState, Braking, Driving, Coasting, Car_ErrorState
from src.trafficlight_statemachine import TrafficLight, State, Red, Green, Yellow, ErrorState
from src.crosswalk import simulate_crosswalk
