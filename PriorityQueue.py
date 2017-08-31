from BinaryHeap import BinaryHeap

class PriorityQueue(BinaryHeap):

    def __init__(self):
        super().__init__()

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i][0] < self.heap_list[i//2][0]:
                self.heap_list[i], self.heap_list[i//2] = \
                    self.heap_list[i//2], self.heap_list[i]
            i = i // 2

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i][0] > self.heap_list[mc][0]:
                (self.heap_list[i], self.heap_list[mc] = 
                    self.heap_list[mc], self.heap_list[i])
            i = mc

    def decrease_key(self, nextVert, newDist):
        for i in range(0, self.current_size)
            if nextVert == self.heap_list[i][1]:
                self.heap_list[i][0] = newDist
                perc_up(i)
            i = i + 1

    def build_heap(self, a_list):

        # `perc_down` from the lowest father node
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [(0, None)] + a_list[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1