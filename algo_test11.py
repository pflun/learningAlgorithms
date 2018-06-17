def globalv1():
    global res
    res = 20
    globalv2()
    globalv2()
    return res


def globalv2():
    global res
    res = res - 10

print globalv1()

print "1+1i".split('+')


class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        self.visited = [False] * len(candidates)

        def dfs(nums, index, tmp):
            if sumUp(tmp) == target:
                self.res.append(tmp[:])
            for i in range(index, len(nums)):
                if self.visited[i]:
                    continue
                tmp.append(nums[i])
                self.visited[i] = True
                dfs(nums, index + 1, tmp)
                self.visited[i] = False
                tmp.pop()

        def sumUp(arr):
            res = 0
            for a in arr:
                res += a
            return res

        dfs(candidates, 0, [])

        return self.res

test = Solution()
print test.combinationSum([2,3,6,7], 7)

print [1, 2, 3].index(2)

dict = {}
pattern = "abbac"
for w in pattern:
    dict[w] = dict.get(w, 0) + 1
print sorted(dict.values())

lex = ['ABDC', 'ABCD', 'DCBA', 'DCAB']
print sorted(lex)

print ord('a') * 10
