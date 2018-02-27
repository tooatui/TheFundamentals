## Things hard to understand
- print function in python 2 vs 3 (print is a statement vs function)
https://www.hackerrank.com/challenges/python-print


## Things that are new to me (in python, but not in Java, C# etc.)
- [Predefined Class Attributes](http://www2.lib.uchicago.edu/keith/courses/python/class/5/), e.g. ``ClassName.__doc__``
- tuple vs list (https://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each)
    - Tuples are fixed size in nature whereas lists are dynamic. In other words, a tuple is immutable whereas a list is mutable. For example, tuple is used in function argument list `*args` 
- yield (generator)
- generator expressions https://medium.freecodecamp.org/python-list-comprehensions-vs-generator-expressions-cef70ccb49db

## Things that are different in other languages
### logical operators
keywords are more of natural languages: e.g. ```and, or, not,``` rather than ```&&, ||, !```
``` 
a = False
b = True

if a and b:
    print("a and b is true")

if a or b:
    print("a or b is true")

if not a
    print("a is not true")
```

### Ternary if statements 
```
# Ternary if statements 
a = 5
b = 6

print("bigger" if a > b else "smaller")
```

### lambda functions
lambda
```
doubla = lambda x: x * 2
print(doubla(21))
```
