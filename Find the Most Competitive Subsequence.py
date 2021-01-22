# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         res = nums[n - k:n]
#         for x in nums[:n - k][::-1]:
#             if x <= res[0]:
#                 res.remove(max(res))
#                 res = [x] + res
#
#         return res
#
#

class Solution:
    def mostCompetitive(self, nums, k):
        n = len(nums)
        if k == n:
            return nums

        stack = []
        flag_index = n - k

        for val in nums:
            while stack and val < stack[-1] and flag_index > 0:
                stack.pop()
                flag_index -= 1

            stack.append(val)

        return stack[:k]


if __name__ == '__main__':
    case = [84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71]
    k = 24
    soln = Solution().mostCompetitive(case, k)
    print(soln)
