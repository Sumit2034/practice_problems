# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

def is_valid_parenthesis(a):
    if not a:
        return "enter a parenthesis string not null value"
    stack = []
    star_stack = []
    length = len(a)
    
    for i in range(length):
        if a[i] == "(":
            stack.append(a[i])
        if a[i] == "*":
            star_stack.append(a[i])
        if a[i] == ")" and (stack or star_stack):
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                if star_stack:
                    star_stack.pop()
                else:
                    print("not_valid")
                    break
    if not stack:
        return "valid"
    else:
        if len(stack) == len(star_stack):
            return "valid"
        return "invalid"

a = "((()))"
print(is_valid_parenthesis(a), a)
a = ")("
print(is_valid_parenthesis(a), a)
a = "("
print(is_valid_parenthesis(a), a)
a = "(*)"
print(is_valid_parenthesis(a), a)
a = "(*"
print(is_valid_parenthesis(a), a)
a = "((**"
print(is_valid_parenthesis(a), a)
a = "*)"
print(is_valid_parenthesis(a), a)
a = "((*"
print(is_valid_parenthesis(a), a)
a = "**))"
print(is_valid_parenthesis(a), a)
