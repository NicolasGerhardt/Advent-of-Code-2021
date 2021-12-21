def get_data(filename):
  lines = []
  with open(filename, "r") as file:
    for line in file:
      line = line.strip()
      if (line != ""):
        lines.append(line.split(" "))
    return lines

def get_movement_type(data: str):
  if data == "forward":
    return (1, 0)
  elif data == "down":
    return (0, 1)
  elif data == "up":
    return (0, -1)
  return (0, 0)

class Submarine:
  def __init__(self) -> None:
      self.position = (0,0)
  def move(self, movement, speed):
    for x in range(speed):
      self.position = tuple(map(lambda i, j: i + j, movement, self.position))

mySub = Submarine()
movementData = get_data("day_02_data.txt")

for command in movementData:
  mySub.move(get_movement_type(command[0]), int(command[1]))

print(f"location: {mySub.position}")
print(f"result: {mySub.position[0] * mySub.position[1]}")