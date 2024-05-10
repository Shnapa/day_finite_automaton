""" My day during Easter break """

import random


class State:
    def __init__(self, name):
        self.name = name


class FiniteStateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.event = [
            "friend call",
            "headache",
            "ride a bike",
            "weak muscle",
        ]
        self.choice = ["do IT homework", "read a book", "study calculus", "study descrete"]

    def add_state(self, state):
        self.states[state.name] = state

    def set_current_state(self, state_name):
        self.current_state = self.states[state_name]

    def run(self, hours):
        hunger = 0
        stress = 0
        hour = 0
        dirtiness = 0
        while hour < hours:
            print(f"{hour + 1}:00", self.current_state.name)
            print("Hunger -", hunger, ";", "Stress level -", stress)
            if self.current_state.name == "Sleep":
                if hour == 6:
                    stress = 0
                    print("\nHello world!")
                    self.set_current_state("Wake up")
            elif hour == 21:
                stress = 0
                print("\nIt's late. Time to sleep!")
                self.set_current_state("Sleep")
            elif hour == 8:
                stress = 0
                print("\nIt's high time to start studying!")
                self.set_current_state("Study")
                stress += 1
            elif hour % 3 == 0:
                random_event = random.choice(self.event)
                if random_event == "friend call":
                    print("\nMy friend asked me for a walk...")
                    self.set_current_state("Walk")
                    stress = 0
                elif random_event == "headache":
                    print("\nI have a headache, I need to take a rest...")
                    self.set_current_state("Free time")
                    stress = 0
                elif random_event == "ride a bike":
                    print("\nWonderful weather! I should ride a bike...")
                    self.set_current_state("Ride a bike")
                elif random_event == "weak muscle":
                    print("\nOh no! My muscles are weak, to the gym!")
                    stress = 0
                    self.set_current_state("Gym")
            elif hunger >= 5 and random.random() < 0.95:
                hunger = 0
                print("\nI'm really hungry...")
                self.set_current_state("Eat")
            elif random.random() < 0.9 and dirtiness >= 20:
                dirtiness = 0
                print("\nAm I that stinky?")
                self.set_current_state("Shower")
            elif stress >= 9:
                stress = 0
                print("\nI'm really stressed. It's time to crochet...")
                self.set_current_state("Crochet")
            else:
                stress += 1
                random_event = random.choice(self.choice)
                print(f"\nI need to {random_event}...")
                self.set_current_state("Study")

            hour += 1
            hunger += 1
            dirtiness += 1
            print()


sleep = State("Sleep")
wake_up = State("Wake up")
eat = State("Eat")
study = State("Study")
free_time = State("Free time")
shower = State("Shower")
walk = State("Walk")
gym = State("Gym")
crochet = State("Crochet")
bike = State("Ride a bike")

fsm = FiniteStateMachine()

for state in [sleep, wake_up, eat, study, free_time, shower, walk, gym, crochet, bike]:
    fsm.add_state(state)

fsm.set_current_state("Sleep")

fsm.run(24)