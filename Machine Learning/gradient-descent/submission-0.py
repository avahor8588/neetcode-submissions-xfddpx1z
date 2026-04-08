class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for i in range(iterations):
            d = 2*init
            init = init - (learning_rate * d)
        return round(init,5)
    