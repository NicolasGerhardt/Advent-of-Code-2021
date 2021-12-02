def get_data(filename) -> list[int]:
  lines = []
  with open(filename, "r") as file:
    for line in file:
      line = line.strip()
      if (line != ""):
        lines.append(int(line))
    return lines

def three_sum(index, data: list[int]) -> int:
  return data[index] + data[index-1] + data[index-2]

data = get_data("data.txt")
prev = None
count = 0

for i in range(2, len(data)):
  print(".", end="")
  if prev is None:
    prev = three_sum(i, data)
    continue
  if prev < three_sum(i, data):
    count += 1
  prev = three_sum(i, data)

print(f"\ncount: {count}")