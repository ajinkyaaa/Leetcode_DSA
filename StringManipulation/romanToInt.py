class Solution:
    def romanToInt(self, s: str) -> None:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res

s = Solution()
ans = s.romanToInt("IV")
print(ans)

"""
Steps:-
create dictionary with letters as key and value as their value
iterate string
if current letter  roman value is less than next value then decrement
else increment

"""