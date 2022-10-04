# Loop

## Class Purpose

Understand  Lists(aka arrays) and iterating over them.

## Class Outline

1. Lists
   
	
## Class Notes

### Introduction
There is a dice game my kids like to play called "TENZI".  In this game, each player has 10 dice that they roll until they get all dice to have the same number.  

One of the key pieces of data that you needed to store and use was a the value of 10 die.  How would you store this information?

One solution would be to create 10 integer variables:

- dice1
- dice2
- dice3
- dice4
- dice5
- dice6
- dice7
- dice8
- dice9
- dice10

This would be a major pain.  We would have to write each of the variables each time we wanted to roll the dice.  You would quickly get tired of writing the variable name every time.

Wouldn't it be better to just have one variable that can hold all ten values:
	  
```python
dice = die 1 | die 2 | die 3 | die 4 | die 5 | die 6 | die 7 | die 8| die 9 | die 10
```

Python has a solution called _lists_ that does exactly that. (In most other programming languages these are called arrays.)
  
Lists are Python's way of storing structured data.  Data that belongs and is used together, but needs to hold multiple values.

Remember how people say that one of the hardest things in programming is naming things.  Lists partially solve this problem.  You can name one thing and then use it to store multiple values.

Lists are called a container variable because they store multiple values.  The container in a list can hold data of any type:

- Primitives (Int, Float, Boolean and String variables)
- Advanced Types called classes (We haven't covered these yet.  Look for this topic in a future lecture.)
- Lists and other collection type variables (Turtles all the way down)

There is not a formal limitation on how many values a list can store.  After a certain point you will run out of computer memory.  This doesn't ever manifest itself in practical situation because the limit is in the thousands.  If you find your self having problems with running out of memory you should probably look into a different method of storing your data such as databases.

Python doesn't enforce this, but it is best practice to only store one type of data in a given list.  You can have a list of integers, a list of strings, and a list of floats, but you shouldn't have a mixed list of strings and floats.  Mixing data types is a major source of very hard to find bugs.  In addition the items in a list should all be related.  If you have variables that serve a different purpose you should create a named variable for each purpose.

### List Syntax and Programming in Python
  
You crate a list using `[]`.  For example:

```python
smoothies = ['banana', 'passion fruit', 'mango', 'acai berry']
```
Each item in a list is given an index number.  These numbers start counting at 0.  You will see this over and over again in programming.  Programmers like to start counting at 0 instead of one.

Lists are said to be "ordered" because item 0 is always in the first position and so on.

You can access items in a list also using `[]`.

```python
favorite = smoothie[2]
```
This will store the value of "mango" the third item in the list in the variable `favorite`.

You can also update a value in a list using the same notation:
```python
smoothie[3] = "blueberry"
```

The list is now: "banana", "passion fruit", "blueberry", "acai berry"

### Common List Operations

Find the length of a list: 
```python
length = len(smoothies)
```

The answer should be 4.

Access the last item in a list:
```python
last = smoothies[-1]
```

The variable `last` will hold the value of the last item in the list in this case "acai berry". You can count staring from the end using a minus sign.  When counting backward you start with -1. (because 0 was already used.) This is unique to Python as far as I am aware, but ends up being very handy.

Add an item to the end of the list:

```python
smoothies.append("tropical")
```

The smoothies list now contains 5 items.  The 4 items already in the list with "tropical" as the new last item.

Create a new empty list:

```python
newList = []
```

This creates an empty list with 0 items in it.  You will sometimes need to do this before filling a list with items in a loop.
	
Delete an item from the list:
```python
del smoothies[1]
```

The `>smoothies` list now contains 4 items.  The second item - remember counting starts from 0 - has been removed.  This list should now be: "banana", blueberry", "acai berry", "tropical".  This is a little inconsistent, but Python's creators wanted to make this common operation very easy so it is a little unique.

Combine two lists:
```python
list1 = ["A", "B", "C"]
list2 = ["X", "Y", "Z"]
combinedList = list1 + list2
```

This will create a single list with the items from `list1` followed by the items from `list2`.
	
Insert an item into an arbitrary position:
```python
smoothies.insert(1, "raspberry")
```

This will insert "raspberry" into position 1 (the second item) of the list moving the index of all subsequent items up by one.  The list is now: "banana", "raspberry", "blueberry", "acai berry", "tropical"

### List Iteration

Lists are especially useful when you need to preform the same operation on on each item in the list.  Think about "TENZI" where you have to roll each of the ten dice and keep track of the results.  If you store the dice in a list you can loop over each dice and roll it if it is not the target number.

```python
import random # This is necessary so that we have access to the operations that generate random numbers
dice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index = 0
length = len(dice)
while index < length:
	dice[index] = random.randInt(1,6) # Generates a random integer between 1 and 6 inclusive
	index = index + 1
```

This will take each item in the dice list and generate a random number between 1 and 6.  Think about what this code would look like without lists:
```python
dice1 = random.randInt(1, 6)
dice2 = random.randInt(1, 6)
dice3 = random.randInt(1, 6)
dice4 = random.randInt(1, 6)
dice5 = random.randInt(1, 6)
dice6 = random.randInt(1, 6)
dice7 = random.randInt(1, 6)
dice8 = random.randInt(1, 6)
dice9 = random.randInt(1, 6)
dice10 = random.randInt(1, 6)
```
The second set of code repeats itself many more times.  If you have an error in your code you would have to change it in 10 places instead of in one place like you would in the first set of code.

One of the key principles of computer programming is "Don't repeat yourself."  Lists help us do that.

Preforming an operation on each item of a list is such a common task that nearly all programming languages have implemented a shortcut.  We call this "iterating" over a list.  In Python it looks like: ```python
dice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for die in dice:
	die = random.randInt(1,6)
```
This greatly reduces the amount of "boilerplate" code that you have to write and as you become familiar with the syntax feel much easier to read. For loops are by far the most common form of looping.  It is actually pretty rare to see a while loop in production code.  This is mainly due to the shorter code and the lower potential for for bugs related to updating the index.

Sometimes it is easier to work with the index numbers rather than each item in a list.  There is a special Python way of handling this. There is a command `range` that creates a list of numbers. For example if you to create a list of the first five numbers you would use:
```python
numberList = range(5)
```
to create a the list `[0, 1, 2, 3, 4]`.  You could then use a for loop to loop over the range have have each index number like so:
```python
for index in range(5):
	print('Iterating through', i)
```
A common pattern is:
```python
print('The smoothies we have available are:')

length = len(smoothies)
for index in range(length):
	print("Smoothie #", index, smoothies[index]) # Prints the smoothie number and name
```

There is a more advanced way to loop over items in a list and get the index at the same time:
```python
for index, smoothie in enumerate(smoothies):
	print("Smoothie #", index, smoothie)
```