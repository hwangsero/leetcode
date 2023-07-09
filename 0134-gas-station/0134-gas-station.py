class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 1:
            return 0 if gas[0] - cost[0] >= 0 else -1
        diff = [gas[i] - cost[i] for i in range(n)]
        left = right = 0
        total = diff[0]
        while (right + 1) % n != left:
            if total < 0:
                left -= 1
                if left < 0:
                    left = n - 1
                total += diff[left]
            else:
                right += 1
                right %= n
                total += diff[right]
            if left == right:
                return -1
        if total >= 0:
            return left
        else: 
            return -1
