'''

Exercise 8a

Given the string “Tom Dick Harry,” break it into individual words, and then sort
those words alphabetically. Once they’re sorted, print them with commas ( , )
between the names.

'''

string = 'Tom Dick Harry'
string = sorted(string.split(' '))
print(', '.join(string))
