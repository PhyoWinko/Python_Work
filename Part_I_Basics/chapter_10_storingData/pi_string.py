filename = "pi_digits.txt"

with open(filename) as file:
    lines = file.readlines()

print(lines)

pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string, len(pi_string))

    