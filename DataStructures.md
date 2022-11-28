# Data Structures

## Class Purpose

Data is the core of any analytics or programming projects.  We have studied basic data types like int, float, string, and boolean.  Those four basic types form the basis of all other data structures.  While you can do a lot with the basic types, at some point you will want to build more complex programs and explore more complex ideas.  In order to do that you will want to start combining basic types into more complex types so that it is easier to reason about the types.  Python provides for a number of different tools for combining data into more complex data structures.  Learning about these data structures abd applying them is the purpose of this lecture.

## Class Outline

1. Tuples
2. Lists or Arrays
3. Dictionaries
4. Sets
5. Classes
	
## Class Notes

### Tuples

At the simplest level you might want to keep multiple pieces of data together in a package.  Tuples are the way to accomplish this in Python.  Tuples are the simplest data structure as they allow you treat multiple values as a single piece of information.  You can create a tuple by using parenthesis like so:

```python
a_tuple = ("a tuple can contain any data type", 12, 3.14, True)
type(a_tuple)
print(a_tuple)
```

Tuples can be useful for storing data that belongs together like a record.  This could be something as simple as a product name and a price or something more complicated like a row in a database.

You can access the elements of a tuple the same way that you access the elements of an array or list.

```python
product = ("Apple", 1.75)
print("A(n)", product[0], "costs $", product[1])
```

Unlike lists however you cannot assign a new value to a specific element in a tuple.  This tuple lives and dies together as a single piece of information.  In programmer speak we call this property "immutable".  If you want to change the value of a field in a tuple you will have to create a new tuple.

The process of creating a tuple is called "packing" a tuple.  You can also "unpack" a tuple to turn it back into its raw values.

```python
product = ("Apple", 1.75)
(productName, price) = product
print(productName)
print(price)
```

Tuples are most useful when returning values from a function.  Functions can only return a single value, but this value can be of any type.  If you want to return more than one value from a function you can use a tuple to combine the information.  You would then unpack the tuple to access the individual elements.  This is by far the most common use for tuples.

```python
import math
def circle_geom(r):
	""" Return (circumference, area) of a circle of radius r """
	c = 2 * math.pi * r
	a = math.pi * r * r
	return (c, a) 

(circum, area) = circle_geom(2)
print("The circumference is", circum)
print("The area is", area)
```

Tuples are very useful for a very narrow range of things.  One of the big problems with tuples is that the individual elements cannot be named which makes it hard to remember what order the elements are stored in and how to access the individual pieces of data.  In practice this means that tuples are usually only used to package a handful of values.  It is rare to see a tuple with more than three values in it and tuples are almost always unpacked right away.

### Lists

We have previous covered lists so I'll keep this section short.  Lists are the same thing as arrays in other languages.  Like tuples they are ordered with unnamed elements.  Unlike tuples they are "mutable" meaning that individual values can be changed and updated.  Unlike most languages Python allows you to mix data types in a list, but this is not recommended.  Lists are most useful when you have a similar set of data that you want to iterate over.  

One interesting thing to try:  Lists can contain tuples and tuples can contain lists.  

Lists are an example of a mutable, ordered information store.  

### Dictionaries

Dictionaries are a powerful and common way of storing information in Python.  They are so useful that many other languages have adopted them.  Dictionaries are similar to lists in many ways, but have a couple of big differences.  The first is that each element of a dictionaries has a name called a key that associates with a value.  They are said to be a collection of key-value pairs.  The second important difference is that dictionaries are unordered.  This means that you cannot just ask for each element in dictionary and expect them to be presented in the same order each time.  

You construct a dictionary in a similar way to a list:

```python
price_list = {"apples": 1.75, "bananas": 0.59, "oranges": 2.29, "pears": 2.77}

print("The price of apples is", price_list["apples"])
print("The price of banannas is", price_list["bananas"])
print("The price of pears is", price_list["pears"])
```

#### Dictionary Operations

