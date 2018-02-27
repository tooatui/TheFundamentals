# Things hard to understand
- print function in python 2 vs 3 (print is a statement vs function)
https://www.hackerrank.com/challenges/python-print


# Things that are new to me (in python, but not in Java, C# etc.)
### [Predefined Class Attributes](http://www2.lib.uchicago.edu/keith/courses/python/class/5/), e.g. ``ClassName.__doc__``
- tuple vs list (https://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each)
    - Tuples are fixed size in nature whereas lists are dynamic. In other words, a tuple is immutable whereas a list is mutable. For example, tuple is used in function argument list `*args` 
    
### yield (generator)

### generator expressions https://medium.freecodecamp.org/python-list-comprehensions-vs-generator-expressions-cef70ccb49db

### list vs set vs tuple
 - A list is sequence of elements in a spedific order, like an array in JavaScript.
 - A tuple is basically an immutable list, meaning that you cannot add, remove or update element. Tuples are fixed size in nature whereas lists are dynamic. Good use for constants. tuple is used in function argument list `*args` 
 - A set is a collection of unordered item within which all elements are unique. 
     ```python
	 lst = [1, 2, 3]
	print(lst[1])


	tpl = (1, 2, 3)
	print(tpl[1])
	# the following statement will throw exception because you cannot update element in tuple
	# tpl[1] = 33

	st = set([1, 2, 3])
	for item in st:
		print(item)
	# the following statement will throw exception: "TypeError: 'set' object does not support indexing"
	# print(st[1])
     ```

# Things that are different in other languages
### logical operators
	keywords are more of natural languages: e.g. ```and, or, not,``` rather than ```&&, ||, !```
	```python
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

# Things that are so cool!
- so easy to set up and start, no more `public static void main(String[] args) throws Exception {}` !!!
- for loop, loop a list has never been so easy!
```
list = [1, 2, 3]
for i in list:
    print(i)
```
- string format
`print("numner of files: {0}".format(len(files)))`


# Resources that I used to learn Python
- Udacity Python course
- Pluralsignt Python course
- Stackoverflow for all sorts of questions (refer my votes)
- My reMarkable python book? (the chapter 1 made me go for python 3.*)
