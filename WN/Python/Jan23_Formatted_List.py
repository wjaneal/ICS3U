#Formatted list
Fruit = ["apples     ", "bananas    ", "mangoes    ", "monkey apples", "pears     "]
Prices = [1.30, 2.99, 3.44, 5.59, 9.99]
print "\tFruit:\tPrice:" 
for i in range(0, len(Fruit)):
	print "\t %s\t%.2f" %(Fruit[i], Prices[i])

