import math

class DiscretizationRandom:
    def __init__(self, min_val, max_val):
        self.x = [1]
        self.y = [2]
        self.z = [3]
        self.u = []
        for i in range(10000):
            self.x.append(math.fmod(171 * self.x[i], 30269))
            self.y.append(math.fmod(170 * self.y[i], 30307))
            self.z.append(math.fmod(172 * self.z[i], 30323))
            self.u.append(math.fmod(self.x[i+1]/30269 + self.y[i+1]/30307 + self.z[i+1]/30323, 1))
        self.min_val = min_val
        self.max_val = max_val
        
    def get_discretized_random(self):
        val_range = self.max_val - self.min_val
        discretized_vals = []
        for i in range(10000):
            val = self.min_val + math.floor(self.u[i] * val_range)
            discretized_vals.append(val)
        return discretized_vals