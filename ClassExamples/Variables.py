
input_valid = False
while not input_valid:
    dog_age = input("Dog age(Enter a whole number): ")
    if dog_age.isdigit():
        dog_age = int(dog_age)
        input_valid = True
    else:
        print("Please try again")
         
if dog_age <= 2:
    print("This dog is a puppy!")
    print("It's age is " + str(dog_age))
elif dog_age <= 10:
    print("This dog is an adult. :(")
else: 
    print("This dog is starting to get old.")


dog_to_human_conversion = 7
print(int(dog_age)*dog_to_human_conversion)