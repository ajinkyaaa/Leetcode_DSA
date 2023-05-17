"""
()
((()))
()()

())
)()
()())
(()))

( => add to stack
) and stack[-1] ==( then pop else: return False
return len stack ==0

"""

def validParenthesis(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return len(stack) == 0
 
assert validParenthesis("()") == True
assert validParenthesis("((()))") ==True
assert validParenthesis("()()")==True

assert validParenthesis("())")==False
assert validParenthesis(")()")==False
assert validParenthesis("()())")==False
assert validParenthesis("(()))")==False
