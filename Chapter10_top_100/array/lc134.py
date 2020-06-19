class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = []
        for start in range(len(gas)):
            gas_1 = gas[start:] + gas[:start]
            cost_1 = cost[start:] + cost[:start]
            gas_reste = 0
            Flag = True
            for elm1, elm2 in zip(gas_1, cost_1):
                gas_reste += elm1 - elm2
                if gas_reste < 0:
                    Flag = False
                    break
            if Flag:
                return start
        return -1
