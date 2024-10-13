from functions import *
from Automaton import Automaton

def build_dfa(pattern, alphabet):
    """
    Build a DFA (Deterministic Finite Automaton) for the given pattern and alphabet.
    """
    dfa = Automaton()
    pattern_len = len(pattern)

    # Add states for the pattern length + 1 (to include the starting and accepting states)
    for idx in range(pattern_len + 1):
        dfa.add_state(idx)

    # Set the starting state to 0
    dfa.set_starting_state(0)

    # Add the accepting state as the state that corresponds to the full match
    dfa.add_accepting_state(pattern_len)

    # Add transitions based on the suffix matching logic
    for idx in range(pattern_len + 1):
        for char in alphabet:
            next_state = compute_suffix_function(pattern, pattern[:idx] + char)
            dfa.add_transition(idx, char, next_state)

    return dfa


def automaton_match(pattern, text):
    """
    Match the pattern in the given text using a DFA built for the pattern.
    """
    # Build the alphabet from the pattern and text
    alphabet = build_alphabet(pattern, text)

    # Build the DFA for the pattern
    dfa = build_dfa(pattern, alphabet)

    # Start processing the text using the DFA
    current_state = dfa.starting_state
    count = 0

    for i, char in enumerate(text):
        try:
            current_state = dfa.get_next_state(current_state, char)
        except ValueError:
            # Reset to the starting state if no transition is found
            current_state = dfa.starting_state
            continue

        if dfa.is_accepting_state(current_state):
            # Pattern found, calculate position
            position = i - len(pattern) + 1
            print(f"Pattern found at position {position}")
            count += 1

    return count