You can add and element to a dictionary just as you would think:

```python
price_list["strawberries"] = 5.23
print(price_list)
```


Just like lists, you can delete an element from a dictionary use the `del` command.


```python
del price_list["pears"]
print(price_list)
```

You can also count the total number of items in a dictionary using `len`

#### Dictionary Methods

There are two main methods that every dictionary has.  (Methods are functions that you can call on the dictionary itself they take the form of dictionary.method())

The first method is `.keys()`.  This will return all the keys in a dictionary.  You can use these in a for loop to loop over all the elements in a dictionary or you can turn it into an array for other users.

```python
for fruit in price_list.keys():
	print("The price of ", fruit, " is $", price_list[fruit], sep="")

fruits = list(price_list.keys())
print(fruits)
```

Looping over the keys of a dictionary is so common that you can omit the `.keys()` when you do it.

```python
for fruit in price_list:
	print("The price of ", fruit, " is $", price_list[fruit], sep="")
```

The second common function is `.values()`. It works exactly like `.keys()` does only it returns the values rather than the keys.

```python
fruit_prices = list(price_list.values())
print(fruit_prices)
```

#### Copies vs. aliases

Dictionaries and lists have a  common feature that can trip you up when you are trying to assign one dictionary to another variable name.  The assignment operator `=` creates an alias to the same dictionary rather than creating a copy of the dictionary.  This means that if you assign one dictionary to another name, changing the value in one will affect the other.  If you truly want independent copies you need to use the `.copy()` method.  An example will probably be more clear than text explaining it.

```python
opposites = {"up": "down", "right": "wrong", "yes": "no"}
alias = opposites
copy = opposites.copy()
alias["right"] = "left"
opposites["right"]
copy["right"] = "privilege"
opposites["right"]
```

Notice that changing the value for the `alias` dictionary also changed the value for the original `opposites` dictionary.  On the other hand modifying the copy leaves the original unchanged.

### Sets

Sets are another collection type like tuples, lists, and dictionaries.  The unique thing about sets is that they can only contain each item once.  Unlike dictionaries they aren't a key value pair, but sets just contain values.  

Sets are much less commonly used than dictionaries or lists, but there are a few times when they are the best thing for the job.  

A set is created using `{}` notation similar to how a dictionary works without the colons that specify a key:value pair.

```python
fruit_set = {"Apple", "Banana", "Pineapple", "Orange"}
```

Sets are rarely used, but can be a great solution to certain types of problems.  There are two main things that you can do with sets.  The first is to loop over each item in the set.  The second is to check if an item is already in the set.

```python
for fruit in fruit_set:
	print(fruit, "is a fruit.")

if "Pineapple" in fruit_set:
	print("Yes, Pineapple is in the set")	
```

If you want to add an item to a set you would use `set.add(item)`.  This will add `item` to the set if it is not already present.  

```python
print(fruit_set)
fruit_set.add("Grape")
print(fruit_set)
fruit_set.add("Apple")  # Duplicate - it will not be added
print(fruit_set)
```

### Classes

Classes represent custom data types in Python where you can combine any of the basic types with both data and behavior.  There are many different analogies that have been used to describe what classes do in a program, but all that I have heard are lacking in some way.  Classes are custom data structures that can hold specific types of data and the methods that operate on that data.  This allows us to group data together to to keep things clean and organized.  At the simplest level we can create an object that just holds data.

```python
class Product:
	id = 0
	name = "Item Name Here"
	description = "A generic description"
	quantity_on_hand = 0
	price = 0.0
```

This is represents a generic product with five different pieces of information.  In some sense this can be thought of as a product blueprint or schema.  The five pieces of information have been provided default values.  We can use 'dot notation' to access each of the specific pieces of information in the class.  This information can also be updated using the same dot notion.

```python
print(Product.id)
print(Product.name)
Product.id = 9999
print(Product.id)
```

