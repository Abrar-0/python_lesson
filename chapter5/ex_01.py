total = 0
count = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
        count += 1
        total += number
    except:
        print("Invalid input")
        continue
print(total , count, total/count)
