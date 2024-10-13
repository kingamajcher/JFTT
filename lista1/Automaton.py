class Automaton:
    # initializes an automaton
    def __init__(self):
        self.states = set()
        self.starting_state = None
        self.transition_func = {}
        self.accepting_states = set()

    # adds a new state to the set of states in the automaton
    def add_state(self, state):
        self.states.add(state)

    # sets the starting state of an automaton
    def set_starting_state(self, state):
        if state not in self.states:
            raise ValueError(f"State {state} does not exist")
        self.starting_state = state

    # returns the next state of an automaton based of current state and input char
    def get_next_state(self, state, input_char):
        if state not in self.transition_func or input_char not in self.transition_func[state]:
            raise ValueError(f"No transition defined from state {state} on input {input_char}")
        return self.transition_func[state][input_char]

    # returns True when given state is an accepting state, otherwise False 
    def is_accepting_state(self, state):
        return state in self.accepting_states

    # add the given state to the set of accepting states
    def add_accepting_state(self, state):
        if state not in self.states:
            raise ValueError(f"State {state} does not exist")
        self.accepting_states.add(state)

    # adds a transition from 'from_state' to 'to_state' based on 'input_char'
    def add_transition(self, from_state, input_char, to_state):
        if from_state not in self.states or to_state not in self.states:
            raise ValueError(f"From state {from_state} or to state {to_state} does not exist")
        if from_state not in self.transition_func:
            self.transition_func[from_state] = {}
        self.transition_func[from_state][input_char] = to_state

    # simulates the automaton processing a string of input characters, returns True or False based on wheter the final state is an accepting state
    def process_input(self, input_string):
        state = self.starting_state
        for char in input_string:
            if state not in self.transition_func or char not in self.transition_func[state]:
                return False
            state = self.transition_func[state][char]
        return self.is_accepting_state(state)
