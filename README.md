# easy_patterns
Demonstrator for teaching design patterns in Python

__GOAL:__
This is a simple repo for showing how to use certain design patterns in 
Python. The intent is to use software best practices and show an easy to
copy demostration of the finiste state machine (FSM) pattern using a 
simulation of a traffic light. 

__ISSUE1--Finite State Machines (big scary phrase):__
Finite state machines (FSMs) help programmers get away from the nested 
conditional logic of stacked if/else blocks and switch statements, which
tend to turn into creeping piles of 'spaghetti code'. The logic always seems
easy when 'in the code', but often becomes burdensome and overcomplicated
in hindsight (ie: when trying to change or fix something weeks or months
after writing it). FSMs deal with this by giving each 'state' the ability to
figure out when it should change and what to do about it.

__Traffic Light (Super Easy FSM Demo):__
There are three states for a given traffic light: red light (stop); 
yellow light (slow down); and green light (go already). The simple sequence
of transitions is: 

                ______      ______
               |      |    |      |
               |Green |--> |Yellow|
               |______|    |______|
                    ^           |
                    |           |
                    |       ____V__  
                    |______|       |
                           |  Red  |
                           |_______|
