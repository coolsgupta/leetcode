class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_map = {}
        pair_count = 0
        for x in nums:
            if x not in count_map:
                count_map[x] = 0

            count_map[x] += 1

            rem = k - x
            if rem not in count_map:
                continue

            else:
                if count_map[rem] >= 1:
                    count_map[x] -= 1
                    count_map[rem] -= 1

                    if count_map[x] == -1:
                        count_map[x] += 2
                        continue

                    pair_count += 1

        return pair_count

