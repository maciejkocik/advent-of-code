def common(tab, minmax):
  if minmax:
    return max(set(tab), key=tab.count)
  else:
    return min(set(tab), key=tab.count)

p = open("input.txt")

Numbers = []

for line in p:
  Numbers.append(line[:-1])

bitsLength = len(Numbers[0])
Bits = [[] for _ in range(bitsLength)]

for i in range(len(Numbers)):
  for j in range(len(Numbers[i])):
    Bits[j].append(Numbers[i][j])

Gamma, Epsilon = [], []

for i in range(bitsLength):
  Gamma.append(common(Bits[i], 1))
  Epsilon.append(common(Bits[i], 0))

Gamma = "".join(str(x) for x in Gamma)
Epsilon = "".join(str(x) for x in Epsilon)
print(int(Gamma, 2)*int(Epsilon, 2))