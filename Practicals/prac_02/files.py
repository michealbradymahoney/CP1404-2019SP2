out_file = open("name.txt", 'w')
name = input("What is your name?")
out_file.write(name)
out_file.close()

in_file = open("name.txt", 'r')
read_name = in_file.read()
print("Your name is", name)
in_file.close()

file = open("numbers.txt")
total = 0
for line in file:
    number = int(line)
    total = total + number
print(total)
file.close()