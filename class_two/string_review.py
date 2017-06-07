print(dir(" "))
# returns 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

"($50.00)".lstrip("(").rstrip(")")
# returns '$50.00'
"hello there friends".split()
# returns ['hello', 'there', 'friends']
" ".join("hello there friends".split())
# returns 'hello there friends'
",".join("hello there friends".split())
# returns 'hello,there,friends'

# Python string processing is akin to regular expressions
# We have the methods on strings that we do, to get us equivalence to the
# power of regular expressions

# So for instance, regex has for loops - http://www.regexpal.com/93418
# As an aside: regular expressions are a turing complete language (in Python && Ruby)
# not the case in Javascript or Perl (at least not Perl 5.x
# https://en.wikipedia.org/wiki/Turing_completeness 

# best practice

for i in "abcd":
    print(i)

# returns
# a
# b
# c
# d
starter_string = ''
string_to_process = 'hello there'

for index, elem in enumerate(string_to_process):
     if index == 0:
             starter_string += elem.upper()
     elif index != 0 and string_to_process[index-1].isspace():
             starter_string += elem.upper()
     else:
             starter_string += elem
 
print(starter_string)

# A defense of list comprehensions

string_to_process.capitalize()
# returns 'Hello there'
[i.capitalize() for i in string_to_process.split(' ')]
# returns ['Hello', 'There']
' '.join([i.capitalize() for i in string_to_process.split(' ')])
# returns 'Hello There'

# Fstring v format

f'{x},{y}'
# returns '5,7'
"{},{}".format(x, y)
