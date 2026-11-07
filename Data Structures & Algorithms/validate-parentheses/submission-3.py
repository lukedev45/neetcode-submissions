class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            if len(stack) > 0:
                if stack[-1] == "(" and bracket == ")":
                    stack.pop()
                elif stack[-1] == "{" and bracket == "}":
                    stack.pop()
                elif stack[-1] == "[" and bracket == "]":
                    stack.pop()
            else:
                return False
        return True