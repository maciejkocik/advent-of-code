p = open("input.txt")

x = 0
y = 0

for line in p:
  line = line.split()
  line[1] = int(line[1])
  if line[0] == "forward":
    x += line[1]
  if line[0] == "up":
    y -= line[1]
  if line[0] == "down":
    y += line[1]

print(x*y)