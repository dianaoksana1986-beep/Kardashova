def validate_brackets(code: str) -> bool:
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}
    
    for char in code:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if stack and stack[-1] == brackets_map[char]:
                stack.pop()  
            else:
                return False  
                
    return len(stack) == 0

print(validate_brackets("def func(): print([1, 2, 3])")) 
print(validate_brackets("if (x > 0 { print(x) }"))        
print(validate_brackets("([)]"))                        