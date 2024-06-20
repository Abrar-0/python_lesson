# word = input("Enter: ")
# if word == 'banana':
#     print('All right, bananas.')
# elif word < 'banana':
#     print('Your word,' + word + ', comes before banana.')
# else:
#     print('Your word,' + word + ', comes after banana.')
# print(dir(word))
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
