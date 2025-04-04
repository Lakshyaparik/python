# files built in methods
# read([size])
# readline()
# readlines()
# write(string)
# writelines(list_of_strings)
# seek(offset[, whence])
# tell()
# flush()

file=open(r"C:\Users\Lakshy\OneDrive\Desktop\python\Files\files_methods\test.txt","r")

#print(file.read(10)) # read 5 bytes from the file

#print(file.readline()) # read a single line from the file

#print(file.readlines()) # read all lines from the file and return as a list

#file.write("This is a test file") # write a string to the file

#file.writelines(["This is line 1\n", "This is line 2\n"]) # write a list of strings to the file

# print(file.tell()) # get the current position of the file pointer
# file.seek(2) # move the file pointer to the beginning of the file
# print(file.read(19)) # read 10 bytes from the file
# print(file.tell()) # get the current position of the file pointer

file.flush() # flush the internal buffer to the file
print(file.read()) # read the entire file

file.close()