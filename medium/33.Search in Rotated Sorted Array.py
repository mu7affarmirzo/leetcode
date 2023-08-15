class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1
        while (start < end):
            mid = (start + end) / 2
            if (nums[mid] > nums[end]):
                start = mid + 1
            else:
                end = mid

        smallest = start

        start, end = 0, len(nums) - 1
        if (target >= nums[smallest] and target <= nums[end]):
            start = smallest
        else:
            end = smallest - 1

        while (start <= end):
            mid = (start + end) / 2
            if (nums[mid] > target):
                end = mid - 1
            elif (nums[mid] < target):
                start = mid + 1
            else:
                return True

        return False