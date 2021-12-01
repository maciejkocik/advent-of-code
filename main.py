f = open("input.txt")

Measurements = []
Count = 0

for line in f:
  Measurements.append(int(line[:-1]))

for i in range(len(Measurements)):
  if Measurements[i] > Measurements [i-1]:
    Count += 1

print(Count)
