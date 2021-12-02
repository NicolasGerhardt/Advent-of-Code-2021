from types import MemberDescriptorType


def get_data(filename):
  lines = []
  with open(filename, "r") as file:
    for line in file:
      line = line.strip()
      if (line != ""):
        lines.append(line)
    return lines

class Submarine:
  def __init__(self) -> None:
      self.position = 0
      self.depth = 0
      self.aim = 0
  def forward(self, amount):
    self.position += amount
    self.depth += self.aim * amount
  def down(self, amount):
    self.aim += amount
  def up(self, amount):
    self.aim -= amount
  def final(self):
    return self.position * self.depth

mySub = Submarine()
movementData = get_data("data.txt")

for move in movementData:
  direction = move.split(" ")[0]
  amount = int(move.split(" ")[1])
  if direction == "forward":
    mySub.forward(amount)
  elif direction == "down":
    mySub.down(amount)
  if direction == "up":
    mySub.up(amount)

print(f"position: {mySub.position}")
print(f"depth: {mySub.depth}")
print(f"aim: {mySub.aim}")
print(f"total: {mySub.final()}")