class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        s = set(nums)
        freqs = []
        for i in s:
            freqs.append(nums.count(i))
        temp = zip(s, freqs)
        print([i for i in temp])

            # temp.append(zip(nums.count(i), i))
        return 1



a = Solution()
a = a.frequencySort([1,1,2,2,2,3])
print(a)

x = [1,1,0]
print(x.remove(max(x)))
print(x)