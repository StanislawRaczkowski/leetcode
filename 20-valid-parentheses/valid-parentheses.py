class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{" }
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets:
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()
        return not stack
 
        # Pierwsza próba
        # for char in s:
        #     if char == "(":    
        #         stack.append("(")
        #     else:
        #         if not stack or stack[-1] != brackets[char]:
        #             return False
        #         stack.pop()
        #     if char == "[":    
        #         stack.append("[")
        #     else:
        #         if not stack or stack[-1] != brackets[char]:
        #             return False
        #         stack.pop()
        #     if char == "{":    
        #         stack.append("{")
        #     else:
        #         if not stack or stack[-1] != brackets[char]:
        #             return False
        #         stack.pop()

        # if not stack or stack[-1] != brackets[char]:
        #     return True 
        # else:
        #     return False