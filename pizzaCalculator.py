#Alexander den Otter
#PizzaCalculator

#Prijs pizzas per stuk
SmallPizza = 3.50
MediumPizza = 4.25
LargePizza = 5.00

#aantal pizzas die de klant wilt
print('Hoeveel Small Pizzas wilt u?') 
Small = int(input("Vul hier in: "))
print('Hoeveel Medium Pizzas wilt u?')
Medium = int(input("Vul hier in: "))
print('Hoeveel Large Pizzas wilt u')
Large = int(input("Vul hier in: "))

#Uitkomst prijs pizzas
answer = SmallPizza*Small + MediumPizza*Medium + LargePizza*Large
print('Totaal bedrag te betalen = € ' + str (answer))





