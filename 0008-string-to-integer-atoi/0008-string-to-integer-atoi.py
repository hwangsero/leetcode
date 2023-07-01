class Solution:
    def myAtoi(self, s: str) -> int:
        start = 0

        for idx, val in enumerate(s):
            if val != ' ':
                start = idx
                break

        s = s[start:]
        
        end = len(s)
        for idx, val in enumerate(s):
            if idx == 0 and (val  == '-' or val == '+'):
                if len(s) == 1 or not s[1].isdigit():
                    return 0
                continue
            if not val.isdigit():
                end = idx
                break
        s = s[:end]
        result = int(s) if s != '' else 0
        result = result if result < 2**31 - 1 else 2**31 - 1
        result = result if result > -2**31 else -2**31
        return result
