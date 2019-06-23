subtotal = input("please input your subtotal and press enter")
taxRate = 0.25 *
tax = taxRate * subtotal
total = tax + subtotal
print("The tax is " + tax + "$")
print("Your Total is" + total)

totaldollar = input("bill total:")
tipper = input("tip per:")
people = input("numer of people:")
price = (totaldollar + tipper
ind = price / people
print("each person should pay = " + ind "$")
