file=open(r"C:\Users\Lakshy\OneDrive\Desktop\python\Files\test.txt","w")
content=file.write("This is a test file")

file=open(r"C:\Users\Lakshy\OneDrive\Desktop\python\Files\test.txt","r")
content=file.read()
#print(content)
file.close()


#append mode   can be used to add content to the file pointer move to end of file
#if file does not exist it will create a new file

file=open(r"C:\Users\Lakshy\OneDrive\Desktop\python\Files\test.txt","a+")

file.write("\nThis is a APPEND MODE ")

file=open(r"C:\Users\Lakshy\OneDrive\Desktop\python\Files\test.txt","r")
content=file.read() 
print(content)
file.close()