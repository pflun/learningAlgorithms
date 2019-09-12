class Solution(object):
    def couplePossibility(self, n, k):
        self.res = []
        self.used = [False] * (n + 1)
        self.couples = 0

        def dfs(n, tmp, prev):
            if len(tmp) == k:
                # shallow copy
                self.res.append(tmp[:])
                if isCouple(tmp[:]):
                    self.couples += 1

            for i in range(prev + 1, n + 1):
                if self.used[i]:
                    continue
                self.used[i] = True
                tmp.append(i)
                dfs(n, tmp, i)
                # backtracking:
                self.used[i] = False
                tmp.pop()

        def isCouple(threeSome):
            if threeSome[0] % 2 == 1 and threeSome[1] % 2 == 0 and threeSome[1] - threeSome[0] == 1:
                return True
            elif threeSome[1] % 2 == 1 and threeSome[2] % 2 == 0 and threeSome[2] - threeSome[1] == 1:
                return True
            return False

        dfs(n, [], 0)

        return self.couples, len(self.res)

test = Solution()
print test.couplePossibility(36, 3)