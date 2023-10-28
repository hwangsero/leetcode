class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        pairs = {
            "I": {"V", "X"},
            "X": {"L", "C"},
            "C": {"D", "M"},
        }

        sum_val = 0
        i = 0
        while i < len(s):
            cur = s[i]
            if cur in pairs and i + 1 < len(s) and s[i + 1] in pairs[cur]:
                sum_val += (romans[s[i + 1]] - romans[cur])
                i += 1
            else:
                sum_val += romans[cur]
            i += 1
        return sum_val
