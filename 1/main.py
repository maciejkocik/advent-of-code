f = open("input.txt")

Measurements = []
Count = 0

for line in f:
  Measurements.append(int(line[:-1]))

for i in range(len(Measurements)-3):
  sumA = Measurements[i]+ Measurements[i+1]+ Measurements[i+2]
  sumB = Measurements[i+1] + Measurements[i+2] + Measurements[i+3]
  if sumB > sumA:
    Count += 1

print(Count)
