class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda box: box[1], reverse=True)

        totalUnits = 0
        for numberOfBoxes, unitsPerBox in boxTypes:
            # Take as many boxes until we're out of space on the truck
            # or we're out of boxes of this type
            numBoxes = min(truckSize, numberOfBoxes)
            totalUnits += numBoxes * unitsPerBox
            truckSize -= numBoxes
        return totalUnits


a = Solution()
a = a.maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35)
print(a)

arr = sorted([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0])
print(sum(arr[1:-2])/len(arr[1:-2]))