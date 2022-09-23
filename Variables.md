# Variables, Boolean Expressions, and Branching

## Class Purpose

Start programming in Python by learning about variables, boolean expressions, and branching.  We are working toward our first project which will be building a game of "Go Fish".  

## Class Outline

1. Variables
   - What they are for
   - Naming Rules
   - Variable Types
   - Variable Values
	 - Bare Types - Literals
	 - Result of an expressions
2. Boolean Expressions
   - Booleans represent true or false values
   - True and False are the foundation of how computers work
   - Booleans allow us to compare different values
   - Compound boolean expressions
3. Branching
   - Allow a computer program to adapt to input
   - if, else, and elif
   - Respond to a boolean expression
	
## Class Notes

### Variables 
Recall the computers only do 4 things:
1. Input Information
2. Store Information
3. Process Information
4. Output Information

Variables are the primary way that a program stores information that it needs to process. They are the fundamental building blocks of programming. Understanding variables - name, value, and type - will essential to understanding how to write effective programs.

Variables are like buckets for storing information in a computer.  The term variables comes from algebra, but are implemented a little bit differently.  Three things make up a variable:

1. Name
2. Value
3. Type

#### Name
The name of the variable is the human readable method for referring to a specific piece of data.  The name of the variable is arbitrary from a computers perspective.  The computer just requires that they be unique and consistent.

> ##### How computers use variables
> When a program is run, the computer will convert all variables names into a numeric code that refers to a specific address in RAM.  Just like physical addresses, computer addresses refer to a specific physical location. Because each location can only store one specific thing, variables can only store a single piece of information.  
> 
> Variables are stored in a table like structure that holds:  
> Example of Variable storage  
>  
> |Name	 | Type (length) | Address in RAM (Memory) | Value |  
> |--------|---------------|-------------------------|-------|  
> |dog_age | int (8)       | AC3F760D                | 3     |  
> |dog_name| String (64)   | AC3F7612                | Kitty |  
> 
> Before a program is run, the computer scans the program to create this look up table of all the variables. Once the computer converts the variable name into an address the computer doesn't pay attention to the name again. Generally the details about how a variable works in a computer are not terribly important until we get to higher level programming concepts.

Naming variables is one of the hardest things about programming.  You want them to be meaningful and descriptive, but not too long or specific.  That being said don't get hung up on finding the perfect name.  It is really easy to change later and the computer doesn't care.

Here are some basic naming rules that you should follow:

1. Code is read and revised more often than it is written. This means that you should optimize for readability not efficient typing.
2. Variable names serve as the main source of information about what your code does. The ideal to strive for is that the code is "self-documenting" meaning that the code does not require any additional comments to explain its purpose or procedure. This does not mean that you should not write comments. It simply means that comments should be reserved for why you did a certain thing rather than what is going on. 
##### Names Example
```python
da = 3
ha = da * 7
print(ha)
```
Compare this to: 
```python			
dog_age = 3
human_equiv_age = dog_age * 7
print(human_equiv_age) 
```
3. Variables names should start with a letter or "_" and may contain letters, number, or underscores. (Applies to Python only)
4. Use variable names for everything in your code. (Even if they will never change). A number that is not assigned to a variable name is often called a "magic number." Strings can have a similar problem. Avoid magic variables even when the number is a fixed and known constant.

See the example in Rule 2 - The "7" on the second line is a magic number. We should fix that by giving it a name.

Another example is often see when computing the area of a circle. The formula is area = π * r^2. We could write this as: 

```python			
area = 3.14 * radius**2
```	

It would be better as: 

```python			
pi = 3.14
area = pi * radius**2
```			

#### Type
A type refers to the type of information that a variable stores. Think of this as python trying to figure out whit size bucket to get for the specific information it is going to hold.

Python has 4 basic variable types:
- Integer - called an Int (int)
- Decimal Number - called a Float (float)
- A true/false value - called a Boolean (Bool)
- A sequence of characters - called a String (str)

Type information is stored with the variable and can _never_ change in a running program. (See the side bar for an example of the lookup table that a computer uses to hold variable information.)

We usually do not need to think too closely about type information in Python.  Python looks at the information that is assigned to a variable when it is created and infers the type.  Most of the time Python gets this right, but occasionally it can't figure it out and you will need to help it.  (Python will complain with an error message when this happens.)

You can use `type(variable_name)` to find the type of a variable in your code or during debugging.

If you need to convert a variable from one type to another you must *cast* it into the new type.

Consider the following case: The number "1" is stored as a string. You can convert it to an integer so you can do math on it by using `int("1")`.
```python
type("1")
type(int("1"))
```

 
The full list of commands for casting is:
```python
int ( . )
float ( . )
bool ( . )
str ( . )
```

