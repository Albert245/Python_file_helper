def find_bracket_pairs(string):
    stack = []
    pairs = []
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                pairs.append((stack.pop(), i))
    pairs.sort(key=lambda x: x[1] - x[0], reverse=True)
    return pairs

string = "((())())()(()))"
bracket_pairs = find_bracket_pairs(string)
print(bracket_pairs)