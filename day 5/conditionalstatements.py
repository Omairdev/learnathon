#if Statement
number = int(input('Enter a number: '))

# check if number is greater than 0
if number > 0:
    print(f'{number} is a positive number.')

print('A statement outside the if statement.')


#Indentation in Python
x = 1
total = 0

# start of the if statement
if x != 0:
    total += x
    print(total)  
# end of the if statement

print("This is always executed.")




#if else Statement
number = int(input('Enter a number: '))

if number > 0:
    print('Positive number')
else:
    print('Not a positive number')

print('This statement always executes')





#if elif Statement
number = -5

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')





#nested Statement
number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')