This is great, but maybe you can see a problem with this.  We have a generic Product in our code, but we really want to work with specific products. and those specific products will have difference variables and attributes.  These specific products are called "instances" and we can create them by using the class name followed by () as if we are calling a function.  We can then update the attributes of the specific instance without changing the generic classes attributes.  

```python
specific_product = Product()
print(specific_product.quantity_on_hand)
specific_product.id = 2213
specific_product.name = "Shovel"
specific_product.description = "A tool that can be used to dig or scoop dirt and rocks"
specific_product.quantity_on_hand = 12
specific_product.price = 19.99
print(Product.id)
print(specific_product.id)
```

You can include any type of data inside a class including other classes.  In this way you can create a complicated data hierarchy that references many other objects.  This is called composition where you pull from difference classes.

```python
class PriceList:
	name = ""
	products = [Product()]
```

Most of your work in programming will be defining and using classes.  In fact all the types we have previously talked about including int, float, bool, and str are classes.  Many times when you create an instance of a class you will also want to fill in the data associated with that class.  We do that by creating a special function in the class called the initializer.

```python
class Product:
	def __init__(self, id, name, description, quantity_on_hand, price):
		self.id = id
		self.name = name
		self.description = description
		self.quantity_on_hand = quantity_on_hand
		self.price = price
```

Notice that with an initializer we no longer have to provide default values for our variables and anytime an object is created the user will have to make sure that every field is provided.  In this way we can ensure that our data is always validated and usable. In addition, we no longer can use the generic version of our product for anything that is useful.  This makes sense because in most cases we only want to manipulate and use the instances of a class not the class itself.

```python
shovel = Product()  # Causes an error message about missing arguments
shovel = Product(id = 1, name = "Shovel", description = "A tool that can be used to dig or scoop dirt and rocks", quantity_on_hand = 12, price = 19.99)
print(shovel.name)
```

There are a number of other special functions that can be attached to classes.  The most commonly used is `__str()__` which provides a string representation of the object that is used when printing out the object.

```python
class Product:
	def __init__(self, id, name, description, quantity_on_hand, price):
		self.id = id
		self.name = name
		self.description = description
		self.quantity_on_hand = quantity_on_hand
		self.price = price
	
	def __str__(self):
		return "Product: " + self.name + ", Price: " + str(self.price) + ", " + str(self.quantity_on_hand) + " on hand."

shovel = Product(id = 1, name = "Shovel", description = "A tool that can be used to dig or scoop dirt and rocks", quantity_on_hand = 12, price = 19.99)
print(shovel)
```

Classes in Python become especially useful as you can write generic functions that operate on a specific instance of a class.  This functions are classed class methods.  Consider what woudl happen if you sold a product.  You would still want to keep the product in your inventory system, but you would want to reduce the number on hand to reflect the sale.  

```python
class Product:
	def __init__(self, id, name, description, quantity_on_hand, price):
		self.id = id
		self.name = name
		self.description = description
		self.quantity_on_hand = quantity_on_hand
		self.price = price
	
	def __str__(self):
		return "Product: " + self.name + ", Price: " + str(self.price) + ", " + str(self.quantity_on_hand) + " on hand."
		
	def sell(self):
		if self.quantity_on_hand > 0:
			self.quantity_on_hand  = self.quantity_on_hand - 1
		else:
			print("Error: You don't have any", self.name, "to sell!")

shovel = Product(id = 1, name = "Shovel", description = "A tool that can be used to dig or scoop dirt and rocks", quantity_on_hand = 12, price = 19.99)
print(shovel)
shovel.sell()
shovel.sell()
print(shovel.quantity_on_hand)
```

Since classes are such a fundamental part of programming there is a lot more that you can learn about how they work and how to use them.  This is just an introduction for now, but it should give you both an idea of how to create and use types as well as why some parts of python look the way that they do.  


## Assignment

Create a class for your specific screen.  We are mostly worried about capturing the data that the screen will capture and not about the specific behaviors that need to be enabled.



