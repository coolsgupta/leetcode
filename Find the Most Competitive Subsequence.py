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

        stack = [nums[0]]
        i = 1
        flag_index = n - k + 1

        while i < n and i < flag_index:
            if nums[i] <= stack[-1]:
                while stack and nums[i] < stack[-1] and i < flag_index:
                    stack.pop()
                    flag_index -= 1

            stack.append(nums[i])
            flag_index += 1

            i += 1

        stack.extend(nums[flag_index:])
        return stack[:k]


if __name__ == '__main__':
    case = [84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71]
    k = 24
    soln = Solution().mostCompetitive(case, k)
    print(soln)
