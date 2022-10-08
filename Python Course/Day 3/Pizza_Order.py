
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

amount=0

if size == "S":
    amount+=15
    if add_pepperoni == "Y" :
        amount+=2
    if extra_cheese == "Y":
        amount+=1
elif size == "M":
    amount+=20
    if add_pepperoni == "Y" :
        amount+=3
    if extra_cheese == "Y":
        amount+=1    
elif size == "L":
    amount+=25
    if add_pepperoni == "Y" :
        amount+=3
    if extra_cheese == "Y":
        amount+=1          
print(f"Your final bill is: ${amount}")               
    




