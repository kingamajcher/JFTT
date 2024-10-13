from functions import *
from Automaton import Automaton

# builds a DFA for given pattern and alphabet
def build_dfa(pattern, alphabet):
    dfa = Automaton()
    pattern_len = len(pattern)

    for idx in range(pattern_len + 1):
        dfa.add_state(idx)

    dfa.set_starting_state(0)

    dfa.add_accepting_state(pattern_len)

    # adds transitions for each state and each character in the alphabet
    for idx in range(pattern_len + 1):
        for char in alphabet:
            next_state = compute_suffix_function(pattern, pattern[:idx] + char)
            dfa.add_transition(idx, char, next_state)

    return dfa

# uses the DFA build from the pattern to find matches in the text
def automaton_match(pattern, text):

    alphabet = build_alphabet(pattern, text)

    dfa = build_dfa(pattern, alphabet)

    current_state = dfa.starting_state
    count = 0

    for i, char in enumerate(text):
        try:
            current_state = dfa.get_next_state(current_state, char)
        except ValueError:
            current_state = dfa.starting_state
            continue

        if dfa.is_accepting_state(current_state):
            position = i - len(pattern) + 1
            print(f"Pattern found at position {position}")
            count += 1

    return count