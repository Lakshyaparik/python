file=open(r"C:\Users\Lakshy\OneDrive\Desktop\python\Files\Screenshot 2024-09-27 202126.png","rb")
content=file.read()
print(len(content),'bytes')
file.close()