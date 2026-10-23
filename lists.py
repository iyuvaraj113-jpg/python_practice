menu = {"idly": 10.00,
        "dosa": 25.00,
        "chapathi":25.00,
        "parota": 30.00,
        "egg": 5.00}

cart =[]
total = 0

print("-----menu-----")
for key, values in menu. items():
    print(f"{key:10}: ${values: 2f}")
print("------------")

while True :
    food = input("select an item (q to quit):").lower()
    if food == "q":
        break
    elif menu .get (food) is not None :
        cart.append (food)

for food in cart:
    toatal+= menu.get (food)
    print(food,end = "")