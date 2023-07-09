class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        answer = 0
        total = 0
        cur = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]

            if cur < 0:
                cur = 0
                answer = i + 1
        return answer if total >= 0 else -1


