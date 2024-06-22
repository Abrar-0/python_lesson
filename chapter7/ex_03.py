filename = input("Enter your file name: ")
count = 0
try:
    if filename == 'na na boo boo':
        print ('NA NA BOO BOO TO YOU - You have been punk\'d!')
    else:
        fread = open(filename)
        # inp = fread.read()
        for lines in fread:
            if lines.startswith('Subject:'):
                count += 1
                # print(lines, end='')
        print(f'There are {count} subject lines in {filename}')
except:
    print(f'Filename {filename} doesn\'t exist')
    quit()
