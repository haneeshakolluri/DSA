import numpy as np
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        arr = np.array(grid)     
        flat = arr.flatten()

        for i in flat:
            if i < 0:
                c += 1
        return c
