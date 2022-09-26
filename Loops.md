# Loop

## Class Purpose

Understand how to repeat programming instructions multiple times in Python.

## Class Outline

1. Loops
   
	
## Class Notes

### Code Blocks

Code blocks are related blocks of code that should be executed as a unit.  They are commonly seen in the statements following an `if` statement, loop, or as a function body.  Unlike many other languages, Python uses intendation to delineate a block of code.  Each block of code is indented, usually by 4 spaces, when the indentation changes, the block of code ends.  Code block must be 1 or more lines long.

```python
# This is the parent block of code

if something True:
	# This is a block of code
	# Notice that it can be multiple lines
# This is no longer in the code block.
# Neither is this.
	
	# This is illegal since it is not part of a code block.  It will cause an 'Indentation Error'
```

The advantage of code block in Python's style is that it makes the code extremely easy to read since it doesn't have extraneous punctuation or words.  The downside is that it can lead to some strange errors that are hard to track down because the beginning and ending of a code block are not explicitly defined.

The place where this will cause you the mose errors is whe nyou try to copy and pate code from another program.

### While Loops

Closely related to if statements are loops.  Many times in programming we want to repeat a statement or block of code until a certain event occurs.  This is called looping.

One way to think about this is: "Please repeat these steps until ... happens".

Like many things, programmers have decided to think about this a little backward.  The common way to express this is as a statement "while this is true execute the following block of code."  The syntax for these statements is:

```python
while expression == True:
	compute_something;
```

One place you can easily see this happening is in the game of "Go Fish"

```python
while sets_left_to_play > 0:
	play_next_round()
```

Inside the while loop, we will often have an "if" statement that changes the expression from False to True. We saw this in the last lesson:

```python
valid = false
while not valid:
	email = input("Please enter your email address")
	valid = is_valid_email_address(email)
```

> #### Side-note: Scope  
> Scope refers to the part of a program that can read or write to a variable.  Scope is defined at the block level.  
>  
> A variable is said to be visible if it can be read or written.  A variable is visible to the code block it is defined in and any child code blocks.  Remember that in python a child code block is any code that is indented to a higher level than the containing code.  

The control variable or expression should be initialized before the while loop so the variable is in the parent scope.  That variable will then be updated in side the while loop which is a child block of the main program.  Remember variables are only visible if they are declared in the same block or a parent block.  The while loop is evaluated at the parent block level so any variables in the expression need to be defined at the parent level.

** Try it (type this code into the an interactive Python session.  (Remember the Visual Studio command is "Run REPL"): *
	
```python
number_of_loops = 0
while number_of_loops < 5:
	number_of_loops = number_of_loops + 1
	print("Completing loop " + str(number_of_loops))
print("We finished.")
```

Beware the infinite loop! This is a programming error that is so common it has its own name.  It occurs when a loop condition is never satisfied.  To stop a program that is caught in an infinite loop you have to force quit.  (Use CTRL+C to force quite a python command like program.)

