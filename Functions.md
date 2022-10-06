# Functions

## Class Purpose

We will be learning about functions and work through a realistic programming exercise.

## Class Outline

1. Quick overview of Functions
2. Work through Wordle Example

## Class Notes

What is wrong with the following code:
```python
dog_name = 'Kitty'
dog_weight = 45
if dog_weight > 20:
	print(dog_name, 'says WOOF WOOF')
else:
	print(dog_name, 'says woof woof')

dog_name = 'Sparky'
dog_weight = 15
if dog_weight > 20:
	print(dog_name, 'says WOOF WOOF')
else:
	print(dog_name, 'says woof woof')

dog_name = 'Jackson'
dog_weight = 12
if dog_weight > 20:
	print(dog_name, 'says WOOF WOOF')
else:
	print(dog_name, 'says woof woof')

dog_name = 'Range'
dog_weight = 65
if dog_weight > 20:
	print(dog_name, 'says WOOF WOOF')
else:
	print(dog_name, 'says woof woof')
```

#### Coding Mantra:
_* Don't Repeat Yourself (DRY) *_
Why would this be such a common coding mantra?

DRY
1. Slows you down
	- Requires a lot of typing
	- Requires you to solve the same problems again and again
2. Increase the chance of errors
	- Anytime you type something in you have a chance of creating errors
	- The probability of an error accumulates with the amount of input
	Copying has the same problem only a little more pernicious.  It is really easy to forget to make a small necessary change in copied code.
3. Making changes or bug fixes becomes much harder
4. Makes it hard to reuse code in different places or programs
	
	
#### Functions
Functions solve these problems.  They allow us to take a block of code and:

- Give it a name
- Call it by name and have it execute the logic

You have already been using functions:
- `print(....)` - Think about the steps a computer requires to actually display something to the screen
- `random.randint(1, 3)`
- `str(...)`

You can tell that these are functions because they have a name followed by a set of parenthesis.

Most of what you will be doing in programming is calling functions that other people have written.  Your job is thus one of finding a function that does what you want, figuring out how to call it, and combining this function with other functions into a program.

Functions are a lot like variables

| Variables | Functions         |
| ---       | ---               |
| Name      | Name              |
| Type      | Return type       |
| Value     | Programming Logic |

Unlike variables, however, a functions expression is evaluated when it is called rather than when it is defined.

Just like variables can't be used before they are defined, functions must be defined before they are called.

#### API
A set of functions that have been packaged together is usually called an API.  (Python calls it a "Module.") Learning an API is the biggest task in programming, but is what will make you an efficient and effective programmer.

You can create your own functions if you can't find something that does what you want.
```python
def bark(name, weight):
	if weight > 20:
		print(name, 'says WOOF WOOF')
	else:
		print(name, 'says woof woof')
```

- def - Tells Python that you are defining a function.
- bark - The name of the function
- (name, weight) - The functions parameters.  Functions can have 0 or more parameters.  (These are variables that serve as a bridge between the calling code and the function.)
- if weight ... - The function body

You can call a function with the name of the function, open parenthesis, value for each parameter, close parenthesis

```python
bark('Kitty', 45)
bark('Sparky', 15)
bark('Jackson', 12)
bark('Ranger', 65)
```


How functions work
- When a function is defined, none of the logic is executed.  It is simply stored so it can be called later.
- When a function is called, the function call is "expanded" and the logic of the function replaces the function call.
Essentially
```python
bark('Kitty', 45)
```

is expanded into
```python
bark.name = 'Kitty'
bark.weight = 45
if bark.weight > 20:
	print(bark.name, 'says WOOF WOOF')
else:
	print(bark.name, 'says woof woof')
```

the "bark." prefix to the variables is just to denote that the variables only apply to this specific bit of code that was part of the bark function.  More on this later today.

### Encapsulation and Abstraction
Functions serve two additional purposes:
- Encapsulation - Code is logically grouped into a compact set of actions that should always be preformed together.  Code that is not part of the group cannot access or change code in the group and the code in the group should not affect code outside the grouping.
- Abstraction - The process of collapsing a set of instructions into a higher level concept that refers to the individual details. Allows you to think at a higher level than a computer instruction.

*Abstraction*
Example: Make a sandwich
Highest level of abstraction:
```python
make_sandwich(peanut_butter, strawberry_jam)
```

Lower level abstraction:
```python
get(white_bread)
get(peanut_butter)
get(strawberry_jam)
put(white_bread.slice, counter)
spread(peanut_butter)
spread(strawberry_jam)
put(white_bread.slice, strawberry_jam)
put_away(white_bread)
put_away(peanut_butter)
put_away(strawberry_jam)
eat(sandwich)
```

