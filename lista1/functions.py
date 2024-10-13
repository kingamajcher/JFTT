# builds a set of unique characters from both the pattern and text
def build_alphabet(pattern, text):
    char_set = set(pattern + text)
    return ''.join(char_set)

# calculates the longest suffix of 'text' that is also a prefix of 'pattern'
def compute_suffix_function(pattern, text):
    max_len = 0
    min_len = min(len(pattern), len(text))
    
    for i in range(1, min_len + 1):
        if pattern[:i] == text[-i:]:
            max_len = i
    return max_len

# calculates the prefix function (pi function) 
def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

# simulates the kmp automaton transition
# current state 'q', input character 'a', pattern, prefix function 'pi'
def kmp_automaton_transition(q, a, pattern, pi):
    while q > 0 and (q >= len(pattern) or pattern[q] != a):
        q = pi[q - 1]
    if q < len(pattern) and pattern[q] == a:
        return q + 1
    return 0
