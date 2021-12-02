p = open("input.txt")

x = 0
y = 0
aim = 0

for line in p:
  line = line.split()
  line[1] = int(line[1])
  if line[0] == "forward":
    x += line[1]
    y += line[1] * aim
  if line[0] == "up":
    aim -= line[1]
  if line[0] == "down":
    aim += line[1]

print(x*y)