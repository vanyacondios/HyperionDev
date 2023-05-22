# Task 12 - Calculate total stock worth in café.

menu = ["juice", "coffee", "pie", "apple", "milk"]
stock = {"juice" : "5", "coffee" : "9", "pie" : "8", "apple" : "10", "milk" : "3"}
price = {"juice" : "1.99", "coffee" : "3.10", "pie" : "3.40", "apple" : "1", "milk" : "1.50"}
total_stock_worth = 0
print("\n")
for i in menu:
        item_value = round(float(stock[i])*float(price[i]), 2)
        total_stock_worth += item_value
        print(i.capitalize() + " stock value is £" + str(item_value) + ".")
print("\nTOTAL stock is worth: £" + str(total_stock_worth) + ".\n")