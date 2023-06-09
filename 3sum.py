class Solution(object):
    def three_sum(self, s):
        s = sorted(s)  # O(nlogn)
        output = set()
        for k in range(len(s)):
            target = -s[k]
            i, j = k + 1, len(s) - 1
            while i < j:
                sum_two = s[i] + s[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((s[k], s[i], s[j]))
                    i += 1
                    j -= 1
        return output

s = Solution()

a = s.three_sum([0,0,0])
print(a)