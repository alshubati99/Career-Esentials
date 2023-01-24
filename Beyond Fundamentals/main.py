# Lists: 
city1 = "Sana'a"
city2 = "Aden"
city3 = "Ibb" 
city4 = "Dubia"
cities = [
    'Tokyo',
    'Dakar',
    'Mumbai',
    'Newyork'
]
print(cities[1])
################################################
# Dictionary:
California_symbols = {
    'bird':'Claifornia quail',
    'animal': 'Grizzly bear',
    'flower': 'poppy',
    'fruit':'Apples'
}
# dictionary doen't use indexing becasue each item is already labled. 
print(California_symbols['fruit'])
################################################
# Iteration:
spices = [
    'salt',
    'pepper',
    'cumin',
    'turmeric'
]
for spice in spices:
    print(spice)

# Loop to count to 100 by 5:
i = 5
while i <=100:
    print(i)
    i+=5  
# Modules practice:
# pycache is created when you import your module. 
import testmodules
testmodules.mult(40,8)
################################################
# Strings:
first = 'khawlah'
note = 'award: Nobel Peace Prize'
first_cap = first.capitalize() 
print(first, first_cap)
award_loc= note.find('award: ')
print(award_loc)
award_txt=note[7:]
print(award_txt)
# Regular Expressions: 

import re 
five_digit = '87503'
five_digit_exp= r'\d{5}'
print(five_digit_exp)
print(re.search(five_digit_exp, five_digit))

# miles to kilometeres:
miles = input('Enter a distance in miles: ')
miles_float = float(miles) # string to float if not made, a type error will arise. 
km = miles_float* 1.609344
print(" the value in kilometers is")
print(km)
################################################
# Input/Output files:
infile = open('values.txt','rt')
outfile = open('values-totaled.txt', 'wt')
print('Processing input')
sum=0
for line in infile:
    sum+= int(line)
    print(line.rstrip(), file=outfile)
print('\nTotal: '+ str(sum), file=outfile)
outfile.close()
print('Output complete')



