countDogFood = int(input())
countCatFood = int(input())

FOOD_CAT_PRICE = 4
FOOD_DOG_PRICE = 2.50

sumPriceFoodCat = countCatFood * FOOD_CAT_PRICE
sumPriceFoodDog = countDogFood * FOOD_DOG_PRICE

Total = sumPriceFoodCat + sumPriceFoodDog

print(f'{Total} lv.')