class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def dfs(open_cnt:int, close_cnt: int, cur_list: List[str]):
            if open_cnt == 0 and close_cnt == 0:
                ans.append("".join(cur_list))
                return

            if open_cnt > 0:
                cur_list.append("(")
                dfs(open_cnt - 1, close_cnt, cur_list)
                cur_list.pop()

            if close_cnt > 0 and open_cnt < close_cnt:
                cur_list.append(")")
                dfs(open_cnt, close_cnt - 1, cur_list)
                cur_list.pop()
        dfs(n, n, [])
        return ans
