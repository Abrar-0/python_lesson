def count(word,letter):
    wd = word
    count = 0
    for lr in wd:
        if lr == letter:
            count = count + 1
    print(count)

count('banana','a')
