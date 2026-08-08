class Solution:
    def isValid(self, s: str) -> bool:
        brackets={'}':'{',']':'[',')':'('}
        stack=[]
        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif c in brackets.keys():
                if len(stack)==0:
                    return False
                if brackets[c]!=stack.pop():
                    return False
                    
        return len(stack)==0


        