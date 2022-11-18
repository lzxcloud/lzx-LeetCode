class Solution:
    @classmethod
    def lengthOfLongestSubstring(self, s : str) -> int:
        times = max = 0
        tmp_chr = []
        for item in s:
            if item not in tmp_chr:
                times += 1
                tmp_chr.append(item)
            else:
                if times > max:
                    max = times
                times = 0
                tmp_chr = []

            print(tmp_chr)
            print(times, max)
        return max


s = "pwwkew"

print(Solution.lengthOfLongestSubstring(s))
