def longest_parenthesis(s):
    balanced = [0]*len(s)
    opened = 0
    for i in range(len(s)):
        if s[i] == '(':
            opened += 1
        else:
            if opened > 0:
                opened -= 1
                balanced[i] += 2 + balanced[i - 1]
                if i - balanced[i] >= 0:
                    balanced[i] += balanced[i - balanced[i]]
    return max(balanced)
