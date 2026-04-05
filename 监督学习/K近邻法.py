from typing import Sequence


# 构造KD树
class Node(object):
    def __init__(self, parent: 'Node', son: 'Node') -> None:
        self.parent = parent
        self.son = son


class KdTree(object):
    def __init__(self, samples: Sequence[tuple[int, ...]], dimention: int) -> None:
        self.samples = samples
        self.dimention = dimention

    def build(self):
        for dim in range(self.dimention):
            dim_column = []
            for i in self.samples:
                dim_column.append(i[0])



if __name__ == "__main__":
    T = {(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)}