Even lower level of abstraction:
```python
walk to pantry
search for white bread
pick up white bread
carry to kitchen counter
place on kitch counter
...
```

And so it continues to individual brain signals dictating specific muscle movements.

The higher the level of abstraction, the easier a problem is to reason about, but the less general the solution.  There is a point where the problem is so abstract that it is not longer a good solution. For example make lunch is probably too high a level of abstraction to be useful without additional clarification.

One of the keys to being a good programmer is being able to think at multiple levels of abstraction and then work at the appropriate level for the current problem. That is one of the keys to pseudo-code.  You start at a high level of abstraction and then slowly expand until you are at a level where it makes sense to start actual programming.  Pseudo-code is so effective because it aids in moving up and down the abstraction ladder.

*Encapsulation*
One of the primary principles of encapsulation is the idea of "variable scope." We have briefly touched on it before, but it becomes essential to understand when working with functions.  You can define variables inside a function, but they are said to be "local" because they do not exist outside the function.

Function parameters are technically local variables.  They are just defined and assigned during the function call instead of with the = operator.

Scope means that you can have the same variable name inside a function that you use in your main program.  I try not to do this however as it causes confusion when you or somebody else is trying to read your code.  It still happens accidentally all the time.  Especially with variables that are slightly generic like "data".

Variables that are defined outside of a function are called "global" variables. The technical rule is that they can global because they can be read from any part of your program.  In Python they can only be written to if you explicitly tag the variable inside your function.

Example code:
```python
greeting = 'Greetings'

def greet(name, message):
	print(greeting, name + '.', message)

greet('June', 'See you soon!')
```

The output of this code is `Greetings June. See you soon!`. Notice that the variable greeting can be accessed from inside the function.

Example 2:
```python
greeting = 'Greetings'

def greet(name, message):
	greeting = 'Hi'
	print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)
```

For this code the output is:
```
Hi June, See you soon!
Greetings
```

Notice that we didn't change the greetings variable even though it looks like it was overwritten inside the function.  This is because the variable inside the function was treated as if it were a brand new variable.  It "masks" or "shadows" the previously defined variable as long as the execution is inside the function.

A final example:
```python
greeting = 'Greetings'

def greet(name, message):
	global greeting
	greeting = 'Hi'
	print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)
```

the output for this code is:
```
Hi June. See you soon!
Hi
```

Notice that the value of the greeting variable was changed inside the function.  This is because we tagged the variable name with the global keyword to tell Python that the variable name was referring to the global variable.

The global keyword is a sign of "code smell" - bad code - that could cause a lot of weird errors.  I don't think that I have ever needed to use it.  Using "global" violates the principle of encapsulation.

#### Return Values
We call a function for two primary purposes:
1. Compute an answer and return the result
2. Do something that produces a "side effect" - an action that changes the state of something outside the function

Examples:
1. `randint(1, 6)` - we want the result of the pseudo-random number generator algorithm that the function returns
2. `print('Hello')`` - we want something changed on the screen.  (Not actually a part of our program.  We actually don't care about the return value of the function.  We just want the side effect.

*Programming Best Practice*
Your functions should either be written to return a result or perform a side-effect, but not both.
You return a value from a function with the `return` statement:
```python
def get_bark(weight):
	if weight > 20:
		return 'WOOF WOOF'
	else:
		return 'woof woof'
```

A function ends immediately after it reaches a return statement.  Nothing after the statement is executed.  While I don't recommend this code, it is equivalent to the previous code:
```python
def get_bark(weight):
	if weight > 20:
		return 'WOOF WOOF'
	return 'woof woof'
```

When you call a function with a return statement, it should be assigned to a variable or immediately used.  Functions called for side effects are almost always on a line by themselves.

#### Special Python Considerations
1. You can give functions default values:

```python
def greet(name, message='You rule!')
	print('Hi', name + '.', message)

greet('John') # Hi John. You rule!
greet('Jennifer', 'How are you today?') # Hi Jennifer, How are you today?
```

Required parameters (parameters without default values) must come before parameters with default values.

```python
def greet(message='You rule!', name):
	print('Hi', name + '.', message)
```

Produces a `SyntaxError: non-default argument follows default argument`

2. When calling a function you can supply parameter names,  This means that you can supply the parameters in any order.
```python
greet('John', 'Howdy partner!')
```
is the same as
```python
greet(message='Howdy partner!', name = 'John')
```

Unnamed parameters must come in the function call before named parameters.