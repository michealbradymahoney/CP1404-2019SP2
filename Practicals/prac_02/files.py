OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, 'w')
name = input("What is your name?")
out_file.write(name)
out_file.close()


