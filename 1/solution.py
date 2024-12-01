# Part 1
with open('left-list.txt', 'r') as file:
    leftList = [line.strip() for line in file.readlines()]

with open('right-list.txt', 'r') as file:
    rightList = [line.strip() for line in file.readlines()]

distanceValues = []
for i in range(1000):
    distance = abs(int(sorted(leftList)[i]) - int(sorted(rightList)[i]))
    distanceValues.append(distance)

print("sum of distanceValues =", sum(distanceValues))

# Part 2
totalSimilarityScore = 0
for value in leftList:
    totalSimilarityScore += int(value) * rightList.count(value)

print("total similarity score =", totalSimilarityScore)
