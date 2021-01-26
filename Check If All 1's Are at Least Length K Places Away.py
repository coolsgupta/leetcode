class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        a = -1
        for i, x in enumerate(nums):
            if x == 1:
                # print(i)
                if a >= 0:
                    # print(i-a)
                    if i - a <= k:
                        return False

                a = i

        return True
