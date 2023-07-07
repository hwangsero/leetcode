class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_nums = set(nums)

        max_cnt = 1
        for num in hash_nums:
            if num - 1 in hash_nums:
                continue

            current_num = num
            current_cnt = 0

            while current_num in hash_nums:
                current_num += 1
                current_cnt += 1

            max_cnt = max(max_cnt, current_cnt)

        return max_cnt
