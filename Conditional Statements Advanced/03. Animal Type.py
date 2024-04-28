animalType = input()

if animalType == "dog":
    type = 'mammal'
elif animalType == "crocodile":
    type = 'reptile'
elif animalType == "tortoise":
    type = 'reptile'
elif animalType == "snake":
    type = 'reptile'
else:
    type = 'unknown'

print(type)