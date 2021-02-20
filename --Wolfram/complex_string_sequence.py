"""
This module is meant to demonstrate how even a simple function like the 
string's replace method can lead to complex, random patterns given certain 
simple rules and a simple initial condition.
"""

def build_complex_text_patterns(initial_string: str, n: int,
                                rules: dict, file_name: str):
    """Create a list of strings length n based based on the rules"""
    rows: list = [initial_string]
    for i in range(n):
        # Apply the first applicable rule then break
        for old, new in rules.items():
            if old in rows[i]:
                rows.append(rows[i].replace(old, new))
                break
    with open(file_name + '.txt', 'w') as f:
        for row in rows:
            f.write(row + '\n')
        print(f'Saved as {file_name}.txt')




rules_a = {' X ': '  X',
        ' ': ' X '}

rules_b = {'X  ': ' XXXX',
        'X XX': ' X ',
        ' ': '  XX'}

rules_c = {'   X': 'X  ',
           '   ': 'XX',
           'X': '  X'}

rules_d = {'XXX': 'X ',
           '  ': ' X',
           ' ': 'X '}


# This rule creates a simple repetitive pattern.
build_complex_text_patterns(' ', 1000, rules_a, 'rule_a_pattern_simple')

# This slightly different rule creates a complex pattern
build_complex_text_patterns(' ', 400, rules_b, 'rules_b_pattern_complex')

# This creates a more dynamic pattern, but not complex
build_complex_text_patterns('X', 1000, rules_c, 'rules_c_pattern_complex')

# This creates a complex pattern
build_complex_text_patterns(' ', 1000, rules_d, 'rules_d_pattern_complex')
