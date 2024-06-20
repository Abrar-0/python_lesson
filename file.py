fout = open('output.txt', 'w')
inp = 'Hello mf \n'
input1 = input("Write what you want: ") + '\n'
fout.write(inp)
fout.write(input1)
fout.close()

fread = open('output.txt')
for lines in fread:
    # lines = lines.rstrip()
    print(lines, end='')

