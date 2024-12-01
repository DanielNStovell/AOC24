with open("Data.txt", "r") as file:
  Data = [i.strip() for i in file.readlines()]

r = [i.split()[0] for i in Data]
l = [i.split()[1] for i in Data]

r.sort()
l.sort()

total = 0

for count in r:
  total += int(count) * l.count(count)

print(total)
