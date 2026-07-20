'''EuclideanDistance2D'''
q1: float = input()
q2: float = input()
p1: float = input()
p2: float = input()

EU_DISTANCE = ((float(q1) - float(p1)) ** 2 + (float(q2) - float(p2)) ** 2) ** 0.5
print(EU_DISTANCE)
