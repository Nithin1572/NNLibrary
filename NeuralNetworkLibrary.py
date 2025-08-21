import pandas as pd # type: ignore
import numpy as np # type: ignore

class NNLib:
    def __init__(self, n):
        self.n = n

    def mult(self, x):
        return self.n * x