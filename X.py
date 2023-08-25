import os
#os.remove("file1.txt")
#f=open("fil
f=open("file2.txt", "a")
#f.write("Hello World ! India is one of the Most Populous country ")
f.write("Hello World ! ")
f.close()
f=open("file2.txt", "r")
print(f.read())