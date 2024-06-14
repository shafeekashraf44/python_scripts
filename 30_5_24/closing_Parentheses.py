# Define lists of opening and closing brackets
opening = ["[", "{", "("]
closing = ["]", "}", ")"]

def checking(myStr):
    stack = []
    for i in myStr:
        if i in opening:
            stack.append(i)
        elif i in closing:
            pos = closing.index(i)
            # Check if the top of the stack matches the corresponding opening bracket
            if (len(stack) > 0) and (opening[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced"
    # Check if any unmatched opening brackets remain
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

# Input string of brackets
STRING = "{[]]{()}}"

# Print the result of checking if the input string is balanced
print(checking(STRING))