Python also allows you to make your own types and also contains some lesser used ones. (More about this later)

#### Value

A variable can only hold a specific piece of information, but when we create a variable we can either assigned to be a bare value called a "literal" or an expression. (i.e. sum = 1+2, this is like Excel where we can either type a value into a cell or use a formula.)  Only the result of the expression is store in a variable and the expression is resolved before the variable is stored.

Example:
```python
a = 2
b = 3
c = a + b
print(c)
# Prints 5
a = 4
print(c)
# Still Prints 5
```

The expressions that you can use depend on the type of the inputs:
 - Integers and Floats - All basic mathematical operations - +, -, *, /, %, **
 - Strings - combine or concatenate 2 strings (+), repeat a string (*)
 - Boolean - boolean arithmatic ( and, or, not - covered later in class)
 - Custom operations called functions are possible - More in a future class
 
Example: Ask for a dog's name and age. Calculate the human equivalent age and then return a greeting with the name of the dog and the age.

```python	
dog_to_human_conversion = 7
dog_name = input("What is your dog's name?")
dog_age = input("How old is your dog?")
human_age = dog_age * dog_to_human_conversion # There is an error on this line.  Can you spot it?
print("Your dog " + dog_name + " would be " + human_age + " years old if they were a human.")
```

##### Sidebar - Python Errors
There are three types of errors in programming:
1. Syntax errors
2. Logic Errors
3. Runtime errors
When Python detects a problem it will raise an error.  It will automatically catch the first Syntax and Runtime errors, but has no ideas when a logic error occurs.
A syntax error occurs when you write invalid Python code.
For Example:
```python
7number = "Seven"
```
produces the following output:
>File "<stdin>", line 1  
>  7number = "Seven"  
>  ^  
>SyntaxError: invalid decimal literal

If we read the error message (the last line) We can see that we have a syntax error and a description of what Python things the error is.  In this and many cases the description is not very helpful.  By the two line above will point to the exact place in the code that the error was found.  Oh yeah, variables can't start with a number.

The second type of error is a logic error.  This occurs when you program runs, but does not produce the output that we expect. This is what happens when we ran our code.  
```python	
dog_to_human_conversion = 7
dog_name = input("What is your dog's name?")
dog_age = input("How old is your dog?")
human_age = dog_age * dog_to_human_conversion # There is an error on this line.  Can you spot it?
print("Your dog " + dog_name + " would be " + human_age + " years old if they were a human.")
# Outputs - Your dog Kitty would be 3333333 years old if they were a human.
```
What happened?  Python thinks that you did everything right, but 3 * 7 should be 21 not 3333333.  Recall the discussion about type?  What happens when you multiple a string by a number?  It repeats the string the given number of times.  This must mean that Python things that `dog_age` is a string "3" instead of the number 3.  We can see this by typing `type(dog_age)` into the Python console.

Let's fix our program:
```python	
dog_to_human_conversion = 7
dog_name = input("What is your dog's name?")
dog_age = int(input("How old is your dog?"))
type(dog_age)
human_age = dog_age * dog_to_human_conversion # There is an error on this line.  Can you spot it?
print("Your dog " + dog_name + " would be " + human_age + " years old if they were a human.")
```
> Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
> TypeError: can only concatenate str (not "int") to str

Uh Oh!  We have another error.  This is the third type of error - a Runtime error.  A Runtime error can only be discovered when a program is run.  They are very common which is why it is important to run your programs early and often.  The sooner you catch a Runtime error the easier it will be to find and fix. A Runtime error occurs when Python can't figure out what you meant.  Usually it occurs when you haven't followed some specific rule, provided bad input, or tried to use a variable that doesn't exist.  There are many types of Runtime errors and Python will try to helpfully point us in the right direction.  In this case we can see from the last line of the output that it is a TypeError.  Python expected a string, but we passed it an integer.  The first two lines in the error message are called the Traceback.  Because the actually error we made might be part of a command before the one Python was currently executing, Python will show us the entire chain of command along with the exact place in the file where it encountered the error.  Learning to decipher Runtime errors will get easier with practice and believe me you will get a lot of practice as you program.

 

### Boolean Expressions

Boolean variables are one of the fundamental types in programming. Boolean variables represent a True or False. These variables form the foundation of how computers work. Remember that all information in a computer is stored as a on/off. In addition the basic building blocks of computers - circuits - are all about making decisions based on these on off values. The other thing to keep in mind is that computers can only make binary decisions. Even if a computer is choosing between three things, it evaluates each choice as a set of pairs. Often this is handled as a cascade. Check the first condition, then check a second condition and so forth.

