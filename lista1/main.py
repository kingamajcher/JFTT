import sys
from FA_matching import automaton_match 
from KMP_matching import kmp_automaton_match 

if len(sys.argv) != 4:
    print("Usage: <type of automata> <pattern> <filename>")
    sys.exit(1)

automata = sys.argv[1]
if automata not in {'FA', 'KMP'}:
    print("Automata type must be FA or KMP")
    sys.exit(1)
pattern = sys.argv[2]
filename = sys.argv[3]

try:
    with open(filename, 'r') as file:
        file_content = file.read()
        if automata == 'KMP':
            matches = kmp_automaton_match(pattern, file_content)
            print(f"Total matches: {matches}")
        elif automata == 'FA':
            matches = automaton_match(pattern, file_content)
            print(f"Total matches: {matches}")
except FileNotFoundError:
    print(f"File '{filename}' does not exist")



