filename = input("Enter your file name: ")
try:
    fread = open(filename)
    inp = fread.read()
    for lines in inp:
        print(lines, end='')
except:
    print("File doesn't exist")
    quit()
