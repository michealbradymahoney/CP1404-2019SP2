OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, 'w')
name = input("What is your name?")
out_file.write(name)
out_file.close()

in_file = open(OUTPUT_FILE, 'r')
read_name = in_file.read()
print("Your name is", name)
in_file.close()

