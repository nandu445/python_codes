# Write content to a new file (or overwrite if it exists)
with open("hellonandu.txt", "r+") as file:
    file.write("Hello Nandu!\n")
    file.write("This is a test file.\n")
    file.write("Python file handling is easy and regular!\n")
