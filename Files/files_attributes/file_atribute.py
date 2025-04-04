# file.name: Returns the name of the file.

# file.mode: Returns the mode in which the file was opened (e.g., "r", "w").

# file.closed: Returns True if the file is closed, otherwise False.

# file.encoding: Returns the encoding used to open the file (e.g., "UTF-8").

# file.newlines: Shows the newline convention used in the file (\n, \r\n, etc.).


# 1. file.name
file = open(r"C:\Users\Lakshy\OneDrive\Desktop\python\Files\files_attributes\example.txt", "w")
print("File Name:", file.name)  # Outputs the name of the file

# 2. file.mode
print("File Mode:", file.mode)  # Outputs the mode in which the file is opened

# 3. file.closed
print("Is File Closed?:", file.closed)  # Outputs False (file is open)
file.close()  # Closing the file
print("Is File Closed Now?:", file.closed)  # Outputs True (file is now closed)

# 4. file.encoding
file = open("example.txt", "r", encoding="UTF-8")
print("File Encoding:", file.encoding)  # Outputs the file's encoding
file.close()

# 5. file.newlines
file = open("example.txt", "r")
print("File Newlines:", file.newlines)  # Outputs newline conventions used in the file
file.close()
