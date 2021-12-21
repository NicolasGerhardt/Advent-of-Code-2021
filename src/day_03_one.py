
BYTE_LENGTH = 12
DATA_FILENAME = "data.txt"

def get_data(filename):
  lines = []
  with open(filename, "r") as file:
    for line in file:
      line = line.strip()
      if (line != ""):
        lines.append(line)
    return lines

def setup_counter():
  counter = {}
  counter["total_records"] = 0
  for i in range(BYTE_LENGTH):
    counter[str(i)] = {"1": 0, "0": 0}
  return counter

def incr(counter, numberStr):
  number = int(numberStr, 2)
  counter["total_records"] += 1
  for i in range(BYTE_LENGTH):
    bit = 2**i
    if number & bit == bit:
      counter[str(i)]["1"] += 1
    else:
      counter[str(i)]["0"] += 1

def power_consumption(counter):
  gammaStr = ""
  epsilonStr = ""
  for i in range(BYTE_LENGTH):
    if counter[str(i)]["1"] > counter[str(i)]["0"]:
      gammaStr = "1" + gammaStr
      epsilonStr = "0" + epsilonStr
    elif counter[str(i)]["1"] < counter[str(i)]["0"]:
      gammaStr = "0" + gammaStr
      epsilonStr = "1" + epsilonStr
    else:
      gammaStr = "E" + gammaStr
      epsilonStr = "E" + epsilonStr

  gamma = int(gammaStr, 2)
  epsilon = int(epsilonStr, 2)
  print(f"gamma: {gammaStr} -> {gamma}")
  print(f"epsilon: {epsilonStr} -> {epsilon}")
  print(f"bitwise &: {gamma & epsilon}")
  
  return gamma * epsilon




def main():
  data = get_data(DATA_FILENAME)
  counter = setup_counter()
  for number in data:
    incr(counter, number)

  for value in counter:
    print(f"{value}: {counter[value]}")

  print(f"power consumption: {power_consumption(counter)}")

if __name__ == "__main__":
  main()