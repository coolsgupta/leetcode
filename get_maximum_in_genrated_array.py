class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # def get_max(n):
        #             if n == 0:
        #                 return 0
        #             if n == 1:
        #                 return 1
        #             if n%2 == 0:
        #                 return get_max(n/2)

        #             i = (n-1)/2
        #             return get_max(i) + get_max(i + 1)

        #         if n == 0:
        #             return 0

        #         return max(get_max(n), get_max(n-1))
        if n == 0:
            return 0
        arr = [0] * (n + 1)
        arr[1] = 1
        for x in range(2, n + 1):
            i = x // 2
            if x % 2 == 0:
                arr[x] = arr[i]

            else:
                arr[x] = arr[i] + arr[i + 1]

        return max(arr)


