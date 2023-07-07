class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_nums = {}
        for num in nums:
            hash_nums[num] = 1

        max_cnt = 1
        for num in list(hash_nums.keys()):
            if not num in hash_nums:
                continue
            hash_nums.pop(num)
            tmp = num + 1
            cnt = 1
            while tmp in hash_nums:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                hash_nums.pop(tmp)
                tmp += 1

            tmp = num - 1
            while tmp in hash_nums:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                hash_nums.pop(tmp)
                tmp -= 1
        return max_cnt
