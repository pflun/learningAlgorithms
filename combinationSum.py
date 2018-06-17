# -*- coding: utf-8 -*-
# 排列和组合（permutation and combination）https://www.youtube.com/watch?v=zIY2BWdsbFs
# https://mnmunknown.gitbooks.io/algorithm-notes/content/517_search_&_recursion_1.html
# DFS
class Solution(object):
    def combinationSum(self, candidates, target):

        return self.dfs(candidates, target, 0, [], [])

    def dfs(self, candidates, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        # 剪枝
        if target < 0:
            return

        # 为了去重的考虑，还是要 dfs 参数里带 index. 这里有一个细微的差别，因为同一个数可以用多次，新一层 dfs 迭代的时候要从上一层一样的 index 开始。然而还是要注意不要去看 index 之前的元素。
        for i in xrange(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)

        return res


# DFS 当前index与下一index（如果存在）
class Solution2:

    def combinationSum(self, candidates, target):
        self.res = []

        def helper(candidates, target, index, tmp):
            if sum(tmp) > target:
                return
            elif sum(tmp) == target:
                self.res.append(tmp)
            helper(candidates, target, index, tmp + [candidates[index]])
            if index + 1 < len(candidates):
                helper(candidates, target, index + 1, tmp + [candidates[index + 1]])

        for i in range(len(candidates)):
            helper(candidates, target, i, [candidates[i]])

        return self.res


test = Solution2()
print test.combinationSum([2, 3, 6, 7], 7)