def computegrade(sc):
    try:
        score = float(sc)
        if (score > 1.0):
            return('Bad Score')
        elif (score >= 0.9):
            return('A')
        elif (score >= 0.8):
            return('B')
        elif (score >= 0.7):
            return('C')
        elif (score >= 0.6):
            return('D')
        elif (score < 0.6):
            return('F')
        else:
            print('Bad Score')
    except:
        print('Enter number from 0.0 to 1.0')

print(computegrade(input("Enter score: ")))
