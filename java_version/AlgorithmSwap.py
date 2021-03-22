class Solution:
    def __init__(self):
        self.count = 0

    def splitAtMid(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        return self.merge(self.splitAtMid(nums[:mid]), self.splitAtMid(nums[mid:]))

    def merge(self, left, right):
        merged = []
        lIndex = 0
        rIndex = 0

        while lIndex < len(left) and rIndex < len(right):
            if left[lIndex] <= right[rIndex]:
                merged.append(left[lIndex])
                self.count += rIndex
                lIndex += 1
                
            if rIndex >= len(right) or (lIndex < len(left) and left[lIndex] <= right[rIndex]):
                merged.append(left[lIndex])
                self.count += rIndex
                lIndex += 1

            else:
                merged.append(right[rIndex])
                rIndex += 1

        return merged

    def getCounts(self, arr):
        self.splitAtMid(arr)
        return self.count


def howManySwaps(arr):
    return Solution().getCounts(arr)


    # for i in range(len(arr) - 1):
    #     for j in range(i, len(arr)):
    #         if arr[j] < arr[i]:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             count += 1
    #
    # return count






if __name__ == '__main__':
    count = 0
    case = [5,1,4,2]
    print(howManySwaps(case))