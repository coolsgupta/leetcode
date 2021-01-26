class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        j = 0
        i = 1

        if arr[-1] < len(arr) + k:
            return arr[-1] + (k - arr[-1] + len(arr))

        while (True):
            if i != arr[i - j - 1]:
                j += 1
                if j == k:
                    return i

            i += 1

