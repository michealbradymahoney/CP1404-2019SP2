# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
output_file = open("name.txt", "w")
name = input("Enter your name? ")
output_file.write(name)
output_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
input_file = open("name.txt", "r")
name = input_file.read()
input_file.close()
print("Your name is ", name)


# 3. Create a text file called numbers.txt and save it in your prac_02 directory.
# Put the numbers 17 and 42 on separate lines in the file and save it:
# 17
# 42
# Write code that opens "numbers.txt", reads the numbers and adds them together then prints the result,
# which should be... 59.
numbers_file = open("numbers.txt", "r")
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
numbers_file.close()
print(number1 + number2)

# 4. Now write a fourth block of code that can print the total for a file containing any number of numbers.
numbers_file = open("numbers.txt", "r")
total = 0
for line in numbers_file:
    number = int(line)
    total += number
numbers_file.close()
print(total)
