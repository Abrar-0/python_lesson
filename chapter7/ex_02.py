# filename = input("Enter your file name: ")
count = 0
num = 0
try:
    fread = open("task2.txt")
    # inp = fread.read()
    for lines in fread:
        if lines.startswith('X-DSPAM-Confidence:'):
            count += 1
            post = lines.find(" ")
            l = lines[post+1:]
            lf = float(l)
            num += lf
            # print(lines, end='')
    print('Number of lines: ', count)
    print('Average spam confidence:', num/count)
except:
    print("File doesn't exist")
    quit()
