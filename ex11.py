
import math

def closest_pair(points):
    min_dist = float('inf')
    pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.dist(points[i], points[j])

            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])

    return pair, min_dist


points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10)]

pair, distance = closest_pair(points)

print("Closest pair:", pair)
print("Minimum distance:", round(distance, 2))
sss