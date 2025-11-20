def isvalid(s):
    stack = []
    for char in s:
        if char in "(,[,{":
            stack.append(char)
            
        else:
            if not stack:
                return False
            
            
            top = stack.pop()
            
            if char == ")" and top != "(":
                return False
            if char == "]" and top != "[":
                return False
            if char == "}" and top != "{":
                return False
           
    return stack == []         

print(isvalid("({[]})"))
print(isvalid("()"))
print(isvalid("({)"))
print(isvalid("(][)])"))
print(isvalid("(({[()]}))"))

