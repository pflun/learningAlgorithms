class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        def helper(index, gas, cost):
            gas = gas[index:] + gas[:index]
            cost = cost[index:] + cost[:index]
            tank = 0
            for i in xrange(len(gas)):
                tank += gas[i]
                tank -= cost[i]
                if tank < 0:
                    return False
            return True

        for i in xrange(len(gas)):
            if helper(i, gas, cost):
                return i
        return -1

test = Solution()
print test.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])