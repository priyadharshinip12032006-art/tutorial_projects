menu={"popcorn":150,
      "coke":90,
      "chips":65,
      "fries":75}
cart=[]
total=0
print("-------menu------")
for key,value in menu.items():
    print(f"{key:10}:{value:.2f}")
while True:
    food=input("enter the iteams u like to order (q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----your order----")
for food in cart:
    total=total+menu.get(food)
    print(food,end=" ")
print()

print(f"total={total:.2f}")