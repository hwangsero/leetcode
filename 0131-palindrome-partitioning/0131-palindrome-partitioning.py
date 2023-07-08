class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        def check_palindrome(substr):
            left, right = 0, len(substr) - 1
            while left < right:
                if substr[left] != substr[right]:
                    return False
                left += 1
                right -= 1
            return True


        def dfs(idx, arr):
            if idx == len(s):
                ans.append(arr[:])
                return

            for end_idx in range(idx + 1, len(s) + 1):
                substr = s[idx:end_idx]
                if check_palindrome(substr):
                    arr.append(substr)
                    dfs(end_idx, arr)
                    arr.pop()

        dfs(0, [])
        return ans


        
