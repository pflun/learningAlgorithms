class Solution(object):
    def getPermutation(self, n, k):
        self.res = []
        visited = [False] * (n + 1)

        def helper(n, tmp, visited):
            if len(tmp) == n:
                self.res.append(tmp)

            for i in range(1, n + 1):
                if not visited[i]:
                    visited[i] = True
                    tmp += str(i)
                    helper(n, tmp, visited)
                    tmp = tmp[:-1]
                    visited[i] = False

        helper(n, '', visited)

        return self.res[k - 1]

test1 = Solution()
print test1.getPermutation(3, 3)