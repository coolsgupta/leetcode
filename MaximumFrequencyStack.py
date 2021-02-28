class FreqStack:

    def __init__(self):
        self.heap = []
        self.count_map = {}
        heapq.heapify(self.heap)
        self.count = 0

    def push(self, x: int) -> None:
        if x not in self.count_map:
            self.count_map[x] = 0
        self.count_map[x] += 1
        self.count += 1

        heapq.heappush(self.heap, (-self.count_map[x], -self.count, x))

    def pop(self) -> int:
        x = heapq.heappop(self.heap)[2]
        self.count_map[x] -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()