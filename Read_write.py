'''reads=open("C:\\Users\\Swapnil Patil\\Downloads\\PythonPractices\\python\\pythonpratices\\Read.txt.txt")
print(reads.read())
reads.close()'''
dr="C:\\Users\\Swapnil Patil\\Downloads\\PythonPractices\\python\\pythonpratices\\Read.txt.txt"
with open(dr,"r") as re:
    for i in re:
        print(i)

