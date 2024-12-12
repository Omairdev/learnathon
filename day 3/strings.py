# create string type variables

name = "Python"
print(name)

message = "I love Python."
print(message)


#String Concatenation 
str1= input('Enter first string: ')
str2= input('Enter second string: ')
result= str1 + str2
print(f"Concatenation of {str1} and {str2} is {result}")



# upper() - Converts the string to uppercase
upper_string = message.upper()
print("Uppercase:", upper_string)

# lower() - Converts the string to lowercase
lower_string = message.lower()
print("Lowercase:", lower_string)


# replace() - Replaces substring inside
replaced_string = message.replace("World", "hyderabad")
print("Replaced:", replaced_string)


# startswith() - Checks if string starts with the specified string
startswith_check = message.startswith("  Hello")
print("Startswith '  Hello':", startswith_check)


# isnumeric() - Checks numeric characters
numeric_check = message.isnumeric()
print("Is numeric:", numeric_check)





