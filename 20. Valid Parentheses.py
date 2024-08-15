class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]     #create stack
        bracket_mapping={      #create dictionary for bbracket
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:  #s string
            if char in bracket_mapping.values():     #If it's an opening bracket
                stack.append(char)    #If it's an opening bracket
            elif char in bracket_mapping.keys():  ## If it's a closing bracket
                if stack and stack[-1] == bracket_mapping[char]: #bracket_map[')'] gives us (.
                    stack.pop()       #remove last char
                else:
                    return False
        return not stack       #the stack is empty, all brackets were matched


