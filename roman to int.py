class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    s = "MCMXCIV"
    roman = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman [s[i]] < roman[s[i + 1]]:
            g=print(s)
            a=print(i)
            d=print(roman [s[i]])
            res -= roman [s[i]]
        else:
            res += roman[s[i]]
            g=print(s)
            a=print(i)
            d=print(roman [s[i]])
    print(res)