from longest_parenthesis import longest_parenthesis


def test_func(s):
    print(longest_parenthesis(s))


if __name__ == '__main__':
    test_func('())(())') #4
    test_func(')(()))))((((()') #4
    test_func(')))()(()(((()()()') #6
    test_func('((()(()))') #8
