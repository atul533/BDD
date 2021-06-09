f1 = open("C:\\Users\\atul.singh\\Desktop\\doc1.txt", "r")
f2 = open("C:\\Users\\atul.singh\\Desktop\\doc2.txt", "w+")

lines = f1.readlines()
for line in lines[0:2]:
    if 'Error' in line:
        pass
    else:
        f2.write(line.upper())

f2.seek(0)
print(f2.read())
