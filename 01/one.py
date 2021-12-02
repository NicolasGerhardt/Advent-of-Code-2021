def get_data(filename) -> list[str]:
  lines = []
  with open(filename, "r") as file:
    for line in file:
      line = line.strip()
      if (line != ""):
        lines.append(line)
    return lines

data = get_data("data.txt")
prev = None
count = 0
for text in data:
  if prev is None:
    print(f"{text} no change")
    prev = int(text)
    continue
  print(text, end="")
  if prev < int(text):
    count += 1
    print(" (increased)")
  else:
    print(" (not increased)")
  prev = int(text)
    
print(f"count: {count}")