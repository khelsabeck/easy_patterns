# easy_patterns
Demonstrator for teaching design patterns in Python

__GOAL:__
This is a simple repo for showing how to use certain design patterns in Python. The intent is to use software best practices and show an easy to copy demostration of the finiste state machine (FSM) pattern using a simulation of a car interacting with a traffic light. 

__ISSUE1--Finite State Machines (big scary phrase):__
Finite state machines (FSMs) help programmers get away from the nested conditional logic of stacked if/else blocks and switch statements, which tend to turn into creeping piles of 'spaghetti code'. The logic always seems easy when 'in the code', but often becomes burdensome and overcomplicated in hindsight (ie: when trying to change or fix something some time after writing it). FSMs deal with this by giving each 'state' responsibility for the logic of when and how to change state, and delegating the state-change to a machine encapsulating the states. As a simple example, if there is a videogame with an NPC, the NPC's aggression (aggro) will likely be managed by dropping an FSM into it. The FSM may change based on alliances/etc, but the FSM will manage the states (AttackingState, RetreatingState, NeutralState, etc).

__Traffic Light (Super Easy FSM Demo):__
There are three states for a given traffic light: red light (stop); yellow light (slow down); and green light (go already). This beautiful ASCII diagram illustrates the states and their transitions: 
                _____'change'_____
               |      |    |      |
               |Green |--> |Yellow|
               |______|    |______|
                    ^           |
                    |           | 'change'
                    |       ____V__  
                    |______|       |
               'change'    |  Red  | 
                           |_______|
__Car FSM:__
The car FSM corresponds to a car, and its three states--braking, driving, and coasting--are the three states for a driver
responding to the states excpeted in a traffic light. In order to keep this simple, the car accepts the traffic light as 
an argument and accesses its state attribute directly. There are better ways to do this for big projects, but for now,
this repo is to serve as a teaching tool. One FSM-based object (car) with a simple FSM is responding directly to the state changes in another (trafficlight).

                ________    Green    ________
               |        |   Light   |        |
               |Braking |-------->  |Driving |
               |________|           |________|
                    ^                  |
                    |                  | Yellow 
          Red       |       ___________V Light
          Light     |______|            |
                           |  Coasting  |
                           |____________|