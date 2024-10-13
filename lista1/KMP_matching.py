from functions import *
from Automaton import Automaton

def build_kmp_automaton(pattern, alphabet):
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    dfa = Automaton()

    # Add states
    for idx in range(m + 1):
        dfa.add_state(idx)
    
    # Set starting state
    dfa.set_starting_state(0)
    
    # Add accepting state
    dfa.add_accepting_state(m)

    # Add transitions
    for idx in range(m + 1):
        for char in alphabet:
            if idx < m and pattern[idx] == char:
                next_state = idx + 1
            else:
                next_state = kmp_automaton_transition(pi[idx - 1], char, pattern, pi) if idx > 0 else 0
            dfa.add_transition(idx, char, next_state)
    
    return dfa


def kmp_automaton_match(pattern, text):
    alphabet = build_alphabet(pattern, text)
    dfa = build_kmp_automaton(pattern, alphabet)
    
    current_state = 0
    count = 0

    for i, char in enumerate(text):
        try:
            current_state = dfa.get_next_state(current_state, char)
        except ValueError:
            current_state = 0
            continue

        if dfa.is_accepting_state(current_state):
            position = i - len(pattern) + 1
            print(f"Pattern found at position {position}")
            count += 1

    return count
