""""
def isValid(s: str) -> bool:
     for i in range(0,len(s)-1):
        if s[i]=='(' and s[len(s)-i-1]==')' or s[i]=='{' and s[len(s)-i-1]=='}' or s[i]=='[' and s[len(s)-i-1]==']':
            return True 
        else:
            return False
        
s="([{}])"
print(isValid(s))

Doesnt work for s=()[]{} or similar series 
"""

#Using stack
def isValid(s: str)->bool:
    stack=[]
    closeToopen={ ")":"(", "]":"[", "}":"{" }
    for char in s:
        if char in closeToopen:
            if stack and stack[-1]==closeToopen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)


s="([{}])"
s1='()[]'
print(isValid(s))
print(isValid(s1))

