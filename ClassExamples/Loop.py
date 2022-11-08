import random # This is necessary so that we have access to the operations that generate random numbers
dice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for index, die in enumerate(dice):
    print("The die is currently ", die)
    dice[index] = random.randint(1,6)
    
print(dice)    


