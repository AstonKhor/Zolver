import numpy as np
import math

def normalize_vect_len(e1, e2):
    longest = np.array(e1 if len(e1) > len(e2) else e2)
    shortest = np.array(e2 if len(e1) > len(e2) else e1)
    indexes = np.array(range(len(longest)))
    np.random.shuffle(indexes)
    indexes = indexes[:len(shortest)]
    longest = longest[sorted(indexes)]
    return shortest, longest


# Match edges by performing a simple norm on each points
def diff_match_edges(e1, e2):
    if len(e2) < len(e1) * 0.9 or len(e2) > len(e1) * 1.1:
        return float('inf')
    shortest, longest = normalize_vect_len(e1, e2)
    diff = 0
    for i, p in enumerate(shortest):
        diff += np.linalg.norm(p[0] - longest[len(longest) - i - 1][0]) ** 2
    return math.sqrt(diff / len(shortest))  # RMSE