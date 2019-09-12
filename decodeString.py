class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c == ']':
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                if stack and stack[-1] == '[':
                    stack.pop()
                # how to handle 10+
                if stack and stack[-1].isdigit():
                    n = int(stack.pop())
                for _ in range(n):
                    stack.append(curr)
            else:
                stack.append(c)
        return ''.join(stack)