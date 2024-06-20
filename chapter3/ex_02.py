hrs = input("Enter Hours:")
try:
    h = float(hrs)
    rate = input("Enter Rate:")
    try:
        r = float(rate)
    except:
        print('Please enter a number')
    if(h > 40):
        pay= 40*r + (h-40)*(r*1.5)
    else:
        pay = h*r
    print(pay)
except:
    print('Please enter a number')

