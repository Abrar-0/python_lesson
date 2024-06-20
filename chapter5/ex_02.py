largest = None
smallest = None
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        numb = int(num)
        if largest is None or numb > largest:
            largest = numb
        if smallest is None or numb < smallest:
            smallest = numb
    except:
        print("Invalid input")
print ("Maximum is ", largest)
print ("Minimum is ", smallest)

