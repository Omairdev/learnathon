s = 'HelloWorld'

print(s[:])

print(s[::])


#slicing different chars
first_five_chars = s[:5]
print(first_five_chars)

third_to_fifth_chars = s[2:5]
print(third_to_fifth_chars)


#reversing a string using slicing
reverse_str = s[::-1]
print(reverse_str)



#using indexs
s1 = s[8:1:-1]
print(s1)