Boolean Variables are primarily used to make comparisons. The comparison operators are:

- < - Less than
- <= - Less than or equal to
-  > - Greater than
-  >= - Greater than or equal to
- == - Equal to
- != - Not Equal to

It is important to note that these operators have a slightly different meaning in programming than they do in math. In math they represent a statement while in programming they represent a question.

Comparisons are usually used for numbers, but they also can be applied to Strings and Boolean values.
	
Try it: (Open a python console in Visual Studio Code and type in the following code. You can do this by pressing ⌘ + ⇧ + p (on Mac), CTRL+SHIFT+P (on Windows) and search for "Start REPL".)

```python
3 < 5
A" > "b"
"1" < "a"
"20" <= "100"
20 <= 100
"20" == 20
"20" <= 20
True < False
1 != 2
```	

As you can see, you can compare strings and boolean values. With strings it compares them based on alphabetical order, numbers are compared numerically. Is there anything that surprised you in these comparisons?

#### Compound Boolean Expressions

Many times you will want to test against multiple conditions or your code will read better if you can reorganize the boolean logic. Compound expressions allow you to do this. There are three operators for compound boolean expressions. This only apply to boolean values and are executed after all the other logic is resolved. The expressions are:

```python
and
or
not
```

(These are present in all programming languages, but other languages like R use &&, ||, ! for and, or, and not respectively.)

and - Compares two boolean values and if both are "True" then the result is true.

```python		
if age > 18 and us_citizen == True:
	print("You should vote")
```

Notice that both expressions must be True in order for the conditional block to be executed.

or - Compares two boolean values if either one or both are true then the whole statement is true.

```python
if order > 29 or loyalty_member:
	print("Congratulations you get free shipping")
```

Notice that loyalty_member does not have a boolean expression, but is just a variable. This means that loyalty member is  of type boolean so we don't need an expression to convert it to a boolean value.

not - Changes a True value to False and vise-versus.

```python
valid = false
		while not valid:
			email = input("Please enter your email address")
			valid = is_valid_email_address(email)
```	

We will be talking about the while statement in the next section, but you should be able to guess what it does.
Compound expressions can be difficult to evaluate when there are a lot of them strung together. Consider this example:

```python
not True or True and False
``` 

Is the result of this expression True or False. Use parenthesis to make things clear.

```python
not (True) or (True and False)
``` 

### Branching

So far the programs that we have written aren't very interesting. They simply go through a series of steps without making any decisions or following different code paths. think about an automated trading program:

```python
if a stock has dropped by more than 2% then buy that stock
```		  

Nothing we have learned so far would allow us to program this rule, but these rules regularly come up in daily life. To make smarter programs we need to be able to have our computer make decisions based on new input or random events. In computer speak we class this "branching".
	
To branch in Python we use an "if" statement:

```python
if current_temperature < 65:
  print("Better bring a jacket or coat.")
```

Note the colon and the indentation on the next line. In an "if" statement there are four important pieces.

if - let's python know we are evaluating a branch

boolean expression (current_temperature < 65) - the is the condition that we want to evaluate. Notice that in Python unlike some other languages parenthesis are not required. It is not an error to include them however. The boolean statement must evaluate to True or False to be useful. (Python treats any non zero value as true.  This is a common source of errors.)
	
: - This ends the boolean expression and lets python know that whatever comes next should be conditionally evaluated.

indented code block - This is the set of code that will be conditionally executed. The indentation is important since it defines a code block.

> #### Side Note
> Python uses indentation to denote a block of code. This block of code serves as a specific unit in a program. Whenever you change the indentation level, you are specifying that you are entering or exiting a block of code.

```python
# This is the parent block of code
# This is still in the parent block
	# This is called a child block
	# still the child
# We are  back in the parent block
```		  

The Python documentation recommends 4-spaces as the preferred indentation level, but it will accept any number of spaces or tabs as long as it is consistent. When you press tab in Visual Studio Code you will get the 4 space indent by default.

One other thing to remember is that Python will only start a new block when you have a colon and that colon has to be part of a valid python command like an if statement.
	
You can also have a block that only runs when an if statement evaluates to False. This is naturally called an "else"

```python
if current_temp < 65:
	print("Better bring a coat or a jacket")
else:
	print("It looks like a nice day")
```		

You can even evaluate multiple conditions sequentially:

```python
if current_temp < 65:
	print("Better bring a coat or a jacket.")
elif current_temp > 80:
	print("Looks like shorts weather")
else:
	print("You must be in Southern California")
```	

elif is just a contraction of "else if."

Branches are mostly used to process input or a random occurence. This input can come from the user, a sensor, or an internet request.
