str = 'X-DSPAM-Confidence: 0.8475'
post = str.find(' ')
flt = str[post+1:]
f = float(flt)
print(type(f))
